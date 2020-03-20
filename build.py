
from string import Template
import glob


def mock_data():
    data = [
        {"filename": "content/about.html",
            "output": "docs/about.html",
            "title": "about"
         },
        {"filename": "content/index.html",
            "output": "docs/index.html",
            "title": "index"
         },
        {"filename": "content/work.html",
            "output": "docs/work.html",
            "title": "work"}
    ]
    return data


def main():
    targetfiles = "*.html"
    TMPL_DIR = "templates/"
    TMPL_TOP = TMPL_DIR + "top.html"
    TMPL_BOTTOM = TMPL_DIR + "bottom.html"
    BUILD_DIR = "docs/"

    PAGE_DATA = mock_data()

    # create tempalte to reference in iteration over page
    template_text = open(TMPL_DIR+'page_template.html').read()
    template = Template(template_text)

    # iterate over each page invoke template with keys from page
    for page in PAGE_DATA:
        title = page.get("title")

        if page.get("filename"):
            page_html = template.safe_substitute(
                title=title,
                index_class="active",
                output=page.get("output") or BUILD_DIR +
                title + ".html"
            )
            open(BUILD_DIR + fname, 'w+').write(page_html)

        else:
            print("missing page")
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

    # Use "format" feature of Python strings to insert data where needed for the
    # index page


main()
