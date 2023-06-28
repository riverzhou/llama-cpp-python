#!/bin/env python3

import redis
import json
import os
from datetime import datetime

logDir  = '/var/log/llama.cpp'
logJsonName = 'llama.log'
logJsonFile = os.path.join(logDir, logJsonName)

if not os.path.exists(logDir):
    os.makedirs(logDir)

rediscon = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
print(rediscon)

with open(logJsonFile, 'a') as fJson:
    while True:
        logDataStr = rediscon.blpop('llama.cpp')[1].decode('utf8')
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logDict = {'time':ts, 'log':json.loads(logDataStr)}
        logJsonStr = json.dumps(logDict, indent=4, ensure_ascii=False)
        fJson.write(logJsonStr + '\n')
        fJson.write('='*50 + '\n')
        fJson.flush()

