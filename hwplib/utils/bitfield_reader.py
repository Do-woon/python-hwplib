from enum import Enum
from hwplib.models.common.bitfield import BitFieldObject


class BitFieldReader:

    def __init__(self, value: int):
        self.value = value

    def get_bits(self, start: int, end: int) -> int:
        # Extract bits from start to end (inclusive).
        mask = (1 << (end - start + 1)) - 1
        return (self.value >> start) & mask

    def parse_to_dict(self, field_map: dict) -> dict:
        result = {}
        for name, (start, end, mapping) in field_map.items():
            raw_value = self.get_bits(start, end)

            if isinstance(mapping, dict):
                # Simple value mapping (e.g., 0: "off", 1: "on")
                result[name] = mapping.get(raw_value, f"[Unknown:{raw_value}]")

            elif isinstance(mapping, type) and issubclass(mapping, Enum):
                # Convert Enum value to its name.
                try:
                    result[name] = mapping(raw_value)
                except ValueError:
                    result[name] = f"[Invalid Enum:{raw_value}]"
            elif isinstance(mapping, type) and issubclass(
                    mapping, BitFieldObject):
                # Nested BitFieldObject, create an instance from the raw value.
                result[name] = mapping.from_value(raw_value)
            elif mapping is None:
                # No mapping, just return the raw value.
                result[name] = raw_value

            else:
                result[name] = f"[Unsupported mapping: {mapping}]"

        return result
