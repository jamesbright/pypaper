import os
import sys

from pypaper import general_tools as gt
from pypaper import latex_tools as lt
from pypaper import py_tools as pyt


def new_paper(folder_path, title, initials):
    print("building new paper")
    root_folder_name = title + "-paper"
    print(folder_path, title, initials)
    base_path = gt.build_base_folders(folder_path, root_folder_name, initials)
    lt.build_base_folders(base_path, root_folder_name, initials, author="")
    pyt.build_base_folders(base_path, initials)
    gt.add_to_gitignore(base_path, initials)
    pass


def get_script_path():
    ffp = os.path.dirname(os.path.realpath(sys.argv[0])) + "/"
    return ffp


def build_new_bibtex(latex_ffp, big_bibtex_ffp, new_bibtex_ffp='new_bibtex.bib'):
    citations = lt.extract_citation_keys_from_latex(latex_ffp=latex_ffp)
    print(citations)
    bstr = lt.compile_bibtex(citations, big_bibtex_ffp)
    with open(new_bibtex_ffp, 'w') as bibfile:
        bibfile.write(bstr)


def console_help():
    print("Usage: python manage.py <option> <args>")
    print("Options: paper <name> <optional: initials>")
    print("         chapter <name> <optional: initials>")
    print("         short-bib <latex file path> <large bibtex path> <optional: new bibtex path>")

if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        console_help()
        sys.exit(1)
    folder_path = get_script_path()

    # start the program
    if arg1 in ["paper", "chapter"]:
        try:
            title = sys.argv[2]
        except IndexError:
            console_help()
            sys.exit(1)
        if len(sys.argv) < 4:
            # prompt user
            initials = "ni"
            pass
        else:
            initials = sys.argv[3]
        new_paper(folder_path, title, initials)
    elif arg1 == "short-bib":
        try:
            latex_ffp = sys.argv[2]
            big_bibtex_ffp = sys.argv[3]
        except IndexError:
            console_help()
            sys.exit(1)
        if len(sys.argv) < 5:
            new_bibtex_ffp = 'new_bibtex.bib'
        else:
            new_bibtex_ffp = sys.argv[4]
        build_new_bibtex(latex_ffp, big_bibtex_ffp, new_bibtex_ffp)

    else:
        console_help()