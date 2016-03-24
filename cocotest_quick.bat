cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coc -t2 -s
rm ./src/cocotest/py2_test.coc
coconut ./src/cocotest/py3_test.coc -t3 -s
coconut ./src/cocotest/py35_test.coc -t3 -s
rm ./src/cocotest/py3_test.coc
cp ../cocotest/extras.coc .
coconut ./extras.coc -s
coconut ./src -s
rm *.coc
rm ./src/*.coc
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
