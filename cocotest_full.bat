cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coc -sf -t2
coconut ./src/cocotest/py3_test.coc -sf -t3
rm ./src/cocotest/py2_test.coc
rm ./src/cocotest/py3_test.coc
coconut ./src -sf
rm ./src/*.coc
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
