"""
Server to facilitate microservice by accepting HTTP request containing
a JSON which defines a key item with a value of an ingredient to find scrape
a definition for.
"""

from flask import Flask, request
import json
from scraper import get_definition
from werkzeug.exceptions import HTTPException

# flask server
app = Flask(__name__)


# URL route
@app.route('/ingredientinfo', methods=['GET'])
def ingredient_info():
    # Get string required for scraper
    data = request.get_json()
    item = data['item']
    # Call imported function from scraper.py to retrieve relevant
    # definition from web
    scrape = get_definition(item)
    if scrape is None:
        return json.dumps({"item": item, "definition": "Item not found."})
    item, definition, url = str(scrape[0]), str(scrape[1]), str(scrape[2])
    # Return json containing formatted item name and definition of item
    return json.dumps(
        {"item": item, "definition": definition, "url": url}), 200


# 500 Error exception handling
@app.errorhandler(500)
def handle_exception(e):
    return {"500 Error": "Internal Service Error"}, 500

# 400 Error exception handling
@app.errorhandler(400)
def handle_exception(e):
    return {"400 Error": "Bad Request"}, 400


# Running on port 6000
if __name__ == "__main__":
    app.run(port=6000)
