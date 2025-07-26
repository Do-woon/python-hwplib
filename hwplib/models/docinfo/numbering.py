from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional

from hwplib.models.common.bitfield import BitFieldObject


# Table 41
class ParagraphNumberFormat(IntEnum):
    NUMBER = 0  # 1, 2, 3 (무한)
    CIRCLED_NUMBER = 1  # ①, ②, ③ (1~20 반복)
    ROMAN_UPPER = 2  # I, II, III (무한)
    ROMAN_LOWER = 3  # i, ii, iii (무한)
    ALPHABET_UPPER = 4  # A, B, C (A~Z 반복)
    ALPHABET_LOWER = 5  # a, b, c (a~z 반복)
    CIRCLED_ALPHABET_UPPER = 6  # Ⓐ, Ⓑ, Ⓒ (A~Z 반복)
    CIRCLED_ALPHABET_LOWER = 7  # ⓐ, ⓑ, ⓒ (a~z 반복)
    HANGUL = 8  # 가, 나, 다 (가~하… 반복)
    CIRCLED_HANGUL = 9  # ㉮, ㉯, ㉰ … (가~하 반복)
    HANGUL_JAMO = 10  # ㄱ, ㄴ, ㄷ (ㄱ~ㅎ 반복)
    CIRCLED_HANGUL_JAMO = 11  # ㉠, ㉡, ㉢ … (ㄱ~ㅎ 반복)
    HANGUL_NUMBER = 12  # 일, 이, 삼 (일~구십구 반복)
    HANJA_NUMBER = 13  # 一, 二, 三 (一~九十九 반복)
    CIRCLED_HANJA_NUMBER = 14  # ㊀, ㊁ … (一~十 반복)
    SIBGAN_HANGUL = 15  # 갑, 을, 병, 정 … (10간)
    SIBGAN_HANJA = 16  # 甲, 乙, 丙, 丁 … (10간 한자)


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
    number_format: ParagraphNumberFormat  # 번호 형식

    _spec = {
        "align_type": (0, 1, ParagraphAlignment),
        "use_inst_width": (2, 2, {0: False, 1: True}),
        "auto_indent": (3, 3, {0: False, 1: True}),
        "distance_type": (4, 4, ParagraphDistanceType),
        "number_format": (5, 9, ParagraphNumberFormat),
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
