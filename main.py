from record import Recorder
from periph_check_test import returnUsedevice
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Script for video recording from selected video source",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--show_device", "-s", type=bool, default=False, help="Display every active video device")
    parser.add_argument("--device","-d", type=int, default=0, help="Select the video device of your choice")
    parser.add_argument("--path","-p",type=str, default="./outputs", help="Enter the directory path of your choice")
    parser.add_argument("-format","-f", type=str, default="mp4", help="Enter the video format of your choice")
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    print('hey')
    args = parse_args()
    if args.show_device == True:
        returnUsedevice()

    else:
        # recorder = Recorder(width=1920,
        #                     height=1080,
        #                     path=args.path,
        #                     format=args.format,
        #                     fps=15,
        #                     device=args.device)
        # recorder.check_dir()
        # recorder.record()
        recorder = Recorder(width=1920,
                            height=1080,
                            path='./outputs',
                            format='mp4',
                            fps=15,
                            device=0)
        recorder.check_dir()
        recorder.record()