cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coc -s -t2 --autopep8
coconut ./src/cocotest/py3_test.coc -s -t3 --autopep8
rm ./src/cocotest/py2_test.coc
rm ./src/cocotest/py3_test.coc
coconut ./src -s --autopep8
rm ./src/*.coc
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
