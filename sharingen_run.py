import cv2
import tensorflow as tf

font = cv2.FONT_HERSHEY_SIMPLEX 
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2
CATEGORIES = ["boar", "ox"]
IMG_SIZE = 50



def prepare(image):
	#img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
	new_array = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
	return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("64x3-CNN.model")

cap = cv2.VideoCapture('http://192.168.1.155:8080/video')

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print()
    viewer = cv2.resize(gray, (IMG_SIZE, IMG_SIZE))
    prediction = model.predict([prepare(viewer)])
    frame = cv2.resize(frame, (1920, 1080))
    frame = cv2.putText(frame, CATEGORIES[int(prediction[0][0])], org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
