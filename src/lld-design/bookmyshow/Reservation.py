"""An immutable confirmation for seats booked at one showtime."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Showtime import Showtime


@dataclass(frozen=True)
class Reservation:
    confirmation_id: str
    showtime: Showtime
    seat_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        # Also protect reservations constructed directly from a mutable list.
        object.__setattr__(self, "seat_ids", tuple(self.seat_ids))
