
import sys
import glob
import os
from jinja2 import Template, Environment, BaseLoader

# TODO:
# Need to templatize navigation and remove markup from base template,
# Right now using function to create list items then inject that into
#  base template instead of the entire nav

TMPL_DIR = "templates/"
BUILD_DIR = "docs/"
TMPL_BASE = TMPL_DIR + "base.html"
TMPL_NAV = TMPL_DIR + "nav.html"
NAV_TITLES = {
    "index": "Trevor Stearns"
}


def main():

    PAGE_DATA = update_navtitles(pages_to_build())
    nav_file = open(TMPL_NAV).read()
    nav_tmpl = Template(nav_file)

    template_html = open(TMPL_BASE).read()
    template = Template(template_html)

    # Loops over each "page" dict in  return data list

    for page in PAGE_DATA:

        # Adding in nav key to each page dictionary if
        # its not already there
        # Doing this because we may want to add a different nav template
        # for certain pages in future
        if "pagenavigation" not in page:

            render_nav_html = nav_tmpl.render(
                pages=PAGE_DATA, current=page['title'])

            # Passes current page into generated navigation html for
            # hightlighting its active state
            page["pagenavigation"] = render_nav_html

        # mutates 'filename' value and assigns HTML found in "filename" key
        tmpl_mapping = swap_file_for_html("filename", page)

        # uses keys from mapping to create html page from template
        page_html = template.render(tmpl_mapping)

        #  Use "output" value for filename and save to specified directory
        create_file(page["output"], page_html, BUILD_DIR)

    print("Build complete")


def update_navtitles(data):
    for page in data:
        if page['navtitle'] in NAV_TITLES:
            page['navtitle'] = NAV_TITLES[page['navtitle']]
    return data


def pages_to_build():

    html_files = glob.glob("content/*.html")
    pages = []

    for file_path in html_files:
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)

        pages.append(
            {"filename": file_path,
             "output": file_name,
             "title": name_only,
             "navtitle": name_only
             })

    return pages


def swap_file_for_html(keyword, collection):
    # simple function that replaces a value with the file contents.
    collection[keyword] = open(collection[keyword]).read()
    return collection


def create_file(pathandfile, content, builddir):
    open(builddir + pathandfile, 'w+').write(content)


main()
