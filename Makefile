.PHONY: quick force linenumbers test

quick:
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
	rm ./src/cocotest/*.coc
	cp -r ./src/* ../cocotest/src

force:
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

linenumbers:
	cp -r ../cocotest/src/* ./src
	coconut ./src/cocotest/py2_test.coco -t2 -sl
	rm ./src/cocotest/py2_test.coco
	coconut ./src/cocotest/py3_test.coco -t3 -sl
	rm ./src/cocotest/py3_test.coco
	coconut ./src/cocotest/py35_test.coco -t35 -sl
	rm ./src/cocotest/py35_test.coco
	cp ../cocotest/extras.coco .
	coconut ./extras.coco -sl
	coconut ./src -sl
	rm *.coco
	rm ./src/*.coco
	rm ./src/cocotest/*.coco
	rm ./src/cocotest/*.coc
	cp -r ./src/* ../cocotest/src

test:
	python ./extras.py
	python ./src/runner.py
	python2 ./src/runner.py
	pypy ./src/runner.py
