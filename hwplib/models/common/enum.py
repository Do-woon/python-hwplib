from enum import IntEnum


class RecordTag(IntEnum):
    BEGIN = 0x10

    # DocInfo
    DOCUMENT_PROPERTIES     = BEGIN
    ID_MAPPINGS             = BEGIN + 1
    BIN_DATA                = BEGIN + 2
    FACE_NAME               = BEGIN + 3
    BORDER_FILL             = BEGIN + 4
    CHAR_SHAPE              = BEGIN + 5
    TAB_DEF                 = BEGIN + 6
    NUMBERING               = BEGIN + 7
    BULLET                  = BEGIN + 8
    PARA_SHAPE              = BEGIN + 9
    STYLE                   = BEGIN + 10
    DOC_DATA                = BEGIN + 11
    DISTRIBUTE_DOC_DATA     = BEGIN + 12
    # BEGIN + 13 is reserved.
    COMPATIBLE_DOCUMENT     = BEGIN + 14
    LAYOUT_COMPATIBILITY    = BEGIN + 15
    TRACKCHANGE             = BEGIN + 16
    MEMO_SHAPE              = BEGIN + 76
    FORBIDDEN_CHAR          = BEGIN + 78
    TRACK_CHANGE            = BEGIN + 80
    TRACK_CHANGE_AUTHOR     = BEGIN + 81
