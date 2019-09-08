from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Group


class HeartModelsTests(TestCase):
    def test_group_subgroups_getter(self):
        '''Group model subgroups range generator works properly'''

        group = Group(name='G1', year=1)

        for i in range(1, 4):
            group.subgroups = i
            self.assertEqual(group.subgroups_range(), range(1, i + 1))
