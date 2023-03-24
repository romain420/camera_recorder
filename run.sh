#!/bin/bash
echo "                                                   _
                                                  | |
   ___ __ _ _ __ ___    _ __ ___  ___ ___  _ __ __| | ___ _ __
  / __/ _' | '_ ' _ \  | '__/ _ \/ __/ _ \| '__/ _' |/ _ \ '__|
 | (_| (_| | | | | | | | | |  __/ (_| (_) | | | (_| |  __/ |
  \___\__,_|_| |_| |_| |_|  \___|\___\___/|_|  \__,_|\___|_|

                                                               "

echo Your are about to run video recording script :

# Run the reconding script
source venv/bin/activate
# To check active video device
#python main.py -s True
# To run recording scrip
python main.py -d 0 -p './outputs' -f mp4
