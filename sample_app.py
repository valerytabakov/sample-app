from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route('/')
def main():
    # return "You are calling me from " + request.remote_addr + "\n"
    # return render_template("index.html")
     return 'Hello World from Flask Web Server!***'

if __name__=="__main__":
    sample.run(host='0.0.0.0', port=8080)

