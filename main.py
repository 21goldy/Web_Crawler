import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


def response(url):
    try:
        return requests.get(url, headers=header)

    except requests.exceptions.ConnectionError:
        pass


# getting the subdomains
# with open('subdomains_list.txt', 'r') as subdomain_list:
#     try:
#         for line in subdomain_list:
#             test_url = line.strip() + '.' + target_url
#             got_response = response(test_url)
#             if got_response:
#                 print("[+] Discovered Subdomains ->" + ' ' + test_url)
#     except requests.exceptions.InvalidURL:
#         pass


# getting the directories
# with open('dirs_list.txt', 'r') as dirs_list:
#     try:
#         for line in dirs_list:
#             test_url = target_url + '/' + line.strip()
#             got_response = response(test_url)
#             if got_response:
#                 print("[+] Discovered directory urls ->" + ' ' + test_url)
#     except requests.exceptions.InvalidURL:
#         pass

# target_url = 'https://vitbhopal.ac.in/'
target_url = 'https://zsecurity.org/'
# target_url = 'https://www.wikipedia.org/'
extracted_links = []


# def crawl(target):
#     result = response(target)
#     content = result.text
#     soup = BeautifulSoup(content, 'html.parser')
#     # print(soup.prettify())
#
#     links = soup.find_all('a')
#     for link in list(set(links)):
#         href = link['href']
#         # print(urljoin(target, href))
#         extracted_links.append(urljoin(target, href))
#         # crawl(urljoin(target, href))
#
#
# crawl(target_url)
# print(len(extracted_links), extracted_links)

result = response(target_url)
content = result.text
soup = BeautifulSoup(content, 'html.parser')

WEB_FORMS = soup.find_all("form")
# print(WEB_FORMS)

names_of_input = []
for form in WEB_FORMS:
    action = form.get('action')
    method = form.get('method')
    # print(action)
    # print(method)

    inputs = form.findAllNext('input')
    for input_name in inputs:
        names_of_input.append(input_name.get('name'))

print(names_of_input)

# r = requests.get('https://vitbhopal.ac.in/')
# print(r.request.headers)
