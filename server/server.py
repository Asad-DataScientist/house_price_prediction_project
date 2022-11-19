# Importing Flask server
# Configured default interpreter as Anaconda
from flask import Flask, request, jsonify
import util
from flask import Flask, request, jsonify
# Created an app using this line
app = Flask(__name__)

# util contains all the routine, whereas this server file just contains the routing of reqeust and response
# First routine to get location names, it will return all the locations
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-control-Allow-origin', '*')

    # returning a response that contains all the locations through util.py
    return response

# end point 'predict_home_price' that takes post method
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath) # here calling util.estimated_price function passing the
    })                                                                            # input parameters that will return estimated price back

    response.headers.add('Access-Control-Allow-Origin','*')

    return response

# in main function running app.run, it will run the application on a specific port.
if __name__ == '__main__':
    print ('Starting Flask')
    util.load_saved_artifacts()
    app.run()