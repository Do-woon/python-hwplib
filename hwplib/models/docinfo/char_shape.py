from dataclasses import dataclass
from enum import IntEnum
from typing import Dict

from hwplib.models.common.colorref import ColorRef
from hwplib.models.common.bitfield import BitFieldObject
from hwplib.models.docinfo.id_mappings import FaceNameType
from hwplib.models.docinfo.border_fill import BorderType


class UnderlineType(IntEnum):
    NONE = 0  # 없음
    UNDER_TEXT = 1  # 글자 아래
    ABOVE_TEXT = 3  # 글자 위


class OutlineType(IntEnum):
    NONE = 0  # 없음
    SOLID = 1  # 실선
    DOT = 2  # 점선
    THICK = 3  # 굵은 실선(두꺼운 선)
    DASH = 4  # 파선(긴 점선)
    DASH_DOT = 5  # 일점 쇄선 (-.-.-.-.)
    DASH_DOT_DOT = 6  # 이점 쇄선 (-..-..-..)


class ShadowType(IntEnum):
    NONE = 0  # 없음
    DISCONTINUOUS = 1  # 비연속
    CONTINUOUS = 2  # 연속


class EmphasisMarkType(IntEnum):
    NONE = 0  # 없음
    BLACK_CIRCLE = 1  # 검정 동그라미 강조점
    WHITE_CIRCLE = 2  # 속 빈 동그라미 강조전
    VERTICAL_LINE = 3  # ˇ
    TILDE = 4  # ~
    BULLET = 5  # •
    COLON = 6  # :


# Table 35
@dataclass
class CharShapeProperty(BitFieldObject):
    italic: bool  # 기울임 여부
    bold: bool  # 진하게 여부
    underline_type: UnderlineType  # 밑줄 종류
    underline_shape: BorderType  # 밑줄 모양 (Table 25)
    outline_type: OutlineType  # 외곽선 종류
    shadow_type: ShadowType  # 그림자 종류
    emboss: bool  # 양각 여부
    engrave: bool  # 음각 여부
    superscript: bool  # 위 첨자 여부
    subscript: bool  # 아래 첨자 여부
    strikeout_type: bool  # 취소선 여부
    emphasis_mark: EmphasisMarkType  # 강조점 종류
    use_font_space: bool  # 글꼴에 어울리는 빈칸 사용 여부
    strikeout_shape: BorderType  # 취소선 모양 (Table 25)
    kerning: bool  # Kerning 여부

    _spec = {
        "italic": (0, 0, {0: False, 1: True}),
        "bold": (1, 1, {0: False, 1: True}),
        "underline_type": (2, 3, UnderlineType),
        "underline_shape": (4, 7, BorderType),
        "outline_type": (8, 10, OutlineType),
        "shadow_type": (11, 12, ShadowType),
        "emboss": (13, 13, {0: False, 1: True}),
        "engrave": (14, 14, {0: False, 1: True}),
        "superscript": (15, 15, {0: False, 1: True}),
        "subscript": (16, 16, {0: False, 1: True}),
        # bit 17 reserved
        "strikeout_type": (18, 20, {i: bool(i) for i in range(8)}),
        "emphasis_mark": (21, 24, EmphasisMarkType),
        "use_font_space": (25, 25, {0: False, 1: True}),
        "strikeout_shape": (26, 29, BorderType),
        "kerning": (30, 30, {0: False, 1: True}),
    }


# Table 33
@dataclass
class CharShape:
    font_ids: Dict[FaceNameType, int]  # 각 언어에서의 FaceName ID
    ratios: Dict[FaceNameType, int]  # 각 언어에서의 장평 (50~200%)
    char_spacings: Dict[FaceNameType, int]  # 각 언어에서의 자간 (-50~50%)
    relative_sizes: Dict[FaceNameType, int]  # 각 언어에서의 상대 크기 (10~250%)
    char_positions: Dict[FaceNameType, int]  # 각 언어에서의 글자 위치 (-100~100%)

    base_size: int  # 기준 크기 (0~4096 pt)
    property: CharShapeProperty  # 글자 속성 비트 필드

    shadow_gap_x: int  # 그림자 간격 X
    shadow_gap_y: int  # 그림자 간격 Y

    text_color: ColorRef  # 글자 색
    underline_color: ColorRef  # 밑줄 색
    shade_color: ColorRef  # 음영 색
    shadow_color: ColorRef  # 그림자 색

    border_fill_id: int  # BorderFill 레코드 참조 ID
    strikeout_color: ColorRef  # 취소선 색 (v5.0.3.0 이상)
