from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "PPT Generator API Running"

@app.route("/createppt", methods=["POST"])
def create_ppt():

    title = ""

    if request.is_json:
        data = request.get_json()
        title = data.get("title", "Default PPT")
    else:
        title = request.form.get("title") or \
                request.args.get("title") or \
                "Default PPT"

    return jsonify({
        "status": "success",
        "message": f"PPT request received for {title}"
    })

if __name__ == "__main__":
    app.run(debug=True)
