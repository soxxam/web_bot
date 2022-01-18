from flask import Flask, render_template

app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/bot/<string:name>/', methods=['GET', 'POST'])
def bot_view(name):
    print(name)
    return render_template('bot.html')

 
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)