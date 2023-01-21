from flask import Flask, jsonify, request

app = Flask(__name__)

database = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']

        database.append({"brand": brand, "model": model, })

        return f"brand: {brand}, model: {model} has been added to database"

        #return do_the_login()
    else:
        return jsonify(database)

app.run(host="0.0.0.0", port=5001)
