#!/bin/bash

for file in `ls ./src`
    do
        echo "Running test for $file"
        if [[ $file == *.py ]]
            then
                python3 -m py_compile src/$file
        elif [[ $file == *.cpp ]]
            then
                g++ src/$file
        elif [[ $file == *.java ]]
            then
                javac src/$file
        else
            echo "Unknown file type"
            return 1
        fi            
    done
