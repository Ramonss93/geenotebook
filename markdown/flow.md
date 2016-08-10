% How to Data Mining
% Jun Xiong
% Aug 2016

<style>
.reveal h1 { font-size: 2.5em; } 
.reveal h3 { text-align: left; }
.reveal h4 { text-align: left; }
.reveal p { text-align: left; }
.reveal ul { text-align: left; }
</style>

### Target
List

* this 
* is
* cool

### Variables
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

### Others
- generate dataset
- plotting
- description
- presentation
