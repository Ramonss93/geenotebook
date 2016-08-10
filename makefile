all:
	cat makefile
run:
dock:
	docker ps -q
	docker port  `docker ps -q` 
stop:
	docker stop  `docker ps -q`
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