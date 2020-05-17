from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


#function to get html data from url
def get_url():

    # URL to be scraped
    URL = 'https://news.google.com'

    try:
        # open url to be scraped
        open_url = urlopen(URL)

    except HTTPError as e:
        #Print error if url is not opened
        print(e)
        # log error to file
        error = open('error_file.txt', 'a')
        error.write("\n"+ str(e))
        error.close()

    else:
       return open_url

## function to parse html data
def parse_data():

    open_url = get_url()

    ##parse data using beautifulsoup
    parser = 'html.parser'
    soup= BeautifulSoup(open_url, parser)

    text = ''
    for tag in soup.find_all("a"):
        text += '\n' + tag.text

    print(text)

parse_data()

