from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    name = {
            "name": "Zhen Lin"
            }
    return jsonify(name)
  
@app.route("/hello/<name>", methods=["GET"])
def hello_name(name): # the name variable being passed in here is the string that the client puts in the <name> part of the url
    h_n = {
            "message": "Hello there, {}".format(name)
            }
    return jsonify(h_n)
  
@app.route("/distance", methods=["POST"])
def cal_distance():
    r = request.get_json() # parses the POST request body as JSON
    a = float(r["a"])
    b = float(r["b"])
    a1 = a[0]
    a2 = a[1]
    b1 = b[0]
    b2 = b[1]
    distance = (a1-b1)**2+(a2-b2)**2
    return jsonify({"distance": distance, 
                    "a": a,
                    "b": b
                    })

if __name__ == '__main__':
    app.run()