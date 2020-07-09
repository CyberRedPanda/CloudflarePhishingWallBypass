###################

# Clearnet version (see other script for tor version)
# This code allows you to programatically download files from websites which Cloudflare has blocked with a "This page has been flagged with phishing" wall.
# Change the "link" and "link_to_get" variables in the "start_download function to the homepage and download links on a site which cloudflare has tagged with "phishing"
# Prepend the homepage URL to the new_url variable

####################


# Instantiate scraper and check to make sure safety protocols are active

import json
import cloudscraper
import sys
from bs4 import BeautifulSoup

# Initiate Scraper instance through tor with masked headers
class Instantiate_scraper:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper(interpreter='nodejs')
        self.headers = {}
        self.headers['User-agent'] = "Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0"

def start_download():
    link = 'PUT HOMEPAGE URL HERE'
    link_to_get = 'PUT FULL FILE URL HERE'
    scraper = Instantiate_scraper()
    scraper = scraper.scraper
    response = scraper.get(link, stream=True, headers=scraper.headers)
    soup = BeautifulSoup(response.text)
    atok = soup.find('input', {'name': 'atok'}).get('value')
    u = soup.find('input', {'name': 'u'}).get('value')
    # print(atok)
    # print(u)
    new_url = 'PREPEND_HOMEPAGE_URL/cdn-cgi/phish-bypass?u={u}&atok={atok}'.format(u=u, atok=atok)
    response_2 = scraper.get(new_url, headers=scraper.headers, allow_redirects=True)
    # print(response_2.text)
    file_name = "file_download"
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = scraper.get(link_to_get, stream=True, headers=scraper.headers, allow_redirects=True)
        total_length = response.headers.get('content-length')
        # show status bar
        if total_length is None: 
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                sys.stdout.flush()


# Execute script
scraper = Instantiate_scraper()
print("Beginning file download, please wait, this may take a while.")
print("Your file name will be \"file_download\"")
start_download()
print("Download is complete")
start_download()
