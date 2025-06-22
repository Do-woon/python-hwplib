from dataclasses import dataclass


@dataclass
class ColorRef:
    red: int
    green: int
    blue: int

    @classmethod
    def from_uint32(cls, value: int) -> "ColorRef":
        blue = (value >> 0) & 0xFF
        green = (value >> 8) & 0xFF
        red = (value >> 16) & 0xFF
        return cls(red=red, green=green, blue=blue)

    def to_uint32(self) -> int:
        return (self.red << 16) | (self.green << 8) | self.blue

    def __str__(self) -> str:
        return f"ColorRef(R: {self.red}, G: {self.green}, B: {self.blue})"
