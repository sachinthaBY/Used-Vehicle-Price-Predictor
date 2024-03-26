from flask_cors import CORS
from flask import Flask
import pickle

app = Flask(__name__)
CORS(app)
model = pickle.load(open('/Users/thashinrahuman/Desktop/Vehicle Price Predictor/VPP/Web/model.pkl', 'rb'))


@app.route('/')
def home():
    return 'Welcome to Used Vehicle Price Predictor'


@app.route('/<value_one>,<value_two>,<value_three>,<value_four>,<value_five>,<value_six>,<value_seven>')
def predict(value_one, value_two, value_three, value_four, value_five, value_six, value_seven):

    prediction = model.predict([[value_one, value_two, value_three, value_four, value_five, value_six, value_seven]])
    output = int(prediction)

    return str(output)


if __name__ == "__main__":
    app.run(debug=True)
