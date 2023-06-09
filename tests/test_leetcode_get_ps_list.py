import unittest

from psdelivery import PsDelivery

class TestLeetcodeGetPsList(unittest.TestCase):
    crawler = PsDelivery('leetcode')

    def test_page_index_is_minus(self):
        with self.assertRaises(ValueError):
            self.crawler.get_list_by_single_page(-1)

    def test_page_index_is_too_large(self):
        res = self.crawler.get_list_by_single_page(999999)
        self.assertEqual(0, len(res))

    def test_page_index_is_str(self):
        with self.assertRaises(ValueError):
            self.crawler.get_list_by_single_page('hello world')

    def test_success_with_serialize(self):
        res = self.crawler.get_list_by_single_page(2, True)
        self.assertEqual(50, len(res))
