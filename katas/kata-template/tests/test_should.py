from unittest import TestCase

from assertpy import assert_that



class FooShould(TestCase):
    def test__foo(
        self,
    ):
        assert_that(True).is_false()
