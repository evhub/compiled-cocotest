cp ../cocotest/extras.coc .
cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coc -s -t2
coconut ./src/cocotest/py3_test.coc -s -t3
rm ./src/cocotest/py2_test.coc
rm ./src/cocotest/py3_test.coc
coconut ./extras.coc -s
coconut ./src -s
rm *.coc
rm ./src/*.coc
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
