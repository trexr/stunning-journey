from string import Template


def main():
    *FIRST, PAGE_DATA = constants()
    build_content(PAGE_DATA)


# mock service package
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


def constants():
    TMPL_DIR = "templates/"
    BUILD_DIR = "docs/"
    PAGE_DATA = mock_data()
    TMPL_BASE = TMPL_DIR + "base.html"
    TMPL_NAV = TMPL_DIR + "nav.html"
    return [TMPL_BASE, TMPL_DIR, TMPL_NAV, BUILD_DIR, PAGE_DATA]


def read_file(path):
    return open(path).read()


def create_page(pathandfile, content):
    if pathandfile and content:
        open(pathandfile, 'w+').write(content)
    else:
        print("Missing path to file or content ")


def swap_file_path_for_text(keyword, collection):
    for key in collection:
        if(key == keyword):
            collection[key] = read_file(collection[key])
    return collection


def build_content(data):
    TMPL_BASE, TMPL_DIR, TMPL_NAV, BUILD_DIR, PAGE_DATA = constants()

    # generate template for page creation
    template_text = read_file(TMPL_BASE)
    template = Template(template_text)
    nav = read_file(TMPL_NAV)

    for page in data:
        # add in nav template
        # will constomize this to inject appropriate active class in nav in future
        if not "nav" in page:
            page["nav"] = nav
            print(page)
        # create mappings for page generation
        tmpl_mapping = swap_file_path_for_text("filename", page)
        page_html = template.safe_substitute(tmpl_mapping)
        create_page(tmpl_mapping["output"], page_html)


main()
