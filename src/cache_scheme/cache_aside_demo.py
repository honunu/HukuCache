from concurrent.futures import ThreadPoolExecutor

from src.cache_scheme.cache_aside_strategy import get_user_by_id, update_user_by_id
from src.cache_scheme.user_repository import update_user_by_id_db

# Initialize user
update_user_by_id_db(1, user={'ID': 1, 'Age': 25})
print(get_user_by_id(1))

user_id = 1
user = {'ID': user_id, 'Age': 30}

result_list = []
read_repeat_time = 1000
with ThreadPoolExecutor(max_workers=10) as executor:
    future_update = executor.submit(update_user_by_id, user_id, user)

    for i in range(read_repeat_time):
        future = executor.submit(get_user_by_id, user_id)
        result = future.result()
        result_list.append(result)

    update_result = future_update.result()

age_list = [result['Age'] for result in result_list]


print(f"{read_repeat_time} reads {age_list.count(25)} times get 25, {age_list.count(30)} times get 30 ")
