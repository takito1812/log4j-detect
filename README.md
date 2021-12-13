<h1 align="center">
  <br>
  log4j-detect
</h1>

<h4 align="center">Simple Python 3 script to detect the "Log4j" Java library vulnerability (CVE-2021-44228) for a list of URL with multithreading</h4>

---

The script "log4j-detect.py" developed in Python 3 is responsible for detecting whether a list of URLs are vulnerable to CVE-2021-44228.

To do so, it sends a GET request using threads (higher performance) to each of the URLs in the specified list. The GET request contains a payload that on success returns a DNS request to Burp Collaborator / interactsh. This payload is sent in a test parameter and in the "User-Agent" / "Referer" / "X-Forwarded-For" / "Authentication" headers.
Finally, if a host is vulnerable, an identification number will appear in the subdomain prefix of the Burp Collaborator / interactsh payload and in the output of the script, allowing to know which host has responded via DNS.

It should be noted that this script only handles DNS detection of the vulnerability and does not test remote command execution.

### Downloading log4j-detect.py

```sh
wget https://github.com/takito1812/log4j-detect/raw/main/log4j-detect.py
```

### Running log4j-detect.py

```sh
python3 log4j-detect.py <urlFile> <collaboratorPayload>
```

![imagen](https://user-images.githubusercontent.com/56491288/145856295-f85b06da-17f2-4aa7-85fb-e0b75d6e1965.png)
