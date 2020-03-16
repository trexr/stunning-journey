
from string import Template
import glob

targetfiles = "*.html"
TMPL_DIR = "templates/"
TMPL_TOP = TMPL_DIR + "top.html"
TMPL_BOTTOM = TMPL_DIR + "bottom.html"

# for fname in glob.glob(targetfiles):
#     name = fname.replace('.html', '')
#     name = 'home' if name == 'index' else name
#     top = open(TMPL_TOP).read()
#     top = top.replace(name+"-link", name + "-link active")
#     bottom = open(TMPL_BOTTOM).read()
#     fnamecontent = open(fname).read()
#     catcontent = "{} {} {}\n".format(top, fnamecontent, bottom)
#     catcontent = catcontent.replace('{{FILE_NAME}}', name)
#     open('docs/'+fname, 'w+').write(catcontent)
#     print("Created in docs:", fname)


template_text = open('page_template.html').read()
template = Template(template_text)


# Use "format" feature of Python strings to insert data where needed for the
# index page
for fname in glob.glob(targetfiles):
    middle_content = open(fname).read()
    page_html = template.safe_substitute(
        title=fname.replace('.html', ''),
        index_class="active",
        content=middle_content,
    )
    open('docs/' + fname, 'w+').write(page_html)
