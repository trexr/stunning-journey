
from string import Template
import sys
import glob
import os

# TODO:
# Need to templatize navigation and remove markup from base template,
# Right now using function to create list items then inject that into
#  base template instead of the entire nav


def main():
    TMPL_DIR = "templates/"
    BUILD_DIR = "docs/"
    PAGE_DATA = pages_to_build()
    TMPL_BASE = TMPL_DIR + "base.html"
    TMPL_NAV = TMPL_DIR + "nav.html"

    template_text = open(TMPL_BASE).read()
    # create template for the base HTML pages
    template = Template(template_text)

    # Loops over each "page" dict in  return data list

    for page in PAGE_DATA:
        # Adding in nav key to each page dictionary if
        # its not already there
        # Doing this because we may want to add a different nav template
        # for certain pages in future
        if "pagenavigation" not in page:

            # Passes current page into generated navigation html for
            # hightlighting its active state

            nav = create_navigation_HTML(PAGE_DATA, page['title'])
            page["pagenavigation"] = nav

        # mutates 'filename' value and assigns HTML found in "filename" key
        tmpl_mapping = swap_file_for_html("filename", page)

        # uses keys from mapping to create html page from template
        page_html = template.safe_substitute(tmpl_mapping)

        #  Use "output" value for filename and save to specified directory
        create_file(tmpl_mapping["output"], page_html, BUILD_DIR)

    print("Build complete")


def pages_to_build():

    # mock service package
    # all_html_files = glob.glob("content/*.html")
    # pages = []
    # print(all_html_files)
    # for file_path in all_html_files:
    #     file_name = os.path.basename(file_path)
    #     name_only, extension = os.path.splitext(file_name)
    #     print(name_only)
    #     pages.append({"filename": file_path,
    #                   "output": file_name,
    #                   "title": name_only,
    #                   "nav-title": name_only
    #                   })

    # pages = []pages.append({"filename": "content/index.html","title": "Index","output": "docs/index.html",})print(pages)
    pages = [
        {"filename": "content/index.html",
         "output": "index.html",
         "title": "home",
         "nav-title": "Trevor Stearns"
         },
        {"filename": "content/work.html",
         "output": "work.html",
         "title": "work",
         "nav-title": "work"},
        {"filename": "content/about.html",
         "output": "about.html",
         "title": "about",
         "nav-title": "about me"
         },

    ]
    return pages


def swap_file_for_html(keyword, collection):
    # simple function that replaces a value with the file contents.
    collection[key] = open(collection[key]).read()
    return collection


def create_file(pathandfile, content, builddir):
    open(builddir + pathandfile, 'w+').write(content)


def create_navigation_HTML(collection, activepage):
    # Builds list of all navigation links from collection of pages on
    # only if it has a 'nav-title' key.
    # There may be pages we don't want to be listed in nav in future so using
    # nav-title as conditional
    # Also inserts active class to respective pages
    nav = ''
    for page in collection:
        # check to see if has nav-title key else ignore
        if 'nav-title' in page:
            # che3cking title
            active = "active" if activepage == page['title'] else ""
            nav += '<li class="nav-item"><a href="' + \
                page["output"] + '" class="nav-link ' + \
                active + '">' + page["nav-title"] + '</a></li>'

    return nav


main()
