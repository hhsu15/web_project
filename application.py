from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route("/extention", methods=['GET', 'POST'])
def extention():
	return render_template("base_ext.html")

@app.route("/profile", methods=['GET', 'POST'])
def profile():
	return render_template("profile.html")

@app.route("/example", methods=['GET', 'POST'])
def example():
	return render_template("example.html")

@app.route("/profile/<username>")
def username(username):
	return 'hey there, {}'.format(username)

if __name__  == '__main__':
	app.run(debug=True)