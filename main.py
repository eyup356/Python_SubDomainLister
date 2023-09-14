import requests
from requests.exceptions import ConnectionError, Timeout

target_input = input("Enter your target domain: ")

wordlist_url = "https://raw.githubusercontent.com/danTaler/WordLists/master/Subdomain.txt"
response = requests.get(wordlist_url)

if response.status_code != 200:
    print(f"Wordlist error ({response.status_code})")
    exit()

wordlist = response.text.split("\n")

for word in wordlist:
    word = word.strip()
    url = "http://" + word + "." + target_input
    try:
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            print(f"Subdomain found: {url}")
        elif response.status_code == 404:
            print(f"Not Found: {url}")
        else:
            print(f"Other Response Code ({response.status_code}): {url}")
    except (ConnectionError, Timeout) as e:
        print(f"Connection Error or Timeout: {url} ({e})")
        continue
