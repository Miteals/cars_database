from flask import Flask, render_template, request
import requests


app = Flask(__name__)

url = "http://127.0.0.1:5001/"

log = []

def get_cars():
    log.append("[FRONTEND] Getting cars ")
    return requests.request("GET", url).json()

def add_brand(request):
    brand = request.form["brand"]
    model = request.form["model"]
    log.append(f"[FRONTEND] Adding brand {brand}, model {model}")
    payload={'brand': brand, 'model': model}
    response = requests.request("POST", url, data=payload)
    log.append(f"{response.text}")


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get("add_brand"):
            add_brand(request)

        if request.form.get("get_cars"):
            return render_template('index.html', log=log, brand=get_cars())

    return render_template('index.html', log=log)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port =5000)
