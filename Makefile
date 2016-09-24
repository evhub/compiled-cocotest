.PHONY: quick
quick:
	python ../coconut/tests
	cp -r ../coconut/tests/dest .

.PHONY: force
force:
	python ../coconut/tests -f
	cp -r ../coconut/tests/dest .

.PHONY: linenumbers
linenumbers:
	python ../coconut/tests -l
	cp -r ../coconut/tests/dest .

.PHONY: run
run:
	python3 ./dest/extras.py
	python3 ./dest/runner.py
	python2 ./dest/runner.py

.PHONY: test
test: quick run
