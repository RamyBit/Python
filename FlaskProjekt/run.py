from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def start():
    fruits = ["Apfel", "Birne", "Banana"]
    return render_template("start.html", page_title="Fruit",fruits=fruits)
@app.route("/hello")
def hello():
    return "Hello World"
@app.route("/test")
def testPrint():
    paragraph = "<p> dieser ist ein <strong>HTML</strong> Paragraf</p>"
    return "Hello Test Debug" + paragraph
@app.route("/fruit_list")
def list_of_fruit():
    fruits = ["Apfel", "Birne", "Banana"]
    output = ""
    for fruit in fruits:
        output += "<h3>" + fruit + "</h3>"

    return output

@app.route("/about")
def about():
    return render_template("about.html", page_title="about",name ="Max Mustermann")
@app.route("/test_name")
def test_name():
    print(request)
    args= request.args
    print(args)
    name = args.get("name")
    age= args.get("age")
    return  render_template("test_name.html",name=name, age=age)
@app.route("/shoping")
def shoping():
    person = ("Max","Mustermann")
    price_list = [
        {"name" : "Festplatte","price": 50},
        {"name": "prozerssor", "price": 150},
        {"name": "Grafikkarte", "price": 12200},
        {"name": "Mainboard", "price": 50},
    ]
    items_list = [
        {"name": "Festplatte", "amount": 5},
        {"name": "prozerssor", "amount": 3},
        {"name": "Grafikkarte", "amount": 500},
        {"name": "Mainboard", "amount": 10},
    ]

    return render_template("shoping.html",person=person, items = items_list)