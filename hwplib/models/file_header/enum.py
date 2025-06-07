from enum import IntEnum


class EncryptVersion(IntEnum):
    NONE = 0
    HWP_25 = 1
    HWP_30_ENHANCED = 2
    HWP_30_OLD = 3
    HWP_70 = 4

    def describe(self):
        return {
            EncryptVersion.NONE: "None",
            EncryptVersion.HWP_25: "HWP <= 2.5",
            EncryptVersion.HWP_30_ENHANCED: "HWP 3.0 Enhanced",
            EncryptVersion.HWP_30_OLD: "HWP 3.0 Old",
            EncryptVersion.HWP_70: "HWP 7.0+",
        }.get(self, "Unknown")


class KoglCountry(IntEnum):
    UNKNOWN = 0
    KOR = 6
    USA = 15

    def describe(self):
        return {
            KoglCountry.UNKNOWN: "Unknown",
            KoglCountry.KOR: "Korea",
            KoglCountry.USA: "United States",
        }.get(self, "Unknown")
