// Recipe Microservice
// Example client for requesting definition via server.py
var request = require('request-promise')

async function ingredient_request(ingredient) {
	// Convert item to JSON
	item = {'item': ingredient}

	// Set parameters to include above item and send request to port 6000.
	var options = {
		method: 'GET',
		uri: 'http://127.0.0.1:6000/',
		body: item,
		json: true
	};

	var sendrequest = request(options)

		// Return result to console
		.then(function (parsedBody) {
			result = parsedBody;
			console.log(result)
			return result;
		})
		.catch(function (err) {
			console.log(null)
		});
}

// Sample call of function
ingredient_request('boudin noir');
