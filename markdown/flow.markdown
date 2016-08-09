% How to Data Mining
% Jun Xiong
% Aug 2016


Target
--------------------

List

* this 
* is
* cool

Variables
---------

The following variables can be defined from the command line:

* theme
* transition

```bash
pandoc -t html5 --template=template-revealjs.html \
	--standalone --section-divs \
  --variable theme="beige" \
  --variable transition="linear" \
  slides.md -o slides.html
```


- generate dataset
- plotting
- description
- presentation
