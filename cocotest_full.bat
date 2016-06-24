cp -r ../cocotest/src/* ./src
coconut ./src/cocotest/py2_test.coco -t2 -sf
rm ./src/cocotest/py2_test.coco
coconut ./src/cocotest/py3_test.coco -t3 -sf
rm ./src/cocotest/py3_test.coco
coconut ./src/cocotest/py35_test.coco -t35 -sf
rm ./src/cocotest/py35_test.coco
cp ../cocotest/extras.coco .
coconut ./extras.coco -sf
coconut ./src -sf
rm *.coco
rm ./src/*.coco
rm ./src/cocotest/*.coco
rm ./src/cocotest/*.coc
cp -r ./src/* ../cocotest/src
PAUSE
