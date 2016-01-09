#!/bin/sh
#
#********************************************************************
# The client shell-hook that in used to collaborate pair-programming
#********************************************************************

FIFO_=$(mktemp)
rm $FIFO_
FIFO=${FIFO_}$(date +'%s')
mkfifo $FIFO
PORT=${1:-12345}

(
    /usr/bin/ttyplay -n $FIFO | ssh daixtr@192.168.5.168 PORT=$PORT ttycast -s $(~/bin/dim.sh)
) >/dev/null &

/usr/bin/ttyrec $FIFO
