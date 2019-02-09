#Getting and posting json
import requests
#test schedule post
# res = requests.post('http://localhost:5000/api/add_schedule/1', json={"times":"[(0, 1), (2, 10)]", "amounts": "[3, 2]"})
# if res.ok:
#     print res.json()

#test data post
import json
import datetime

class DateTimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return super(DateTimeJSONEncoder, self).default(obj)

import math
for i in range(10):
    res = requests.post('http://localhost:5000/api/add_data/0/0', json={"timestamp":DateTimeJSONEncoder().encode([datetime.datetime.now()]), "weight": math.sin(i/3)})
    if res.ok:
        print res.json()


for i in range(10):
    res = requests.post('http://localhost:5000/api/add_data/0/1', json={"timestamp":DateTimeJSONEncoder().encode([datetime.datetime.now()]), "ftime": i, "amt": i/2.0})
    if res.ok:
        print res.json()

for i in range(10):
    res = requests.post('http://localhost:5000/api/add_data/0/2', json={"timestamp":DateTimeJSONEncoder().encode([datetime.datetime.now()]), "amt": i/2.0})
    if res.ok:
        print res.json()