from enum import Enum
import dataclasses
import datetime
import re
from typing import List, Optional, TextIO, Tuple


class ParsingPhase(Enum):
    SECTION_NAME = 0
    TIME = 1
    ORIGINAL_TEXT = 2
    ANNOTATIONS = 3
    PAGE_NUMBER = 4
    END = 5


@dataclasses.dataclass
class Annotation:
    section_name: str
    time: datetime.datetime
    original_text: str
    annotations: str
    page_number: int


@dataclasses.dataclass
class AnnotationList:
    name: str
    author: str
    annotations: List[Annotation]


def parse_name(line: str) -> str:
    match = re.compile(r".*<<(.*)>>").search(line)

    if not match:
        raise ValueError(f"Could not find name in line: {line}")

    return match.group(1)


def parse_author(line: str) -> str:
    return line.strip()


def parse_section_name(line: str) -> str:
    return line.strip()


def parse_time(line: str) -> datetime.datetime:
    match = re.compile(r".*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).*").search(line)
    if not match:
        raise ValueError(f"Could not parse time: {line}")

    return datetime.datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")


def parse_possible_prefix_line(line: str) -> Tuple[Optional[str], str]:
    match = re.compile(r"^\u3010(.*)\u3011(.*)$").search(line)

    if not match:
        return (None, line.strip())

    return match.group(1), match.group(2).strip()


def is_annotation_end(line: str) -> bool:
    match = re.compile(r"^-+$").search(line)

    if not match:
        return False

    return True


def get_annotations(file: TextIO) -> AnnotationList:
    name = ""
    author = ""
    all_annotations: List[Annotation] = []

    section_name: Optional[str] = None
    time: Optional[datetime.datetime] = None
    original_text: List[str] = []
    annotations: List[str] = []
    page_number: Optional[int] = None

    parsing_phase = ParsingPhase.SECTION_NAME

    for line_no, line in enumerate(file):
        prefix, line_data = parse_possible_prefix_line(line)
        if prefix == "Original Text":
            parsing_phase = ParsingPhase.ORIGINAL_TEXT
        elif prefix == "Annotations":
            parsing_phase = ParsingPhase.ANNOTATIONS
        elif prefix == "Page Number":
            parsing_phase = ParsingPhase.PAGE_NUMBER
        elif is_annotation_end(line):
            parsing_phase = ParsingPhase.END

        if line_no == 0:
            name = parse_name(line)
        elif line_no == 1:
            author = parse_author(line)
        elif parsing_phase == ParsingPhase.SECTION_NAME:
            section_name = parse_section_name(line)
            parsing_phase = ParsingPhase.TIME
        elif parsing_phase == ParsingPhase.TIME:
            time = parse_time(line)
            parsing_phase = ParsingPhase.ORIGINAL_TEXT
        elif parsing_phase == ParsingPhase.ORIGINAL_TEXT:
            original_text.append(line_data)
        elif parsing_phase == ParsingPhase.ANNOTATIONS:
            annotations.append(line_data)
        elif parsing_phase == ParsingPhase.PAGE_NUMBER:
            page_number = int(line_data)
        elif parsing_phase == ParsingPhase.END:
            if section_name is None:
                raise ValueError(
                    "Found no section_name in section ending " f"at line {line_no}."
                )
            elif time is None:
                raise ValueError(f"Found no time in section ending at line {line_no}.")
            elif page_number is None:
                raise ValueError(
                    "Found no page_number in section ending " f"at line {line_no}."
                )

            all_annotations.append(
                Annotation(
                    section_name=section_name,
                    time=time,
                    original_text="\n".join(original_text),
                    annotations="\n".join(annotations),
                    page_number=page_number,
                )
            )
            section_name = None
            time = None
            original_text = []
            annotations = []
            page_number = None
            parsing_phase = ParsingPhase.SECTION_NAME

    return AnnotationList(
        name=name,
        author=author,
        annotations=all_annotations,
    )
