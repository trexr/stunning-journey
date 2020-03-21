from string import Template
import sys


def main():
    *FIRST, PAGE_DATA = constants()
    build_content(PAGE_DATA)


def constants():
    TMPL_DIR = "templates/"
    BUILD_DIR = "docs/"
    PAGE_DATA = mock_data()
    TMPL_BASE = TMPL_DIR + "base.html"
    TMPL_NAV = TMPL_DIR + "nav.html"
    return [TMPL_BASE, TMPL_DIR, TMPL_NAV, BUILD_DIR, PAGE_DATA]


def mock_data():
    # mock service package
    data = [
        {"filename": "content/index.html",
            "output": "index.html",
            "title": "home",
            "nav-name": "Trevor Stearns"
         },
        {"filename": "content/work.html",
            "output": "work.html",
            "title": "work",
            "nav-name": "work"},
        {"filename": "content/about.html",
            "output": "about.html",
            "title": "about",
            "nav-name": "about me"
         },

    ]
    return data


def read_file(path):
    try:
        return open(path).read()
    except:
        print("     Oops!", sys.exc_info()[0], "occured: ", path)
        print("     Make sure you have correct files in content folder.")


def create_page(pathandfile, content):
    *VARS, BUILD_DIR, PAGE_DATA = constants()

    try:
        open(BUILD_DIR + pathandfile, 'w+').write(content)
        print("Created", pathandfile)
    except:
        print("     Oops!", sys.exc_info()[0], "occured: ", pathandfile)


def swap_file_path_for_text(keyword, collection):
    for key in collection:
        if(key == keyword):
            collection[key] = read_file(collection[key])
    return collection


def build_navigation(collection, activepage):
    nav = ''
    for page in collection:
        # check to see if has nav-name key else ignore
        if 'nav-name' in page:
            active = "active" if activepage == page['title'] else ""
            nav += '<li class="nav-item"><a href="' + \
                page["output"] + '" class="nav-link ' + \
                active + '">' + page["nav-name"] + '</a></li>'

    return nav


def build_content(data):
    TMPL_BASE, *VARS = constants()

    # generate template for page creation
    template_text = read_file(TMPL_BASE)
    template = Template(template_text)
    # nav = read_file(TMPL_NAV)

    for page in data:
        # add in nav template to page dict
        if not "nav" in page:
            # create page based navigation
            nav = build_navigation(data, page['title'])
            page["nav"] = nav

        # create mappings for page generation
        tmpl_mapping = swap_file_path_for_text("filename", page)
        page_html = template.safe_substitute(tmpl_mapping)

        create_page(tmpl_mapping["output"], page_html)

    print("Build complete")


main()
