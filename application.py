from flask import Flask, render_template, url_for,request, jsonify
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route("/extention", methods=['GET', 'POST'])
def extention():
	return render_template("base_ext.html")

@app.route("/hello", methods=['POST'])
def hello():
	name = request.form.get("name")
	return render_template("index.html", name=name)

notes = []
@app.route("/profile", methods=['GET', 'POST'])
def profile():
	return render_template("profile.html")

notes = []
@app.route("/example", methods=['GET', 'POST'])
def example():
	headline = 'Hello this is the headline2!'
	intro = 'This is my introduction'
	if request.method == 'POST':
		note = request.form.get('note')
		notes.append(note)
		return render_template("example.html", notes=notes, headline2=headline, intro=intro)
	return render_template("example.html", headline2=headline, intro=intro)

@app.route("/bye", methods=['GET', 'POST'])
def bye():
	headline = 'Goodbye!'
	intro  = "I am saying goodbye"
	return render_template("example.html", headline2=headline, intro=intro)

@app.route("/check_user/<the_name>", methods=['GET', 'POST'])
def check_user(the_name):
	my_name = the_name
	return render_template("example.html", my_name=my_name)

@app.route("/base", methods=['GET', 'POST'])
def base():
	return render_template("base.html")	

@app.route("/profile/<username>",methods=['GET', 'POST'])
def username(username):
	return 'hey there, {} - this is my profile'.format(username)

@app.route("/welcome",methods=['GET', 'POST'])
def welcome():
	name = request.form.get("name")
	return render_template("welcome.html", name=name)

@app.route("/ajax",methods=['GET', 'POST'])
def ajax():
	return render_template("ajax.html")

@app.route("/convert",methods=['GET','POST'])
def convert():
	
    currency = request.form.get('currency').upper()
    res = requests.get("http://api.fixer.io/latest",params={'base':'USD','symbols':currency}) 
    data = res.json()

    return jsonify({'success':True,'rate':data['rates'][currency]})
    # if res.status_code != 200:
    # 	return jsonify({'success':False})
    # if currency not in data['rates']:
    # 	return jsonify({'success':False})
	
	# return jsonify({'success':True,'rate':data['rates'][currency]})

@app.route("/api/data",methods=['GET', 'POST'])
def api():
	data = {'data':'this is my api'}
	return jsonify(data)

@app.route("/api/double/<int:num>",methods=['GET', 'POST'])
def api_double(num):
	data = {'data': num * 2}
	return jsonify(data)

@app.route("/chatroom",methods=['GET', 'POST'])
def chatroom():
	return render_template("chatroom.html")

@socketio.on("submit vote")
def vote(data):
	selection = data['selection']

	emit("announce vote", {"selection":selection},broadcast=True)


if __name__ == '__main__':
    socketio.run(app)

# if __name__  == '__main__':
# 	app.run(debug=True)