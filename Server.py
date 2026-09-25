import cv2
import os
import pickle
import numpy as np


face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def detect_faces(image):
    image_array = np.array(image)

    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    return faces
      
def get_face_encoding(image):
    image_array = np.array(image)

    encodings = face_recognition.face_encodings(image_array)

    if len(encodings) == 0:
        raise Exception("No face found")


def save_face_encoding(client_info, encoding):
    os.makedirs("face/registration", exist_ok=True)

    file_path = f"faces/registration/{client_info}.pkl"

    with open(file_path, "wb") as file:
        pickle.dump(encoding, file)

    return file_path
    

    if len(encodings) > 1:
        raise Exception("More than one face found")

    return encodings[0]


