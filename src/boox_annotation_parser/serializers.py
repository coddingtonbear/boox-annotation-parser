import json
from abc import ABCMeta
from abc import abstractmethod
from typing import Dict

from yaml import safe_dump

from boox_annotation_parser.parser import AnnotationList


class BaseSerializer(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, annotations: AnnotationList) -> str:
        ...

    def to_dictionary(self, annotations: AnnotationList) -> Dict:
        dict_annotations = []
        for annotation in annotations.annotations:
            dict_annotations.append(
                {
                    "section_name": annotation.section_name,
                    "time": annotation.time.strftime("%Y-%m-%d %H:%M"),
                    "original_text": annotation.original_text,
                    "annotations": annotation.annotations,
                    "page_number": annotation.page_number,
                }
            )

        return {
            "name": annotations.name,
            "author": annotations.author,
            "annotations": dict_annotations,
        }


class JsonSerializer(BaseSerializer):
    def serialize(self, annotations: AnnotationList) -> str:
        return json.dumps(
            self.to_dictionary(annotations),
            indent=4,
        )


class NLJsonSerializer(BaseSerializer):
    def serialize(self, annotations: AnnotationList) -> str:
        lines = [
            json.dumps(d).replace("\n", "\\n")
            for d in self.to_dictionary(annotations)["annotations"]
        ]
        return "\n".join(lines)


class YamlSerializer(BaseSerializer):
    def serialize(self, annotations: AnnotationList) -> str:
        return safe_dump(
            self.to_dictionary(annotations),
        )
