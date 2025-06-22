from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from hwplib.models.common.bitfield import BitFieldObject


class BinDataType(IntEnum):
    LINK = 0  # 그림 외부 파일 참조 (0x0000)
    EMBEDDING = 1  # 그림 파일 포함 (0x0001)
    STORAGE = 2  # OLE 포함 (0x0002)


class BinDataCompress(IntEnum):
    DEFAULT = 0  # 스토리지의 디폴트 모드 따라감 (0x0000)
    COMPRESSED = 1  # 무조건 압축 (0x0010)
    UNCOMPRESSED = 2  # 무조건 압축하지 않음 (0x0020)


class BinDataAccessState(IntEnum):
    UNACCESSED = 0  # 아직 access 된 적 없는 상태 (0x0000)
    SUCCESS = 1  # access에 성공하여 파일을 찾은 상태 (0x0100)
    ERROR = 2  # access에 실패한 에러 상태 (0x0200)
    IGNORED_ERROR = 3  # 링크 access가 실패했으나 무시된 상태 (0x0300)


@dataclass
class BinDataProperty(BitFieldObject):
    type: BinDataType
    compress: BinDataCompress
    state: BinDataAccessState

    _spec = {
        "type": (0, 3, BinDataType),
        "compress": (4, 5, BinDataCompress),
        "state": (8, 9, BinDataAccessState),
    }


@dataclass
class BinData:
    property: BinDataProperty
    absolute_path: Optional[str] = None
    relative_path: Optional[str] = None
    storage_id: Optional[int] = None
    extension: Optional[str] = None
