# Put your app in here.
from flask import Flask, request
app = Flask(__name__)

from operations import add, sub, mult, div

@app.route("/add")
def addFunction():
    searchA = int(request.args.get('a'))
    searchB = int(request.args.get('b'))
    val = add(searchA, searchB)
    return str(val)

@app.route("/sub")
def subFunction():
    searchA = int(request.args.get('a'))
    searchB = int(request.args.get('b'))
    val = sub(searchA, searchB)
    return str(val)

@app.route("/mult")
def multFunction():
    searchA = int(request.args.get('a'))
    searchB = int(request.args.get('b'))
    val = mult(searchA, searchB)
    return str(val)

@app.route("/div")
def divFunction():
    searchA = int(request.args.get('a'))
    searchB = int(request.args.get('b'))
    val = div(searchA, searchB)
    return str(val)


dictOne = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
    }

@app.route("/math/<operators>")
def mathFuncs(operators):
    # searchA = int(request.args.get('searchA'))
    searchA = int(request.args.get('a'))
    # searchB = int(request.args.get('searchB'))
    searchB = int(request.args.get('b'))
    output = dictOne[operators](searchA, searchB)

    return str(output)