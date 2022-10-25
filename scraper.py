"""
Web scraper which takes a string of an ingredient and returns a relevant
HTML element from whatscookingamerica.net which contains a definition and url
(if applicable) of the passed item.
"""

import mechanicalsoup

link = "https://whatscookingamerica.net/glossary/"


# Takes a string and returns definition from whatscookingamerica.net if valid
def get_definition(item):
    # Create a browser object
    b = mechanicalsoup.StatefulBrowser()
    b.set_user_agent('recipe-service')
    # Retrieve HTML document
    data_page = b.get(link).soup
    # Locate the strong element within the HTML document that contains
    # the item name.
    scraped_data = data_page.find((lambda
                                       tag: tag.name == "strong" and
                                            item.lower() in tag.text.lower()))

    # Ignore false matches from non-ingredient name elements
    if scraped_data:
        if 'itemprop="name"' in str(scraped_data):
            item = scraped_data.contents[0].text
            p_item = scraped_data.find_next('p').contents
            # Select items have no definition, only history
            if str(p_item[0].text) == "History:":
               p_item = scraped_data.find_next('p').find_next('p').contents
            definition = p_item[0].text
            url = "No url"
            # Check if a URL is present in the matched <p> element
            if len(p_item) > 1:
                url = p_item[1]
            # Return list of item, definition, and url
            return [item.lower().capitalize(), definition, url]
    else:
        return None
