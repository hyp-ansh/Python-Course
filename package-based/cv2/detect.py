import cv2
from random import *
# Loading some pre-trained data face from open-cv "https://github.com/opencv/opencv/tree/master/data/haarcascades"
trained_face = cv2.CascadeClassifier("face.xml")
trained_smile = cv2.CascadeClassifier("smile.xml")

# Resizing Image with same Aspect Ratio
def ResizeRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=inter)

# Opens the image
def show(title, image):
    # Opens/shows the image file
    cv2.imshow(title, image)
    # Waits for user to close
    cv2.waitKey()

# Opens the camera stream
def vid_show(title, stream):
    cv2.imshow(title, stream)
    key = cv2.waitKey(1)
    return key

# Converting to grayscale
def gray(image):
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_frame

# Locating the coordinates for the face(s)
def locate_face(image):
    face_coordinates = trained_face.detectMultiScale(image)
    return face_coordinates

# Drawing rectangle around the face
def face_box(x, y, w, h):
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame

def circle():
    return

cam_stream = cv2.VideoCapture(0)
while True:
    # Reads the current frame
    is_frame , frame = cam_stream.read()
    frame = ResizeRatio(frame, height=600)
    # Mirrors the frame
    # frame = cv2.flip(frame, 1)
    gray_frame = gray(frame)
    coordinates_raw = locate_face(gray_frame)
    for coordinate in coordinates_raw:
        (x, y, w, h) = coordinate
        face_box(x, y, w, h)
    key = vid_show("Detect x Webcam", frame)
    if key == 81 or key == 113:
        break

cam_stream.release()
cv2.destroyAllWindows()

"""
For Pictures
raw_img = cv2.imread("images/img00.jpg")
frame = ResizeRatio(raw_img, width=720)
gray_frame = gray(frame)
coordinates_raw = locate_coordinate(gray_frame)

# For making rectangle around all faces
for coordinate in coordinates_raw:
    (x, y, w, h) = coordinate
    final_frame = rectangle(x, y , w, h)
show("Detect x Face", final_frame)
# print(coordinates_raw)
"""
