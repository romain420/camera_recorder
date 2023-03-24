#!/bin/bash
echo Thanks you to clone or download this projet
echo This project is use to record video with python form a video device

echo "                                                   _
                                                  | |
   ___ __ _ _ __ ___    _ __ ___  ___ ___  _ __ __| | ___ _ __
  / __/ _' | '_ ' _ \  | '__/ _ \/ __/ _ \| '__/ _' |/ _ \ '__|
 | (_| (_| | | | | | | | | |  __/ (_| (_) | | | (_| |  __/ |
  \___\__,_|_| |_| |_| |_|  \___|\___\___/|_|  \__,_|\___|_|

                                                               "

# Create a new virtual environment with Python 3.10
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt

