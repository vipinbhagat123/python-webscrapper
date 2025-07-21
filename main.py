import requests

def fetchAndSaveToFIle(url, path):
    r=requests.get(url)
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)


url ="https://timesofindia.indiatimes.com/india/vice-president-jagdeep-dhankhar-resigns-from-his-post-citing-health/articleshow/122819108.cms"
fetchAndSaveToFIle(url, 'date/times.html')