from flask import Flask, request, jsonify

ApplicationInput = Flask(__name__)

@ApplicationInput.route("/")
def main():
  return "Traffic Sign Recognition API"

@ApplicationInput.route("/prediction", methods = ["POST"])
def prediction():
  data = request.get_json();
  clientinfo = data.get("Client Name")

try:
  return jsonify({
    
  "client_name": clientinfo,
  "message": "Request received successfully"
  
})

except Exception as error:
  return jsonify({
    "error" : str(error)
  }), 400

if __name__ == "__main__":
    ApplicationInput.run(debug=True)
