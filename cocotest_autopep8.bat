cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coco -t2 -s --autopep8
rm ./src/cocotest/py2_test.coco
coconut ./src/cocotest/py3_test.coco -t3 -s --autopep8
rm ./src/cocotest/py3_test.coco
coconut ./src/cocotest/py35_test.coco -t35 -s --autopep8
rm ./src/cocotest/py35_test.coco
cp ../cocotest/extras.coco .
coconut ./extras.coco -s --autopep8
coconut ./src -s --autopep8
rm *.coco
rm ./src/*.coco
rm ./src/cocotest/*.coco
cp -r ./src/* ../cocotest/src
PAUSE
