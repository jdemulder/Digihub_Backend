from flask_cors import CORS
from flask import Flask

from src.mds import mds_analysis

app = Flask(__name__)
CORS(app)

@app.route('/')
def connect():
    return '{"message": "Connection succeeded."}'

@app.route('/runMdsAnalysis')
def runMds():
    mds_analysis('./data/Golden Standard Digihub.csv', 'Golden Standard Digihub')
    return '{"message": "Finished MDS Analysis."}'

if __name__ == '__main__':
    app.run()
