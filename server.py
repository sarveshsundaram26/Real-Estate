import util
from flask import Flask,request,jsonify
app=Flask(__name__)
util.load_artifacts()
@app.route("/load_artifacts")
def load_artifacts():
    util.load_artifacts()
@app.route('/get_location_names')
def get_location_names():
    print('get location running')
    response=jsonify(
        {
            'locations':util.get_location_names()
        }          )
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
        print("predict home price is running")
        total_sqft=request.form['total_sqft']
        location=request.form['location']
        bhk=request.form['bhk']
        bath=request.form['bath']

        response=jsonify(
            {
                'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
            }
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
if __name__=='__main__':
    print('Starting python flask server')
    app.run()