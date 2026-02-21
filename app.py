# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)


#here we are chaeking that our backend is working properly


# From Now we are makeing An API endpoint



# This endpoint:

# Receives data (options)

# Processes data (random choice)

# Sends back JSON result

# This is real backend engineering.

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Spin API Route
@app.route("/spin", methods=["POST"])
def spin():
    data = request.get_json(force=True)

    print("Received JSON:", data)

    if not data or "options" not in data:
        return jsonify({"error": "Invalid request"}), 400

    options = data["options"]

    if not options:
        return jsonify({"error": "No options provided"}), 400

    result = random.choice(options)

    print("Selected result:", result)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)