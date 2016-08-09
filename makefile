all:
	cat makefile
ee:
	earthengine authenticate
pull:
	git pull origin master --force
push:
	git config --global user.email "jun.xiong1981@gmail.com"
	git config --global user.name "Jun Xiong"
	git add .
	git commit -m 'update'
	git push origin master --force
install:
	pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
	jupyter contrib nbextension install --user
	jupyter nbextension enable toc2/main
	jupyter nbextension enable codefolding/main
	pip install qgrid
	pip install pandas-datareader
	pip install tabulate
	# conda install -y -c r r-essentials
	conda install -y -c anaconda pytables
	conda install -y -c scitools cartopy
	conda install -y pandoc
	conda install -y graphviz
md:
	pandoc -s -S --bibliography misc/jxiong.bib --filter pandoc-citeproc --csl misc/apa.csl -o output/paper.html CropExtentInEE.md
flow:
	# black (default) - white - league - sky - beige - simple - serif - blood - night - moon - solarized
	pandoc -t html5 --template=markdown/template-revealjs.html --standalone --section-divs --variable theme="solarized" --variable transition="linear" markdown/$@.md -o markdown/$@.html
classee:
	pandoc -t html5 --template=markdown/template-revealjs.html --standalone --section-divs --variable theme="solarized" --variable transition="linear" markdown/$@.md -o markdown/$@.html