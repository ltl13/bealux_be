import pytest

from tests import PytestBase


class TestExampleClass(PytestBase):
    @pytest.fixture(autouse=True)
    def _setup(self):
        super()._setup()

    def test_a(self):
        assert True