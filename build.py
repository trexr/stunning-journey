
import glob

targetfiles = "*.html"
TMPL_DIR = "templates/"
TMPL_TOP = TMPL_DIR + "top.html"
TMPL_BOTTOM = TMPL_DIR + "bottom.html"

for fname in glob.glob(targetfiles):
    name = fname.replace('.html', '')
    name = 'home' if name == 'index' else name
    top = open(TMPL_TOP).read()
    top = top.replace(name+"-link", name + "-link active")
    bottom = open(TMPL_BOTTOM).read()
    fnamecontent = open(fname).read()
    catcontent = "{} {} {}\n".format(top, fnamecontent, bottom)
    catcontent = catcontent.replace('{{FILE_NAME}}', name)
    open('docs/'+fname, 'w+').write(catcontent)
    print("Created in docs:", fname)
