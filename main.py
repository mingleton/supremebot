from supreme import Supreme
import datetime

def main(category, name, color, size, checkoutDelay, url):
    if releaseType == 'R':
        supreme = Supreme(category, name, color, size, checkoutDelay)
        supreme.addToCart(supreme.restock(url))
        supreme.checkOut()
    else:
        supreme = Supreme(category, name, color, size, checkoutDelay)
        supreme.addToCart(supreme.search())
        supreme.checkOut()

if __name__ == '__main__':
    # enter R for restock mode else leave blank
    releaseType = ''.upper()
    # enter category for release mode lese leave blank
    category = 'jackets'
    # enter name for release mode else leave blank
    name = 'parka'
    # enter color for release mode else leave blank
    color = 'rose'
    # enter size for desired size else leave blank for O/S or random
    size = ''
    # Enter checkout delay to avoit ghost checkout or else enter None
    checkoutDelay = None
    
    # this will be promt if restock mode is selected else ignore this
    url = input('Enter url: ').strip() if releaseType =='R' else None
    
    # don't change anything here
    print(datetime.datetime.now().strftime('%x %X'), 'Starting the script')
    main(category, name, color, size, checkoutDelay, url)
