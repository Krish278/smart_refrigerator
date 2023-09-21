from datetime import date, datetime, timedelta

from flask import Flask, redirect, render_template, request, session, url_for
from flask_mail import Mail, Message

from database import *

app = Flask(__name__)

app.secret_key = "Mandyammu"  # Make sure to set a secret key

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # Port for TLS
app.config['MAIL_USERNAME'] = 'smartfridge12@gmail.com'
app.config['MAIL_PASSWORD'] = 'woqs cmue akni jsgs'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Default recipient's email address
default_recipient = '20r11a0579@gcet.edu.in'
default_message = 'this item is expired...!!'


@app.route("/")
def sf():
  return render_template("home1.html")


@app.route('/login', methods=['POST'])
def login():
  if request.method == "POST":
    username = request.form.get('username')
    password = request.form.get('password')
    user, pass1 = validate(username)
    if username == user and password == pass1:
      return render_template("home.html")
    return render_template("login.html", error="Invalid username or password")


@app.route('/home')
def home():
  return render_template("home.html")


@app.route('/signup')
def signup():
  return render_template("signup.html")


@app.route("/signup1", methods=["POST"])
def signup1():
  username = request.form.get("username")
  password = request.form.get("password")
  #confirm_password = request.form.get("confirm_password")
  email = request.form.get("email")

  # Basic validation
  if not username or not password:
    return "Username and password are required fields."

  #if password != confirm_password:
  # return "Passwords do not match."

  if search(username) == username:
    print(123)
    return "Username is already taken. Please choose another."
  print(123)
  insert(username, email, password)

  # Redirect to a success page or login page
  #return redirect(url_for("home"))

  return redirect(url_for("home"))


@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/about1")
def about1():
  return render_template("about1.html")


@app.route("/explore")
def explore():
  return render_template("explore.html")


@app.route("/add")
def add():
  return render_template("add.html")


@app.route("/delete")
def delete():
  return render_template("delete.html")


@app.route("/contents")
def contents():
  return render_template("contents.html")


@app.route("/contents", methods=['POST'])
def add_contents():
  data, col = view()
  return render_template("contents.html", data=data, col=col)


@app.route('/del', methods=['POST'])
def dele():
  return ""


@app.route("/login1")
def login1():
  return render_template("login.html")


@app.route("/contents_1", methods=['POST'])
def add_contents_1():
  data, col = view()
  session['contents'] = data
  return render_template("delete.html", data=data, col=col)


@app.route("/remove", methods=['POST'])
def remove_1():
  items = session['contents']
  #print(type(items))
  #print(items)
  item = request.form.get("item")
  #print(item)
  #print(type(item))
  l = []
  for i in items:
    l.append(i[1])
  print(l)
  if item in l:
    remove1(item)
    return render_template("delete.html", k="Item deleted")
  return render_template("delete.html", k="Enter a valid item")


@app.route('/additems', methods=['POST', "GET"])
def additems():
  item_name = request.form.get('item-name')
  quantity = int(request.form.get('quant'))
  date = str(date.today())
  print(date)
  day = str(datetime.today() - timedelta(days=7))
  session["day1"] = day[0:10]
  add_db(item_name, quantity, date, day)
  return render_template('add.html', k="Item added")


@app.route('/mail', methods=["POST", "GET"])
def send_default_email():
  if date.today() == date(2023, 9, 22):  # Use date() to create a date object
    try:
      msg = Message(
          'mail@gmail.com',
          sender='smartfridge12@gmail.com',  # Your email address
          recipients="default_recipient")
      msg.body = default_message

      # Assuming 'mail' is your Flask-Mail instance
      mail.send(msg)

      print('Default email sent successfully!')
    except Exception as e:
      print(f'Error sending default email: {str(e)}')

  return render_template("contents.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
