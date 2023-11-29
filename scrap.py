import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '__RequestVerificationToken_L1NjYW5uaW5n0=M6ogNkhXXOXXCCyJCqP73hqiaIh_sx695jIkUO8kKHX5CAji9BJhRxSqAM-Q3sjVLpo6wAX0fALjnWO6RGOn8YKJW7JkXpDynH50oiiSRKE1',
    'Origin': 'http://scan.smsitgroup.com',
    'Referer': 'http://scan.smsitgroup.com/scanning',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

Data = {
    '__RequestVerificationToken': '',
    'Email': 'shivam@scan-logic.com',
    'Password': 'service12',
}

with requests.session() as s:
    login_url = 'http://scan.smsitgroup.com/scanning'
    r= s.get(login_url)
    soup = BeautifulSoup(r.text,'html.parser')
    request_token = soup.find('input', {'name':"__RequestVerificationToken"})['value']
    Data['__RequestVerificationToken']= request_token
    s.post(login_url,data=Data, headers=headers)
    
    r = s.get("http://scan.smsitgroup.com/Scanning/User/Home")

    print(r.text)