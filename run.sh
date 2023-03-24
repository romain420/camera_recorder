#!/bin/bash
echo Your are about to run video recording script :

# Run the reconding script
source venv/bin/activate
# To check active video device
#python main.py -s True
# To run recording scrip
python main.py -d 0 -p './outputs' -f mp4
