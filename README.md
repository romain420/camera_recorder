# Camera recorder

## Introduction
This repository is usefull to record video from input device on your computer. It gives you the oportunity to do this directly by running a python or shell script. It can be use on **Linux**. We are not sure this project can run on **Windows**

## Installation
Follow those installation steps to run the project:
### 1- clone the project:
```shell
git clone https://github.com/romain420/camera_recorder.git camera_recorder
cd camera_recorder
```
### 2- Create a environement and install all differents packages:
For this you have 2 differents options:  
First you can run `install.sh`
```shell
bash install.sh
```
Else you can manually run all line inside this file
```shell
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
You normally install all depency needed to run the project. To avoid error make sure you got virtual environnement active, check if you have `(venv)` at the begining of your line.

## Run project
To run the project, there is once again 2 differents ways to do it.  
First you can run `run.sh`
```shell
bash run.sh 
```
*It will activate your virtual environment even if it is not active yet*  
Second you can run the script in command line
```shell
source venv/bin/activate
python main.py
```
## Additionnal features
You can customise a little bit the video recording by changing parameter in `main.py` running command.  
By this way:
```shell
# To get help to check the differents arguments
python main.py -h

# To check all active video device
python main.py --show_device True

# Or simply to run script with arguments
python main.py --path './outputs' --device 0 --format mp4
```

## Conclusion
I hope this `README.md` have been usefull for you. If you have any difficulties by running this script, you can open an issue or directly contact me.
