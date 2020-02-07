import requests
import time
import json
# Unityで起動したサーバから座標データをJsonとして送ってもらう
url = 'http://localhost:8080/'
msg = ''

while True:
    response = requests.get(url)
    msg = response.text.strip()
    try:
        data = json.loads(msg)
        print('x=%f y=%f z=%f' % (data["x"], data["y"], data["z"]))
        time.sleep(1)
    except:
        print(msg)
        break