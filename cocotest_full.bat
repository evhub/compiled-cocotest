cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coc -t2 -sf
rm ./src/cocotest/py2_test.coc
coconut ./src/cocotest/py3_test.coc -t3 -sf
rm ./src/cocotest/py3_test.coc
cp ../cocotest/extras.coc .
coconut ./extras.coc -sf
coconut ./src -sf
rm *.coc
rm ./src/*.coc
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
