"""Regression tests. Run with unittest discovery as shown in README.md."""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import FrozenInstanceError
from datetime import datetime, timedelta, timezone
from threading import Barrier
import unittest

from BookingSystem import BookingSystem
from Movie import Movie
from Showtime import Showtime
from Theater import Theater


class BookingSystemTests(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("movie-1", "Interstellar")
        self.first = Theater("theater-1", "Downtown")
        self.second = Theater("theater-2", "Uptown")
        future = datetime.now() + timedelta(days=1)
        self.show1 = Showtime("show-1", self.movie, self.first, future, "Screen 1")
        self.show2 = Showtime("show-2", self.movie, self.second, future, "Screen 2")
        self.first.add_showtime(self.show1)
        self.second.add_showtime(self.show2)
        self.system = BookingSystem([self.first, self.second])

    def test_theater_lookup_checks_later_theaters_and_unknown_ids(self):
        self.assertEqual(self.system.get_showtimes_at_theater(self.second.id), [self.show2])
        with self.assertRaisesRegex(ValueError, "Theater not found"):
            self.system.get_showtimes_at_theater("missing")

    def test_search_filters_past_shows_and_normalizes_title(self):
        self.show1.start_time = datetime.now() - timedelta(days=1)
        self.assertEqual(self.system.search_movies("  STELLAR  "), [self.show2])
        self.assertEqual(self.system.search_movies("  "), [])
        self.assertEqual(self.system.get_showtimes_at_theater(self.first.id), [])

    def test_booking_and_cancellation_in_later_showtime(self):
        requested = ["A5", "A6"]
        reservation = self.system.book(self.show2.id, requested)
        requested.append("A7")
        self.assertEqual(reservation.seat_ids, ("A5", "A6"))
        self.assertNotIn("A5", self.system.get_available_seats(self.show2.id))
        self.assertIn("A5", self.system.get_available_seats(self.show1.id))
        self.assertIs(self.system.cancel_reservation(reservation.confirmation_id), reservation)
        self.assertIn("A5", self.system.get_available_seats(self.show2.id))
        with self.assertRaisesRegex(ValueError, "already cancelled"):
            self.system.cancel_reservation(reservation.confirmation_id)

    def test_reservation_cannot_be_reassigned_to_release_booked_seats(self):
        reservation = self.show1.book(["A5"])
        with self.assertRaises(FrozenInstanceError):
            reservation.seat_ids = ("A6",)
        self.assertNotIn("A5", self.show1.get_available_seats())

    def test_invalid_requests_leave_inventory_unchanged(self):
        before = self.show1.get_available_seats()
        for seats in ([], "A5", ["A5", "A5"], ["A5", "AA1"], [["A5"]]):
            with self.subTest(seats=seats):
                with self.assertRaises(ValueError):
                    self.show1.book(seats)
                self.assertEqual(self.show1.get_available_seats(), before)

    def test_conflicting_request_does_not_partially_book(self):
        self.show1.book(["A5"])
        with self.assertRaises(ValueError):
            self.show1.book(["A6", "A5"])
        self.assertIn("A6", self.show1.get_available_seats())

    def test_started_show_cannot_be_booked(self):
        self.show1.start_time = datetime.now() - timedelta(seconds=1)
        with self.assertRaisesRegex(ValueError, "already started"):
            self.show1.book(["A5"])

    def test_timezone_aware_start_time_supports_search_and_booking(self):
        self.show1.start_time = datetime.now(timezone.utc) + timedelta(days=1)
        self.assertIn(self.show1, self.system.search_movies("Interstellar"))
        self.assertEqual(self.show1.book(["A5"]).seat_ids, ("A5",))

    def test_concurrent_requests_cannot_double_book(self):
        barrier = Barrier(2)

        def attempt_booking():
            barrier.wait(timeout=5)
            try:
                return self.show1.book(["A5"])
            except ValueError:
                return None

        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(lambda _: attempt_booking(), range(2)))
        self.assertEqual(sum(result is not None for result in results), 1)
        self.assertNotIn("A5", self.show1.get_available_seats())

    def test_schedule_rejects_duplicate_ids_and_wrong_ownership(self):
        with self.assertRaises(ValueError):
            BookingSystem([self.first, Theater(self.first.id, "Duplicate")])
        duplicate = Showtime(self.show1.id, self.movie, self.second, self.show2.start_time, "3")
        self.second.add_showtime(duplicate)
        with self.assertRaises(ValueError):
            BookingSystem([self.first, self.second])
        with self.assertRaises(ValueError):
            self.first.add_showtime(self.show2)
        with self.assertRaises(ValueError):
            self.first.add_showtime(self.show1)

    def test_unknown_showtime_and_confirmation_raise_clear_errors(self):
        with self.assertRaisesRegex(ValueError, "Showtime not found"):
            self.system.get_available_seats("missing")
        with self.assertRaisesRegex(ValueError, "Reservation not found"):
            self.system.cancel_reservation("missing")


if __name__ == "__main__":
    unittest.main()
