from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from hwplib.models.common.bitfield import BitFieldObject


class LineSpacingType(IntEnum):
    PERCENT = 0  # 글자에 따라 (%)
    FIXED = 1  # 고정값
    ONLY_MARGIN = 2  # 여백만 지정


class Alignment(IntEnum):
    JUSTIFY = 0  # 양쪽 정렬
    LEFT = 1  # 왼쪽 정렬
    RIGHT = 2  # 오른쪽 정렬
    CENTER = 3  # 가운데 정렬
    DISTRIBUTE = 4  # 배분 정렬
    DIVIDE = 5  # 나눔 정렬


class BreakLatinWord(IntEnum):
    WORD = 0  # 단어 기준
    HYPHEN = 1  # 하이픈 기준
    LETTER = 2  # 글자 기준


class BreakHangulWord(IntEnum):
    WORD = 0  # 어절 기준
    LETTER = 1  # 글자 기준


class VerticalAlignment(IntEnum):
    FONT = 0  # 글꼴 기준
    TOP = 1  # 위쪽
    CENTER = 2  # 가운데
    BOTTOM = 3  # 아래쪽


class ParaHeadShape(IntEnum):
    NONE = 0  # 없음
    OUTLINE = 1  # 개요
    NUMBER = 2  # 번호
    BULLET = 3  # 글머리표 (Bullet)


# Table 44
@dataclass
class ParaShapeProperty1(BitFieldObject):
    line_spacing_type: LineSpacingType  # 줄 간격 종류 (한글 2007 이하에서만 사용)
    alignment: Alignment  # 정렬 방식
    break_latin_word: BreakLatinWord  # 영어 줄나눔 기준
    break_hangul_word: BreakHangulWord  # 한글 줄나눔 기준
    use_line_space_between_para: bool  # 편집 용지의 줄 격자 사용 여부
    minimum_space: int  # 공백 최소값 (0 ~ 75%)
    protect_single_line: bool  # 외톨이줄 보호 여부
    next_para_join: bool  # 다음 문단과 함께 여부
    protect_para: bool  # 문단 보호 여부
    page_break_before: bool  # 문단 앞에서 항상 쪽 나눔 여부
    vertical_alignment: VerticalAlignment  # 세로 정렬
    use_font_line_space: bool  # 글꼴에 어울리는 줄 높이 여부
    para_head_shape: ParaHeadShape  # 문단 머리 모양 종류
    para_level: int  # 문단 수준(1 ~ 7, 0은 문단 수준 없음)
    border_connect: bool  # 문단 테두리 연결 여부
    ignore_para_margin: bool  # 문단 여백 무시 여부
    last_line_shape: bool  # 문단 꼬리 모양

    _spec = {
        "line_spacing_type": (0, 1, LineSpacingType),
        "alignment": (2, 4, Alignment),
        "break_latin_word": (5, 6, BreakLatinWord),
        "break_hangul_word": (7, 7, BreakHangulWord),
        "use_line_space_between_para": (8, 8, {
            0: False,
            1: True
        }),
        "minimum_space": (9, 15, {
            i: i
            for i in range(76)
        }),  # 0 ~ 75%
        "protect_single_line": (16, 16, {
            0: False,
            1: True
        }),
        "next_para_join": (17, 17, {
            0: False,
            1: True
        }),
        "protect_para": (18, 18, {
            0: False,
            1: True
        }),
        "page_break_before": (19, 19, {
            0: False,
            1: True
        }),
        "vertical_alignment": (20, 21, VerticalAlignment),
        "use_font_line_space": (22, 22, {
            0: False,
            1: True
        }),
        "para_head_shape": (23, 24, ParaHeadShape),
        "para_level": (25, 27, {
            i: i
            for i in range(0, 8)
        }),  # 0 ~ 7
        "border_connect": (28, 28, {
            0: False,
            1: True
        }),
        "ignore_para_margin": (29, 29, {
            0: False,
            1: True
        }),
        "last_line_shape": (30, 30, {
            0: False,
            1: True
        }),
    }


# Table 45
@dataclass
class ParaShapeProperty2(BitFieldObject):
    single_line_input: bool  # 한 줄로 입력 여부
    auto_spacing_hangul_english: bool  # 한글-영문 간격 자동 조정 여부
    auto_spacing_hangul_number: bool  # 한글-숫자 간격 자동 조정 여부

    _spec = {
        "single_line_input": (0, 1, {
            0: False,
            1: True
        }),
        "auto_spacing_hangul_english": (4, 4, {
            0: False,
            1: True
        }),
        "auto_spacing_hangul_number": (5, 5, {
            0: False,
            1: True
        }),
    }


class LineSpacingKind(IntEnum):
    AUTO = 0  # 글자에 따라
    FIXED = 1  # 고정값
    ONLY_MARGIN = 2  # 여백만 지정
    MINIMUM = 3  # 최소값 사용


# Table 46
@dataclass
class ParaShapeProperty3(BitFieldObject):
    line_spacing_kind: LineSpacingKind  # 줄 간격 종류

    _spec = {
        "line_spacing_kind": (0, 4, LineSpacingKind),
    }


# Table 43
@dataclass
class ParaShape:
    property1: ParaShapeProperty1  # 속성1
    left_margin: int  # 왼쪽 여백
    right_margin: int  # 오른쪽 여백
    indent: int  # 들여쓰기/내어쓰기
    top_para_space: int  # 문단 간격 위
    bottom_para_space: int  # 문단 간격 아래
    line_space_old: int  # 줄간격 (5.0.2.5 미만 버전)
    tab_definition_id: int  # TabDef ID
    numbering_bullet_id: int  # Numbering / Bullet ID
    border_fill_id: int  # 테두리/배경 (BorderFill) ID
    left_border_space: int  # 테두리 왼쪽 간격
    right_border_space: int  # 테두리 오른쪽 간격
    top_border_space: int  # 테두리 위쪽 간격
    bottom_border_space: int  # 테두리 아래쪽 간격
    property2: Optional[ParaShapeProperty2] = None  # 속성2 (버전 >= 5.0.1.7)
    property3: Optional[ParaShapeProperty3] = None  # 속성3 (버전 >= 5.0.2.5)
    line_spacing: Optional[int] = None  # 줄간격 (버전 >= 5.0.2.5)
