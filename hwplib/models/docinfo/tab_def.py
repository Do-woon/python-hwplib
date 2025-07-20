from dataclasses import dataclass
from enum import IntEnum
from typing import List

from hwplib.models.common.bitfield import BitFieldObject
from hwplib.models.docinfo.border_fill import BorderType


@dataclass
class TabDefProperty(BitFieldObject):
    auto_tab_left: bool  # 문단 왼쪽 끝 자동 탭(내어 쓰기용 자동 탭) 여부
    auto_tab_right: bool  # 문단 오른쪾 끝 자동 탭 유무

    _spec = {
        "auto_tab_left": (0, 0, {0: False, 1: True}),
        "auto_tab_right": (1, 1, {0: False, 1: True}),
    }


class TabType(IntEnum):
    LEFT = 0  # 왼쪽
    RIGHT = 1  # 오른쪽
    CENTER = 2  # 가운데
    DECIMAL = 3  # 소수점


@dataclass
class TabInfo:
    position: int  # 탭의 위치
    tap_type: TabType  # 탭의 종류
    fill_type: BorderType  # 탭의 채움 종류 (Table 25)


@dataclass
class TabDef:
    property: TabDefProperty
    tab_infos: List[TabInfo]
