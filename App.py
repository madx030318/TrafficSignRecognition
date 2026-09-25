from flask import Flask, request, jsonify

ApplicationInput = Flask(__name__)

@ApplicationInput.route("/")
def main():
  return "Traffic Sign Recognition API"

@ApplicationInput.route("/prediction", methods = ["POST"])
def prediction():
  data = request.get_json();
  clientinfo = data.get("Client Name")
  imageinfo = data.get("Image_URL")

try:

  image = download_image(image_url)

  faces = detect_faces(image)

  return jsonify({
    "client_name": client_name,
    "faces_detected": len(faces)
  })
  

except Exception as error:
  return jsonify({
    "error" : str(error)
  }), 400

if __name__ == "__main__":
    ApplicationInput.run(debug=True)
