import cv2

# Open the default camera (usually 0) and set the video size
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./outputs/output.mp4', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret==True:
        # Write the frame into the output video file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Cam Recording',frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when the job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
