from flask import Flask 
app = Flask(__name__) # name is just the name of the module - can be == to main 

@app.route("/")
@app.route('/home')
def home():
	return "<h1>Home Page<h1>"
@app.route("/about")
def about():
	return "<h1>About Page<h1>"


if __name__ == '__main__':
	app.run(debug=True)


# https://www.youtube.com/watch?v=QnDWIZuWYW0