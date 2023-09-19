from flask import Flask, request

app = Flask(__name__)

database = {"Mominur": "100"}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to my cute API"


@app.route("/getdata", methods=["GET", "PUT"])
def get_data():
    key, value = list(request.args.items())[0]
    if value not in database:
        return "Value does not exist"
    item = database[value]
    return f"ID of {value} is {item}"


@app.route("/add_data", methods=["GET", "PUT"])
def add_data():
    key, value = list(request.args.items())[0]
    database[key] = value
    return f"{key} added"


@app.route("/deletedata", methods=["GET", "DELETE"])
def delete_data():
    key, value = list(request.args.items())[0]
    database.pop(value)
    return f"{value} deleted"


if __name__ == "__main__":
    app.run()
