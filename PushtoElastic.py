

import json

import requests
import os
from requests.auth import HTTPBasicAuth
import pandas as pd
from datetime import datetime

columns = ['TimeNow', 'Class', 'Count']
index = [0]
timenow = timenow = datetime.utcnow()
df_ = pd.DataFrame(index=index, columns=columns)
df_.loc[0, 'TimeNow'] = timenow
df_.loc[0, 'Class'] = 1
df_.loc[0, 'Count'] = 0


jn = df_.to_json(orient='records', lines=True)

jn1 = json.loads(jn)


print(jn)

# url = 'https://elasticsearch.redrange1.devwerx.org:51443/persondetect/_doc'
# username = 'elastic'
# password = 'ohnohch2aZ'
# headers = {'Content-Type': 'application/json', 'X-HTTP-Method-Overide': 'PUT', 'Accept-Charset': 'UTF-8'}
# r = requests.post(url, data=json.dumps(jn1), headers=headers, auth=HTTPBasicAuth(username, password))


