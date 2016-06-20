cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coco -t2 -s
rm ./src/cocotest/py2_test.coco
coconut ./src/cocotest/py3_test.coco -t3 -s
rm ./src/cocotest/py3_test.coco
coconut ./src/cocotest/py35_test.coco -t35 -s
rm ./src/cocotest/py35_test.coco
cp ../cocotest/extras.coco .
coconut ./extras.coco -s
coconut ./src -s
rm *.coco
rm ./src/*.coco
rm ./src/cocotest/*.coco
cp -r ./src/* ../cocotest/src
PAUSE
