#from crypt import methods
from flask import Flask
from housing.logger import logging

app=Flask(__name__)

@app.route("/",methods = ['POST','GET'])
def index():
    logging.info("we are testing logging module in logger file !")
    return "Hello world"


if __name__=="__main__":
    app.run(debug= True)