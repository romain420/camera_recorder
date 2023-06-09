import cv2
import os
from datetime import datetime
import psutil

class Recorder:
    def __init__(self, width: int, height: int, path: str, fps: float, format: str, device: int):
        self.width = width
        self.height = height
        self.path = path
        self.fps = fps
        self.format = format
        self.device = device

    def check_dir(self):
        print("Check directory:")
        if os.path.isdir(self.path):
            print("\tThis directory exist\n")
        else:
            os.mkdir(self.path)
            print("\tDirectory successfully created\n")

    def source_format(self):
        if self.format == "MJPG":
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            return fourcc
        else:
            print(f"Error: Format '{self.format}' is not supported")

    def check_space(self):
        disk = psutil.disk_usage('/')
        free_space = disk.free/(1024**3)
        print("\nCheck free space on disk:")
        if free_space > 50:
            print(f"\tFree space on disk: {free_space:.2f} GB")
            return True
        else:
            print("⚠ ERROR: Not enough space ⚠")
            print(f"\tOnly free space on disk: {free_space:.2f} GB")
            print(f"\t⚠ Please make some space on your disk. You should get more than 50 Go of free space ⚠")
            return False


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
        cap = cv2.VideoCapture(self.device)
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        cap.set(cv2.CAP_PROP_FPS, self.fps)

        format = cap.get(cv2.CAP_PROP_FORMAT)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Date text setup
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 1
        color = (0, 168, 0)

        print("Video property:")
        print(f"\tWidth: {width}")
        print(f"\tHeight: {height}")
        print(f"\tFPS: {fps}")
        print(f"\tFormat: {format}")

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        video_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        fourcc = Recorder.source_format(self)#cv2.VideoWriter_fourcc(*'mp4v')#
        out = cv2.VideoWriter(f"{self.path}/video_{current_time}.avi", fourcc, fps, (int(width), int(height)))

        while (cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                # Set date and hours
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cv2.putText(frame, current_time, (0, 25), font, scale, color, 2)

                # Write the frame into the output video file
                out.write(frame)

                # Display the resulting frame
                cv2.imshow(f"Cam Recording start: {video_time}", frame)

                # Press 'q' to exit the loop
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            else:
                break

        # Release everything when the job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()