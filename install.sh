#!/bin/bash
echo Thanks you to clone or download this projet
echo This project is use to record video with python form a video device

# Create a new virtual environment with Python 3.10
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt

