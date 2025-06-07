from enum import IntEnum


class BitFieldObject:

    @classmethod
    def get_spec(cls) -> dict:
        return getattr(cls, "_spec", {})

    @classmethod
    def from_value(cls, value: int):
        from hwplib.utils.bitfield_reader import BitFieldReader
        reader = BitFieldReader(value)
        fields = reader.parse_to_dict(cls.get_spec())
        return cls(**fields)

    def describe(self) -> dict:
        result = {}
        spec = self.get_spec()

        for name, _ in spec.items():
            val = getattr(self, name, None)

            if isinstance(val, BitFieldObject):
                result[name] = val.describe()

            elif isinstance(val, IntEnum):
                result[name] = {
                    "name":
                    val.name,
                    "value":
                    val.value,
                    "desc":
                    val.describe() if hasattr(val, "describe") else val.name
                }

            else:
                result[name] = val

        return result
