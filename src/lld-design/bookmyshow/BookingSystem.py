"""Search and booking facade over a preconfigured theater schedule."""

from collections.abc import Iterable

from Reservation import Reservation
from Showtime import Showtime
from Theater import Theater


class BookingSystem:
    def __init__(self, theaters: Iterable[Theater]) -> None:
        # Configure theaters and showtimes first. These indexes represent the
        # schedule at construction; adding showtimes later requires rebuilding.
        self.theaters = tuple(theaters)
        self._theaters_by_id: dict[str, Theater] = {}
        self.showtimes: dict[str, Showtime] = {}

        for theater in self.theaters:
            if theater.id in self._theaters_by_id:
                raise ValueError("Theater IDs must be unique")
            self._theaters_by_id[theater.id] = theater

            for showtime in theater.showtimes:
                if showtime.theater is not theater:
                    raise ValueError("Showtime belongs to a different theater")
                if showtime.id in self.showtimes:
                    raise ValueError("Showtime IDs must be unique across theaters")
                self.showtimes[showtime.id] = showtime

    def search_movies(self, title: str) -> list[Showtime]:
        """Return upcoming showtimes matching a case-insensitive title fragment."""
        if not title or not title.strip():
            return []
        search_text = title.strip().casefold()
        return [
            showtime
            for showtime in self.showtimes.values()
            if search_text in showtime.movie.title.casefold() and showtime.is_upcoming()
        ]

    def get_showtimes_at_theater(self, theater_id: str) -> list[Showtime]:
        theater = self._theaters_by_id.get(theater_id)
        if theater is None:
            raise ValueError("Theater not found")
        return [
            showtime
            for showtime in self.showtimes.values()
            if showtime.theater is theater and showtime.is_upcoming()
        ]

    def _find_showtime(self, showtime_id: str) -> Showtime:
        showtime = self.showtimes.get(showtime_id)
        if showtime is None:
            raise ValueError("Showtime not found")
        return showtime

    def get_available_seats(self, showtime_id: str) -> list[str]:
        return self._find_showtime(showtime_id).get_available_seats()

    def book(self, showtime_id: str, seat_ids: list[str] | tuple[str, ...]) -> Reservation:
        return self._find_showtime(showtime_id).book(seat_ids)

    def cancel_reservation(self, confirmation_id: str) -> Reservation:
        """Search all showtimes and return the cancelled reservation."""
        for showtime in self.showtimes.values():
            reservation = showtime.cancel(confirmation_id)
            if reservation is not None:
                return reservation
        raise ValueError("Reservation not found or already cancelled")
