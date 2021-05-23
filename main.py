from flask import Flask, jsonify, request
import requests as req

app = Flask(__name__)

@app.route("/")
def main():
    return jsonify(
        code=400,
        code_name="Bad Request",
        response="Please put in a character to code."
    )

@app.route("/api")
def api_main():

    if request.args.get("char"):
        return jsonify(
            code=200,
            code_name="OK",
            request=request.args.get("char"),
            response=[{ "item": char, "itemcode": ord(char) } for char in request.args.get("char")]
        )
    else:
        return jsonify(
            code=200,
            code_name="OK",
            message="Put in a character to see it's ASCII code!"
        )

if __name__ == "__main__":
    app.run(debug=True, port=3619)