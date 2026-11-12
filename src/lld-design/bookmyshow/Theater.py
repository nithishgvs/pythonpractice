"""A theater and the showtimes scheduled there."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Showtime import Showtime


class Theater:
    def __init__(self, theater_id: str, name: str) -> None:
        self.id = theater_id
        self.name = name
        self.showtimes: list[Showtime] = []

    def add_showtime(self, showtime: Showtime) -> None:
        if showtime.theater is not self:
            raise ValueError("This showtime belongs to a different theater")
        if any(existing.id == showtime.id for existing in self.showtimes):
            raise ValueError("Showtime ID already exists in this theater")
        self.showtimes.append(showtime)

    def add_showtme(self, showtime: Showtime) -> None:
        """Compatibility alias for the original misspelled method."""
        self.add_showtime(showtime)
