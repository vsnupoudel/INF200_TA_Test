# -*- coding: utf-8 -*-

import pytest

class TestAnimal:

    def test_syntax(self):
        with pytest.raises(ZeroDivisionError):
            _ = 12 / 0

    def test_print_animal(self):
        assert 1 == 2
