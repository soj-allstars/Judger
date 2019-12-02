from rq import Queue
import json
from redis import Redis
import time

q = Queue(connection = Redis("47.106.140.231", "6379"))
test_dict = dict()
fo = open("testjson.json", "r")
test_dict = json.load(fo)                             
result = q.enqueue("queue_dealer.deal_submitted", **test_dict)

print("submit-----")
time.sleep(1)
print(result.result)

pass