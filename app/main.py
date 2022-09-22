class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return self + Distance(other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __ge__(self, other) -> bool:
        return not self < other

    def __le__(self, other) -> bool:
        return not self > other
