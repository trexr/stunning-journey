
from string import Template


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
    TMPL_BASE = TMPL_DIR + "base.html"
    BUILD_DIR = "docs/"
    PAGE_DATA = mock_data()
    TMPL_NAV = TMPL_DIR + "nav.html"

    # create tempalte to reference in iteration over page
    template_text = open(TMPL_BASE).read()
    template = Template(template_text)

    # iterate over each page invoke template with datum
    for page in PAGE_DATA:
        title = page["title"]
        output = page["output"]
        content = page["filename"]

        if output and len(output):
            page_html = template.safe_substitute(
                title=title,
                nav=open(TMPL_NAV).read(),
                index_class="active",
                content=open(content).read()
            )
            print(open(TMPL_NAV).read())
            open(output, 'w+').write(page_html)
            print("Created", title, "page")

        else:
            print("Content file is missing")


main()
