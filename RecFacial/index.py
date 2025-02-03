import face_recognition
import cv2

# Carrega a imagem da pessoa conhecida
imagem_conhecida = face_recognition.load_image_file("pessoa_conhecida.jpg")
encoding_conhecido = face_recognition.face_encodings(imagem_conhecida)[0]

# Captura o vídeo da webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Captura um único frame do vídeo
    ret, frame = video_capture.read()

    # Converte a imagem de BGR (OpenCV) para RGB (face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Encontra todas as faces e seus encodings no frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Com