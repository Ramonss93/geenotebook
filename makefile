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
ext:
	pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
	jupyter contrib nbextension install --user
	jupyter nbextension enable toc2/main
	jupyter nbextension enable codefolding/main
pip: ext
	pip install qgrid
	pip install pandas-datareader
	pip install tabulate
pkg: pip
	conda install -y -c r r-essentials
	conda install -y -c anaconda pytables
	conda install -y -c scitools cartopy
	conda install -y pandoc
	conda install -y graphviz
md:
	pandoc -s -S --bibliography misc/jxiong.bib --filter pandoc-citeproc --csl misc/apa.csl -o output/paper.html CropExtentInEE.md
dn:
	wget https://raw.githubusercontent.com/handsontable/handsontable/master/dist/handsontable.full.js
	wget https://raw.githubusercontent.com/handsontable/handsontable/master/dist/handsontable.full.css
sld:
	jupyter nbconvert slides.ipynb --to slides --output-dir output