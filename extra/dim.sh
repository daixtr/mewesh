#!/bin/sh
#

dim () 
{ 
    cols=$(tput cols);
    lines=$(tput lines);
    echo -n "${cols}x${lines}"
}

########################################
# get accurate shell terminal dimensions
dim
