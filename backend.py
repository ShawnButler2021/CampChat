from flask import Flask, render_template, request

web_app = Flask(__name__)


@web_app.route("/")
def index():
  return render_template('index.html')



web_app.run(debug=True)