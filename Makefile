.PHONY: quick force linenumbers test

quick:
	python ../coconut/tests
	cp -r ../coconut/tests/dest .

force:
	python ../coconut/tests -f
	cp -r ../coconut/tests/dest .

linenumbers:
	python ../coconut/tests -l
	cp -r ../coconut/tests/dest .

test:
	python3 ./extras.py
	python3 ./cocotest/runner.py
	python2 ./cocotest/runner.py
