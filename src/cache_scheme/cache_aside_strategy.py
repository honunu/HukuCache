import time

from src.cache.huku_cache import HukuInMemoryCache
from src.cache_scheme.user_repository import get_user_by_id_db, update_user_by_id_db

cache = HukuInMemoryCache()


def cache_preheat():
    user_ids = [1, 2, 3]
    for user_id in user_ids:
        user = get_user_by_id_db(user_id)
        cache.set(user_id, user)


def get_user_by_id(user_id: int):
    """
    cache aside read
    """
    start_time = time.time()
    user = cache.get(user_id)
    consume_time = time.time() - start_time
    print(f'cache get {consume_time}s')

    if user:
        print(f'cache hit for {user_id}')
        return user
    else:
        print(f'cache miss for {user_id}')

        start_time = time.time()
        user = get_user_by_id_db(user_id)
        consume_time = time.time() - start_time
        print(f'database get {consume_time}s')

        cache.set(user_id, user)
        return user


def update_user_by_id(user_id: int, user):
    """
    cache aside, update database and then remove cache
    """
    update_user_by_id_db(user_id, user)
    cache.delete(user_id)



