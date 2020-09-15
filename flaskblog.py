from flask import Flask 
app = Flask(__name__) # name is just the name of the module - can be == to main 

@app.route("/")
def hello():
	return "hello world"