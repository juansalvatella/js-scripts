#!/bin/bash

if [[ $# -ne 2 ]]
	then
	echo "Error: Illegal number of arguments"
	echo "Try: ./min.sh /path/to/dir js"
	exit 1 
fi

if [[ -d $1 ]];
	then
	
	FILES=$(find $1 -type f -print | grep ."$2"$)
	for f in $FILES
	do
		echo "Processing $f"
	 	./jsmin < $f >> reparable.js 
	done 

fi