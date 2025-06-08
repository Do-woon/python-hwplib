from dataclasses import dataclass

@dataclass
class StartNumber:
    page: int
    footnote: int
    endnote: int
    picture: int
    table: int
    equation: int

@dataclass
class CaretPosition:
    list_id: int
    para_index: int
    char_index: int

@dataclass
class DocumentProperties:
    section_count: int
    start_number: StartNumber
    caret_position: CaretPosition
