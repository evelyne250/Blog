
import urllib.request,json
from .models import Quotes



# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url

    base_url = app.config['QUOTES_API']






def get_Quotes():
    '''
    Function that gets the json responce to our url request
    '''
    any_quote = requests.get(Quotes_api)
    new_quote = random_quote.json()
    id = new_quote.get("id")
    author = new_quote.get("author")
    quote = new_quote.get("quote")
    permalink = new_quote.get("permalink")
    quote_item = Quotes(id,author,quote,permalink)
  return quote_item   
  