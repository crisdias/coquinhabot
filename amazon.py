# https://webservices.amazon.com/paapi5/documentation/assets/archives/paapi5-python-sdk-example.zip

# from amazon_paapi import AmazonApi
from dotenv       import load_dotenv
from utils        import pp

import re
import requests
import os
load_dotenv()

TAG     = os.environ['AMAZON_TAG']


# def amazon_search(search):
#   amazon = AmazonApi(KEY, SECRET, TAG, COUNTRY)

#   try:
#     busca = amazon.search_items(keywords=search, search_index='Books')
#   except Exception as e:
#     if str(type(e)) == "<class 'amazon_paapi.errors.exceptions.ItemsNotFound'>":
#       print('Items not found')
#       return 0
#     else:
#       print('Error: ' + str(e))
#       return 0

#   # dump item
#   dict = busca.to_dict()
#   return dict['items']


def get_asin_from_link(link):
    if '/dp/' in link:
        match = re.search(r"/dp/([A-Z0-9]{10})(?:[/?]|$)", link)
    elif '/ASIN/' in link:
        match = re.search(r"/ASIN/([A-Z0-9]{10})(?:[/?]|$)", link)
    else:
        return None
    
    if match:
        return match.group(1)
    else:
        return None


def extract_amazon_url(text):
  pattern = re.compile(r'https://amzn\.to/[a-zA-Z0-9]+')

  match = pattern.match(text)
  if match:
      text = extract_full_amazon_url( match.group() )


  amazon_url_pattern = re.compile(r'(http://|https://)?(www\.)?amazon\.com(\.br)?/[\w/\-\?\+.&%=]+')
  url = re.search(amazon_url_pattern, text)
  if url:
    return url.group()
  else:
    return 0


def add_affiliate_tag_to_product(asin):
  return f'https://www.amazon.com.br/dp/{asin}/?tag={TAG}'


def extract_full_amazon_url(short_url):
    response = requests.head(short_url, allow_redirects=True)
    return response.url


def amazon_tagger(url):
  import urllib.parse

  parsed = urllib.parse.urlparse(url)
  params = urllib.parse.parse_qsl(parsed.query)

  print('url: ')
  pp(url)
  print('\n')

  newparams = []
  has_tag = False

  for param in params:
    if param[0] == 'tag':
      param = ('tag', TAG)
      has_tag = True

    newparams.append(param)

  if not has_tag:
    newparams.append(('tag', TAG))

  # rebuild url
  newurl = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, urllib.parse.urlencode(newparams), parsed.fragment))
  print(f'newurl: {newurl}')

  return newurl



if __name__ == '__main__':
  # url = (extract_amazon_url("Esse livro aqui é muito legal! https://www.amazon.com.br/dp/8574066702/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_s=merchandised-search-3&pf_rd_r=D0C711EQ3CXVPNVAEAMF&pf_rd_t=101&pf_rd_p=94d88079-e94d-42b6-a704-f78cabb64d41&pf_rd_i=13420258011 Vocês não acham?"))
  # print(get_asin_from_link(url))

  # print(extract_amazon_url("aqui não tem nada"))

  print(extract_amazon_url("https://amzn.to/3Hioj6S"))

  # pp(amazon_tagger('https://www.amazon.com.br/dp/8574066702/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_s=merchandised-search-3&pf_rd_r=D0C711EQ3CXVPNVAEAMF&tag=XELELE&pf_rd_t=101&pf_rd_p=94d88079-e94d-42b6-a704-f78cabb64d41&pf_rd_i=13420258011'))

