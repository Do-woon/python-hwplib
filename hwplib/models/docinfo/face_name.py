from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from hwplib.models.common.bitfield import BitFieldObject


@dataclass
class FaceNameProperty(BitFieldObject):
    has_substitute_font: bool  # 대체 글꼴 존재 여부
    has_font_type_info: bool  # 글꼴 유형 정보 존재 여부
    has_base_font: bool  # 기본 글꼴 존재 여부

    _spec = {
        "has_substitute_font": (7, 7, {
            0: False,
            1: True
        }),
        "has_font_type_info": (6, 6, {
            0: False,
            1: True
        }),
        "has_base_font": (5, 5, {
            0: False,
            1: True
        }),
    }


class SubstituteFontType(IntEnum):
    UNKNOWN = 0
    TTF = 1  # TrueType 글꼴
    HFT = 2  # HWP 전용 글꼴


@dataclass
class FontTypeInfo(BitFieldObject):
    font_family: int  # 글꼴 계열
    serif_style: int  # 세리프 유형
    weight: int  # 굵기
    proportion: int  # 비례
    contrast: int  # 대조
    stroke_deviation: int  # 스트로크 편차
    arm_style: int  # 자획 유형
    letterform: int  # 글자형
    midline: int  # 중간선
    x_height: int  # X-높이

    # Each field is a byte (8 bits).
    _spec = {
        "font_family": (0, 7, None),
        "serif_style": (8, 15, None),
        "weight": (16, 23, None),
        "proportion": (24, 31, None),
        "contrast": (32, 39, None),
        "stroke_deviation": (40, 47, None),
        "arm_style": (48, 55, None),
        "letterform": (56, 63, None),
        "midline": (64, 71, None),
        "x_height": (72, 79, None),
    }


@dataclass
class FaceName:
    property: FaceNameProperty  # 속성
    name: str  # 글꼴 이름
    substitute_font_type: Optional[SubstituteFontType]  # 대체 글꼴 유형
    substitute_font_name: Optional[str]  # 대체 글꼴 이름
    font_type_info: Optional[FontTypeInfo]  # 글꼴 유형 정보
    base_font_name: Optional[str]  # 기본 글꼴 이름
