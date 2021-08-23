# flake8: noqa
import datetime
from io import StringIO
from unittest import TestCase

from boox_annotation_parser import parser

EXAMPLE_FILE = """\
BOOX Reading Notes | <<Trilogia de la Fundacion (Spanish Edition) - Isaac Asimov (146)>>
Isaac Asimov
Cuarta parte. Los comerciantes
Time：2021-08-17 22:48
【Original Text】ruegos
【Annotations】requests
【Page Number】442
-------------------
Cuarta parte. Los comerciantes
Time：2021-08-18 07:10
【Original Text】—Si el intento de comerciar fuera deliberado, excelencia, sería lo más alocado y contrario a las más estrictas reglas de nuestro Gremio.
—Alocado
【Annotations】test

test

test
【Page Number】443
-------------------
"""


class TestBasic(TestCase):
    def test_parses_file(self):
        annotations = parser.get_annotations(StringIO(EXAMPLE_FILE))

        assert (
            annotations.name
            == "Trilogia de la Fundacion (Spanish Edition) - Isaac Asimov (146)"
        )
        assert annotations.author == "Isaac Asimov"
        assert len(annotations.annotations) == 2

        expected_annotations = [
            parser.Annotation(
                "Cuarta parte. Los comerciantes",
                datetime.datetime(2021, 8, 17, 22, 48),
                "ruegos",
                "requests",
                442,
            ),
            parser.Annotation(
                "Cuarta parte. Los comerciantes",
                datetime.datetime(2021, 8, 18, 7, 10),
                "—Si el intento de comerciar fuera deliberado, excelencia, sería lo más alocado y contrario a las más estrictas reglas de nuestro Gremio.\n—Alocado",
                "test\n\ntest\n\ntest",
                443,
            ),
        ]

        assert annotations.annotations == expected_annotations
