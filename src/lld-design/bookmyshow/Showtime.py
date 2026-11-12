"""Seat inventory and atomic booking operations for one movie screening."""

from __future__ import annotations

from datetime import datetime
from threading import Lock
from uuid import uuid4

from Movie import Movie
from Reservation import Reservation
from Theater import Theater


class Showtime:
    def __init__(
        self,
        showtime_id: str,
        movie: Movie,
        theater: Theater,
        start_time: datetime,
        screen_name: str,
    ) -> None:
        self.id = showtime_id
        self.movie = movie
        self.theater = theater
        self.start_time = start_time
        self.screen_name = screen_name

        # Preserve the original layout: 26 rows, seats numbered 0 through 20.
        self.all_seats = tuple(
            f"{row}{number}"
            for row in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for number in range(21)
        )
        self._seat_ids = frozenset(self.all_seats)
        self._reservations: dict[str, Reservation] = {}
        self.lock = Lock()

    def is_upcoming(self) -> bool:
        """Compare using the start time's timezone (or local time if naive)."""
        return self.start_time > datetime.now(tz=self.start_time.tzinfo)

    def _get_booked_seats(self) -> set[str]:
        """Caller must hold the lock while reading active reservations."""
        return {
            seat
            for reservation in self._reservations.values()
            for seat in reservation.seat_ids
        }

    def get_available_seats(self) -> list[str]:
        with self.lock:
            booked_seats = self._get_booked_seats()
            return [seat for seat in self.all_seats if seat not in booked_seats]

    def book(self, seat_ids: list[str] | tuple[str, ...]) -> Reservation:
        """Reserve all requested seats, or fail without reserving any."""
        if not isinstance(seat_ids, (list, tuple)) or not seat_ids:
            raise ValueError("Select seats using a nonempty list, such as ['A5']")

        # Detach from the caller's list before validation and storage.
        requested_seats = tuple(seat_ids)
        for seat in requested_seats:
            if not isinstance(seat, str) or seat not in self._seat_ids:
                raise ValueError(f"Invalid seat: {seat}")
        if len(requested_seats) != len(set(requested_seats)):
            raise ValueError("Do not select the same seat twice")

        # Availability checks and the write share one lock, preventing two
        # callers from successfully reserving the same seat.
        with self.lock:
            if not self.is_upcoming():
                raise ValueError("This showtime has already started")
            booked_seats = self._get_booked_seats()
            for seat in requested_seats:
                if seat in booked_seats:
                    raise ValueError(f"Seat {seat} is already booked")

            confirmation_id = str(uuid4())
            reservation = Reservation(confirmation_id, self, requested_seats)
            self._reservations[confirmation_id] = reservation
            return reservation

    def cancel(self, confirmation_id: str) -> Reservation | None:
        """Release the seats; return None if no active reservation matches."""
        with self.lock:
            return self._reservations.pop(confirmation_id, None)
