cp ../cocotest/extras.coc .
cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coc -s -t2 --linenumbers
coconut ./src/cocotest/py3_test.coc -s -t3 --linenumbers
rm ./src/cocotest/py2_test.coc
rm ./src/cocotest/py3_test.coc
coconut ./extras.coc -s --linenumbers
coconut ./src -s --linenumbers
rm *.coc
rm ./src/*.coc
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
