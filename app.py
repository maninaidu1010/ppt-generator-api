from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "PPT Generator API Running"

@app.route("/createppt", methods=["POST"])
def create_ppt():

    data = request.json

    title = data.get("title", "Default PPT")

    return jsonify({
        "status": "success",
        "message": f"PPT request received for {title}"
    })

if __name__ == "__main__":
    app.run(debug=True)
