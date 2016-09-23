.PHONY: quick force linenumbers run test

quick:
	python ../coconut/tests
	cp -r ../coconut/tests/dest .

force:
	python ../coconut/tests -f
	cp -r ../coconut/tests/dest .

linenumbers:
	python ../coconut/tests -l
	cp -r ../coconut/tests/dest .

run:
	python3 ./dest/extras.py
	python3 ./dest/runner.py
	python2 ./dest/runner.py

test: quick run
