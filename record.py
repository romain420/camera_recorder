import cv2
import os

# Open the default camera (usually 0) and set the video size
# cap = cv2.VideoCapture(0)
# # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
# print(cap)
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('./outputs/output.mp4', fourcc, 20.0, (640, 480))
#
# while(cap.isOpened()):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     if ret==True:
#         # Write the frame into the output video file
#         out.write(frame)
#
#         # Display the resulting frame
#         cv2.imshow('Cam Recording',frame)
#
#         # Press 'q' to exit the loop
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# # Release everything when the job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()

class Recorder:
    def __init__(self, width: int, height: int, path: str, fps: float, format: str):
        self.width = width
        self.height = height
        self.path = path
        self.fps = fps
        self.format = format

    def check_dir(self):
        if os.path.isdir(self.path):
            print("This directory exist")
        else:
            os.mkdir(self.path)
            print("Directory successfully created")

    def source_format(self):
        if self.format == "mp4":
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            return fourcc
        else:
            print(f"Error: Format '{self.format}' is not supported")

    def periph_choice(self):
        # checks the first 10 indexes.
        index = 0
        arr = []
        i = 10
        while i > 0:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
            index += 1
            i -= 1
        return arr# TODO write method to find the go video peripheric to record video

    def record(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        cap.set(cv2.CAP_PROP_FPS, self.fps)

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)

        print("Video property:")
        print(f"\tWidth: {width}")
        print(f"\tHeight: {height}")
        print(f"\tFPS: {fps}")

        fourcc = Recorder.source_format(self)#cv2.VideoWriter_fourcc(*'mp4v')#
        out = cv2.VideoWriter(f"{self.path}/output.mp4", fourcc, fps, (int(width), int(height)))

        while (cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                # Write the frame into the output video file
                out.write(frame)

                # Display the resulting frame
                cv2.imshow('Cam Recording', frame)

                # Press 'q' to exit the loop
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            else:
                break

        # Release everything when the job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()