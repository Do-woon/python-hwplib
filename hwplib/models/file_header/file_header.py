from dataclasses import dataclass

from .bitfield import FileHeaderAdditionalProperties, FileHeaderProperties
from .enum import EncryptVersion, KoglCountry


@dataclass
class FileHeader:
    signature: str
    version_raw: int
    properties: FileHeaderProperties
    additional_properties: FileHeaderAdditionalProperties
    encrypt_version: EncryptVersion
    kogl_country: KoglCountry

    @property
    def version_str(self) -> str:
        MM = (self.version_raw >> 24) & 0xFF
        nn = (self.version_raw >> 16) & 0xFF
        PP = (self.version_raw >> 8) & 0xFF
        rr = self.version_raw & 0xFF
        return f"{MM}.{nn}.{PP}.{rr}"

    def __str__(self):
        return (
            f"<HWP FileHeader>\n"
            f"  Signature       : {self.signature}\n"
            f"  Version         : {self.version_str} (0x{self.version_raw:08X})\n"
            f"  Properties      : {self.properties.describe()}\n"
            f"  Additional Props: {self.additional_properties.describe()}\n"
            f"  Encryption Ver  : {self.encrypt_version.describe()}\n"
            f"  KOGL Country    : {self.kogl_country.describe()}")
