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

from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/spin", methods= ["POST"])
def spin():
    data = request.get_json()
    options = data.get("options", [])

    if not options:
        return jsonify({"error":"No options provided"}), 400
    
    result = random.choice(options)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug = True)

