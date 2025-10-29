import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("canera not detected")
else:
    while True:
        ret, frame =camera.read()
    if not ret:
        print("no frame recorded")
        break
    cv2.imshow("recording", frame)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
