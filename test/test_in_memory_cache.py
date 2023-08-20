import unittest

from src.cache.huku_cache import HukuInMemoryCache


class InMemoryCacheTest(unittest.TestCase):
    def setUp(self):
        self.cache = HukuInMemoryCache()

    def test_set_and_get(self):
        self.cache.set('key1', 'value1')
        self.assertEqual(self.cache.get('key1'), 'value1')

    def test_delete(self):
        self.cache.set('key3', 'value3')
        self.cache.delete('key3')
        self.assertIsNone(self.cache.get('key3'))

    def test_clear(self):
        self.cache.set('key4', 'value4')
        self.cache.set('key5', 'value5')
        self.cache.clear()
        self.assertIsNone(self.cache.get('key4'))
        self.assertIsNone(self.cache.get('key5'))