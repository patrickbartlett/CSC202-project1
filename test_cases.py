import unittest
import permute
import gummy_bears
import base_convert


class TestProject1(unittest.TestCase):

    def test_permute(self):
        self.assertEqual(
            permute.perm_gen_lex('abc'),
            ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        )
        self.assertEqual(
            permute.perm_gen_lex(''),
            []
        )
        self.assertEqual(
            permute.perm_gen_lex('a'),
            ['a']
        )
        self.assertEqual(
            permute.perm_gen_lex('ab'),
            ['ab', 'ba']
        )

    def test_bears(self):
        self.assertEqual(
            gummy_bears.bears(-1),
            False
        )
        self.assertEqual(
            gummy_bears.bears(0),
            False
        )
        self.assertEqual(
            gummy_bears.bears(1),
            False
        )
        self.assertEqual(
            gummy_bears.bears(41),
            False
        )
        self.assertEqual(
            gummy_bears.bears(42),
            True
        )
        self.assertEqual(
            gummy_bears.bears(-42),
            False
        )
        self.assertEqual(
            gummy_bears.bears(43),
            False
        )
        self.assertEqual(
            gummy_bears.bears(52),
            True
        )
        self.assertEqual(
            gummy_bears.bears(84),
            True
        )
        self.assertEqual(
            gummy_bears.bears(96),
            True
        )
        self.assertEqual(
            gummy_bears.bears(104),
            True
        )
        self.assertEqual(
            gummy_bears.bears(250),
            True
        )

    def test_base_convert(self):
        self.assertEqual(
            base_convert.convert(12, 2),
            '1100'
        )
        self.assertEqual(
            base_convert.convert(16, 2),
            '10000'
        )
        self.assertEqual(
            base_convert.convert(12, 3),
            '110'
        )
        self.assertEqual(
            base_convert.convert(16, 3),
            '121'
        )
        self.assertEqual(
            base_convert.convert(12, 4),
            '30'
        )
        self.assertEqual(
            base_convert.convert(16, 4),
            '100'
        )
        self.assertEqual(
            base_convert.convert(12, 5),
            '22'
        )
        self.assertEqual(
            base_convert.convert(16, 5),
            '31'
        )
        self.assertEqual(
            base_convert.convert(12, 6),
            '20'
        )
        self.assertEqual(
            base_convert.convert(16, 6),
            '24'
        )
        self.assertEqual(
            base_convert.convert(12, 7),
            '15'
        )
        self.assertEqual(
            base_convert.convert(16, 7),
            '22'
        )
        self.assertEqual(
            base_convert.convert(12, 8),
            '14'
        )
        self.assertEqual(
            base_convert.convert(16, 8),
            '20'
        )
        self.assertEqual(
            base_convert.convert(12, 9),
            '13'
        )
        self.assertEqual(
            base_convert.convert(16, 9),
            '17'
        )
        self.assertEqual(
            base_convert.convert(12, 10),
            '12'
        )
        self.assertEqual(
            base_convert.convert(16, 10),
            '16'
        )
        self.assertEqual(
            base_convert.convert(12, 11),
            '11'
        )
        self.assertEqual(
            base_convert.convert(16, 11),
            '15'
        )
        self.assertEqual(
            base_convert.convert(12, 12),
            '10'
        )
        self.assertEqual(
            base_convert.convert(16, 12),
            '14'
        )
        self.assertEqual(
            base_convert.convert(12, 13),
            'C'
        )
        self.assertEqual(
            base_convert.convert(16, 13),
            '13'
        )
        self.assertEqual(
            base_convert.convert(12, 14),
            'C'
        )
        self.assertEqual(
            base_convert.convert(16, 14),
            '12'
        )
        self.assertEqual(
            base_convert.convert(12, 15),
            'C'
        )
        self.assertEqual(
            base_convert.convert(16, 15),
            '11'
        )