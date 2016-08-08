all:
	cat makefile
flow:
	pandoc -t html5 --template=template-revealjs.html \
		--standalone --section-divs \
		--variable theme="beige" \
		--variable transition="linear" \
		$@.md -o $@.html