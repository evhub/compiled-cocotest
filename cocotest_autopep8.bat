cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coc -t2 -s --autopep8
rm ./src/cocotest/py2_test.coc
coconut ./src/cocotest/py3_test.coc -t3 -s --autopep8
rm ./src/cocotest/py3_test.coc
coconut ./src/cocotest/py35_test.coc -t35 -s --autopep8
rm ./src/cocotest/py35_test.coc
cp ../cocotest/extras.coc .
coconut ./extras.coc -s --autopep8
coconut ./src -s --autopep8
rm *.coc
rm ./src/*.coc
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
