.PHONY: quick
quick:
	python ../coconut/tests
	cp -r ../coconut/tests/dest .

.PHONY: linenumbers
linenumbers:
	python ../coconut/tests -l
	cp -r ../coconut/tests/dest .

.PHONY: mypy
mypy:
	python ../coconut/tests --mypy
	cp -r ../coconut/tests/dest .

.PHONY: run
run:
	python3 ./dest/extras.py
	python3 ./dest/runner.py
	python2 ./dest/runner.py

.PHONY: clean
clean:
	rm -rf ../coconut/tests/dest
	rm -rf ./dest

.PHONY: force
force: clean quick

.PHONY: test
test: quick run
