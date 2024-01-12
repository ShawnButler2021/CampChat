from flask import Flask, render_template, request, redirect

web_app = Flask(__name__)


@web_app.route("/", methods=["POST", "GET"])
def index():
  if request.method == "GET":
    return render_template('index.html')

  else:
    if request.form["ip-address"] != None:
      return redirect(for_url("room.html"))
    return redirect(for_url("create_room.html"))


@web_app.route("/create_room")
def create_room():
  return render_template('create_room.html')

@web_app.route("/room")
def room():
  return render_template('room.html')





web_app.run(debug=True)