#!/opt/conda/bin/python
import os, sys
from glob import glob
if len(sys.argv) > 1:
	if sys.argv[1] == 'all':
		filelist = [os.path.splitext(os.path.basename(f))[0] for f in glob('markdown/*.md')]
	else:
		filelist = [os.path.splitext(os.path.basename(sys.argv[1]))[0]]
	for filename in filelist:
		# print('markdown/%s.md' % filename)
		mkfilename = 'markdown/%s.md' % filename		
		if os.path.exists(mkfilename):
			fline=open(mkfilename).readline().rstrip()
			if fline.find('%') != -1:
				cmd = 'pandoc -t html5 --template=html/revealjs.tmpl --standalone --section-divs --variable theme="solarized" --variable transition="linear" markdown/%s.md -o html/%s.html'
			elif fline.find('paper') != -1:
				cmd = 'pandoc -s -S --bibliography misc/jxiong.bib --filter pandoc-citeproc --csl misc/apa.csl markdown/%s.md -o html/%s.html'
			else:
				cmd = 'pandoc --toc -s -S --bibliography misc/jxiong.bib --filter pandoc-citeproc --csl misc/apa.csl markdown/%s.md -o html/%s.html'
			os.system(cmd % (filename, filename))
			print('%s.html created.' % filename)