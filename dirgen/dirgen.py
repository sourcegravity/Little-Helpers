import xml.etree.ElementTree as ET
import os

def ensure_dir(path):
    """
    Creates a directory if it does not already exist.
    """
    if not os.path.exists(path):
        os.mkdir(path)

def create_dir_from_xml(rootdir, node):
    """
    Creates the directory tree described by `node` inside the directory `rootdir`.

    `node` itself represents a single directory of a directory tree. It must have a 'name'
    attribute and can optionally contain a list of child <dir> nodes.

    The function first creates the single directory represented by `node` and
    then calls itself recursively for all child <dir> nodes with the path of the
    created directory as new `rootdir`.
    """
    # check if we have a 'name' attribute
    dirname = node.attrib['name']
    if not dirname:
        raise Exception("Missing 'name' attribute")

    dirpath = os.path.join(rootdir, dirname)

    # create directory
    ensure_dir(dirpath)

    # recursively create subdirectories
    for child in node.findall('dir'):
        create_dir_from_xml(dirpath, child)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Create a directory structure from a given xml file.')
    parser.add_argument('config_file', metavar="XML-CONFIG",
                        help='Path to a xml file that describes the directory structure to create.')
    args = parser.parse_args()

    tree = ET.parse(args.config_file)
    root = tree.getroot()
    create_dir_from_xml("./", root)


if __name__ == "__main__":
    main()