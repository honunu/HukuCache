from src.cache.huku_cache import HukuInMemoryCache

cache = HukuInMemoryCache()

cache.set('data1', 'book1')
cache.set('data2', b'book2')

print(cache.get('data1'))
print(cache.get('data2'))