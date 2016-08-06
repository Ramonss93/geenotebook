all:
	conda install -c conda-forge jupyter_nbextensions_configurator
cre:
	cp credentials /home/jovyan/.config/earthengine/credentials
push:
	git config --global user.email "jun.xiong1981@gmail.com"
	git config --global user.name "Jun Xiong"
	git add .
	git commit -m 'update'
	git push origin master --force
in:
	conda install -c osgeo gdal
	pip install cartopy