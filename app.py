from flask import Flask, jsonify, request, render_template
from database import get_all_items, add_item, delete_item

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(get_all_items())

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    if not data or "name" not in data:
        return {"error": "Invalid input"}, 400

    add_item(data["name"])
    return {"message": "Item added"}, 201

@app.route("/items/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):
    delete_item(item_id)
    return {"message": "Item deleted"}, 200

if __name__ == "__main__":
    app.run(debug=True)
