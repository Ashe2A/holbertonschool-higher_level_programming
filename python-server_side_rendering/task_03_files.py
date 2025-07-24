#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/items")
def items():
    try:
        with open("items.json", "r") as f:
            data = json.load(f)
            items = data["items"]
    except Exception as e:
        print(str(e))
        items = []

    return render_template("items.html", items=items)


@app.route("/products")
def product_display():
    source = request.args["source"]
    id = request.args.get("id", None)

    try:
        if source == "json":
            with open("products.json", "r") as f:
                products = json.load(f)
        elif source == "csv":
            with open("products.csv") as f:
                products = list(csv.DictReader(f))
        else:
            return render_template("product_display.html",
                                   error="Wrong source"), 200

        if not id:
            product_display = products
        else:
            product_display = []
            for i in products:
                if "id" in i and str(i["id"]) == id:
                    product_display.append(i)

            if product_display == []:
                return render_template("product_display.html",
                                       error="Product not found."), 200

        return render_template("product_display.html",
                               products=product_display), 200

    except Exception as e:
        return render_template("product_display.html",
                               error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
