from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional

from hwplib.models.common.bitfield import BitFieldObject


class ParagraphAlignment(IntEnum):
    LEFT = 0  # 왼쪽 정렬
    CENTER = 1  # 가운데 정렬
    RIGHT = 2  # 오른쪽 정렬


class ParagraphDistanceType(IntEnum):
    RATIO = 0  # 글자 크기에 대한 상대 비율(%)로 지정
    FIXED = 1  # 거리 값으로 지정


# Table 40
@dataclass
class ParagraphHeadProperty(BitFieldObject):
    align_type: ParagraphAlignment  # 문단 정렬 종류 (0~2)
    use_inst_width: bool  # 번호 너비를 실제 인스턴스 문자열의 너비에 따를지 여부
    auto_indent: bool  # 자동 내어쓰기 여부
    distance_type: ParagraphDistanceType  # 본문과의 거리 해석 방식

    _spec = {
        "align_type": (0, 1, ParagraphAlignment),
        "use_inst_width": (2, 2, {0: False, 1: True}),
        "auto_indent": (3, 3, {0: False, 1: True}),
        "distance_type": (4, 4, ParagraphDistanceType),
    }


# Table 39
@dataclass
class ParagraphHeadInfo:
    property: ParagraphHeadProperty
    width_adjustment: int  # 너비 보정값
    distance_from_body: int  # 본문과의 거리
    char_shape_id: Optional[int]  # 참조하는 글자 모양 ID (None이면 기본 글자 모양 사용)


# Table 38
@dataclass
class LevelNumbering:
    paragraph_head_info: ParagraphHeadInfo  # 문단 머리 정보
    number_format: str  # 번호 형식 (UTF-16LE 문자열)
    start_number: Optional[int] = None  # 레벨별 시작 번호


# Table 38
@dataclass
class Numbering:
    base_start_number: int  # 기본 시작 번호
    levels: List[LevelNumbering]  # 각 레벨에 해당하는 번호 매기기 정보 (level 1-10)
