from dataclasses import dataclass
from enum import IntEnum

from hwplib.models.common.bitfield import BitFieldObject


@dataclass
class FileHeaderProperties(BitFieldObject):
    is_compressed: bool  # 압축 여부 (bit 0)
    is_encrypted: bool  # 암호화 여부 (bit 1)
    is_for_distribution: bool  # 배포용 문서 여부 (bit 2)
    is_script_saved: bool  # 스크립트 저장 여부 (bit 3)
    is_drm: bool  # DRM 보안 문서 여부 (bit 4)
    has_xml_template: bool  # XML template 스토리지 존재 여부 (bit 5)
    has_document_history: bool  # 문서 이력 관리 존재 여부 (bit 6)
    has_digital_signature: bool  # 전자 서명 존재 여부 (bit 7)
    is_certificate_encrypted: bool  # 공인인증서 암호화 여부 (bit 8)
    has_pre_saved_signature: bool  # 전자 서명 예비 저장 여부 (bit 9)
    is_certificate_drm: bool  # 공인 인증서 DRM 보안 문서 여부 (bit 10)
    is_ccl: bool  # CCL 문서 여부 (bit 11)
    is_mobile_optimized: bool  # 모바일 최적화 여부 (bit 12)
    is_personal_info_protected: bool  # 개인 정보 보안 문서 여부 (bit 13)
    is_change_tracking: bool  # 변경 추적 문서 여부 (bit 14)
    is_kogl_copyright: bool  # 공공누리(KOGL) 저작권 문서 여부 (bit 15)
    has_video_control: bool  # 비디오 컨트롤 포함 여부 (bit 16)
    has_table_of_contents_control: bool  # 차례 필드 컨트롤 포함 여부 (bit 17)
    reserved: int = 0  # 예약 필드 (bit 18-31, 사용되지 않음)

    _spec = {
        "is_compressed": (0, 0, {
            0: False,
            1: True
        }),
        "is_encrypted": (1, 1, {
            0: False,
            1: True
        }),
        "is_for_distribution": (2, 2, {
            0: False,
            1: True
        }),
        "is_script_saved": (3, 3, {
            0: False,
            1: True
        }),
        "is_drm": (4, 4, {
            0: False,
            1: True
        }),
        "has_xml_template": (5, 5, {
            0: False,
            1: True
        }),
        "has_document_history": (6, 6, {
            0: False,
            1: True
        }),
        "has_digital_signature": (7, 7, {
            0: False,
            1: True
        }),
        "is_certificate_encrypted": (8, 8, {
            0: False,
            1: True
        }),
        "has_pre_saved_signature": (9, 9, {
            0: False,
            1: True
        }),
        "is_certificate_drm": (10, 10, {
            0: False,
            1: True
        }),
        "is_ccl": (11, 11, {
            0: False,
            1: True
        }),
        "is_mobile_optimized": (12, 12, {
            0: False,
            1: True
        }),
        "is_personal_info_protected": (13, 13, {
            0: False,
            1: True
        }),
        "is_change_tracking": (14, 14, {
            0: False,
            1: True
        }),
        "is_kogl_copyright": (15, 15, {
            0: False,
            1: True
        }),
        "has_video_control": (16, 16, {
            0: False,
            1: True
        }),
        "has_table_of_contents_control": (17, 17, {
            0: False,
            1: True
        }),
        "reserved": (18, 31, None),
    }


@dataclass
class FileHeaderAdditionalProperties(BitFieldObject):
    ccl_info: bool = False  # CCL, 공공누리 라이선스 정보 (bit 0)
    is_copy_restricted: bool = False  # 복제 제한 여부 (bit 1)
    # 동일 조건 하에 복제 허가 여부 (복제 제한인 경우 무시, bit 2)
    is_copy_allowed_under_same_conditions: bool = False
    reserved: int = 0  # 예약

    _spec = {
        "ccl_info": (0, 0, {
            0: False,
            1: True
        }),
        "is_copy_restricted": (1, 1, {
            0: False,
            1: True
        }),
        "is_copy_allowed_under_same_conditions": (2, 2, {
            0: False,
            1: True
        }),
        "reserved": (3, 31, None),
    }


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
