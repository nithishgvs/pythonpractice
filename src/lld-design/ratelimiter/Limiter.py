from abc import ABC, abstractmethod
from RateLimitResult import RateLimitResult


class Limiter(ABC):
    # every algorithm must implement this method
    @abstractmethod
    def allow(self, client_id: str) -> RateLimitResult:
        pass
