import threading
import unittest
from concurrent.futures import ThreadPoolExecutor, wait

from src.cache.huku_cache import HukuInMemoryCache


class TestConcurrency(unittest.TestCase):
    def setUp(self):
        self.cache = HukuInMemoryCache()
        self.key = 'concurrent_key'
        self.value = 0
        self.cache.set(self.key, self.value)
        self.lock = threading.Lock()

    def add(self):
        with self.lock:
            current_value = self.cache.get(self.key)

            self.cache.set(self.key, current_value + 1)

    def test_concurrent_access_with_thread_pool(self):
        count_to = 1_000_00

        with ThreadPoolExecutor(max_workers=10) as executor:
            for i in range(count_to):
                task = executor.submit(self.add)

        self.assertEqual(count_to, self.cache.get(self.key))


if __name__ == '__main__':
    unittest.main()
