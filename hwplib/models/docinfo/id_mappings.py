from dataclasses import dataclass, field
from typing import Dict, Union

from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.enum import FaceNameType

# Order of tags must match the order in the HWP specification, Table 16.
ID_MAPPING_INDEX_TO_TAG = [
    RecordTag.BIN_DATA,
    RecordTag.FACE_NAME,  # Hangul Font
    RecordTag.FACE_NAME,  # English Font
    RecordTag.FACE_NAME,  # Hanja Font
    RecordTag.FACE_NAME,  # Japanese Font
    RecordTag.FACE_NAME,  # Etc Font
    RecordTag.FACE_NAME,  # Symbol Font
    RecordTag.FACE_NAME,  # User Font
    RecordTag.BORDER_FILL,
    RecordTag.CHAR_SHAPE,
    RecordTag.TAB_DEF,
    RecordTag.NUMBERING,
    RecordTag.BULLET,
    RecordTag.PARA_SHAPE,
    RecordTag.STYLE,
    RecordTag.MEMO_SHAPE,  # (5.0.2.1+)
    RecordTag.TRACK_CHANGE,  # (5.0.3.2+)
    RecordTag.TRACK_CHANGE_AUTHOR,  # (5.0.3.2+)
]


@dataclass
class IDMappings:
    counts: Dict[Union[RecordTag, tuple[RecordTag, FaceNameType]],
                 int] = field(default_factory=dict)

    def get_count(self, tag: RecordTag, subtype: FaceNameType = None) -> int:
        key = (tag, subtype) if subtype else tag
        return self.counts.get(key, 0)
