#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import lyrics


class TestLyricsMethods(unittest.TestCase):
    
    def test_is_not_none(self):
        self.assertIsNotNone(lyrics.get_lyrics(['meshuggah'], ['bleed']))

    def test_is_none(self):
        self.assertIsNone(lyrics.get_lyrics(['mes'], ['ble']))

    def test_wrong_args(self):
        self.assertEqual(lyrics.get_lyrics(['1'], ['2']), int)
        self.assertEqual(lyrics.get_lyrics(['meshugga'], ['1']), int)
        self.assertEqual(lyrics.get_lyrics(['1'], ['meshugga']), int)

if __name__ == '__main__':
    unittest.main()
