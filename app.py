from flask import Flask
from Housing.logger import logging
from Housing.exception import HousingException
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try: 
        raise Exception("we are testing custom exception")
    except Exception as e:
         Housing = HousingException(e,sys)
         
         logging.info("we are testing logging module")
    logging.info("we are testing module")
    return "CI CD pipeline has been established. "

if __name__ =="__main__":
    app.run(debug=True)
    
#from flask import Flask
#import numpy as np 
#import pandas as pd 

#app = Flask(__name__)

#@app.route('/',methods=['GET'])
#def home():
    #return "Hello World"

#if __name__=="__main__":
    #app.run(host='0.0.0.0',port=5000,debug=True) 