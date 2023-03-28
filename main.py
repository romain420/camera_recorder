from record import Recorder
from periph_check_test import returnUsedevice
import argparse
from datetime import datetime

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
    start_time = datetime.now()
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"⚠ The record start at: {time_str} ⚠\n")
    print("""
                                                           _
                                                          | |
           ___ __ _ _ __ ___    _ __ ___  ___ ___  _ __ __| | ___ _ __
          / __/ _' | '_ ' _ \  | '__/ _ \/ __/ _ \| '__/ _' |/ _ \ '__|
         | (_| (_| | | | | | | | | |  __/ (_| (_) | | | (_| |  __/ |
          \___\__,_|_| |_| |_| |_|  \___|\___\___/|_|  \__,_|\___|_|
    """)
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
        recorder = Recorder(width=1280,
                            height=720,
                            path='./outputs',
                            format='MJPG',
                            fps=30,
                            device=0)
        if recorder.check_space():
            recorder.check_dir()
            recorder.record()

        stop_time = datetime.now()
        delta_time = stop_time - start_time
        print(f"\nExecution time: {delta_time}")
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"End of video recording: {time_str}")