for file in `ls ./src`
    do
        if [[ $file == *.py ]]
            then
                python3 -m py_compile src/$file
        elif [[ $file == *.cpp ]]
            then
                g++ src/$file
        elif [[ $file == *.java ]]
            then
                javac src/$file
        fi            
    done
