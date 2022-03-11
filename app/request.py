
import urllib.request,json

from.models import Quotes


def get_quotes():
    get_quotes_url='http://quotes.stormconsultancy.co.uk/random.json'
    # with urllib.request.urlopen(get_quotes_url)as url:
    get_quotes_data = urllib.request.urlopen(get_quotes_url)
    get_quotes_response = json.loads(get_quotes_data.read())
    new_quote = None
    if get_quotes_response:
       id= get_quotes_response.get('id')
       author = get_quotes_response.get('author')
       quote= get_quotes_response.get('quote')

    new_quote = Quotes(author,id,quote)

    return new_quote

