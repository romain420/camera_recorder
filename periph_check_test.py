import os
import cv2

def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        try:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
            index += 1
            i -= 1
        except cv2.error as e:
            # Camera cannot be opened, continue to next index
            # print(f"Error: {e}")
            index += 1
        except IndexError:
            # Index is out of range, stop loop
            print("Index out of range")
            break
    return arr

def returnUsedevice():
    devices = returnCameraIndexes()
    print(f"Find the list of {len(devices)} active devices:")
    for device in devices:
        if device in [0,2]:
            print(f"\tDevice {device}: Is certainly webcam output")
        else:
            print(f"\tDevice {device}: Can be video capture device")

if __name__ == '__main__':
    # arr = returnCameraIndexes()
    # print(arr)
    returnUsedevice()