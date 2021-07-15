#!/bin/bash

# not sure how I am going to get around this. 
# I guess I can do a for loop.

# I need to loop through each file, and if the file has changed then, 
FILENAME="/home/samuel/bin/*"
# timediff in seconds. 120 == 2 min
OLDTIME=2111
CURTIME=$(date +%s)
FILETIME=$(stat --format %Y $FILENAME)
TIMEDIFF=$(expr $CURTIME - $FILETIME)

# if timediff is bigger than oldtime,
if [ $TIMEDIFF -lt $OLDTIME ];then
    echo okays
fi