#!/usr/bin/env  python3

from pprint import pprint


class Colors:
    red = "\033[91m"
    reset = "\033[0m"
    green = "\033[92m"
    yellow = "\033[93m"


def create_clases_dictionary(
    start_clases: int, end_clases: int, start_xpath: int, end_xpath: int
):
    """ Create dict comprenhention to clases

    Args:
        start_clases (int): start number of clase
        end_clases (int): end number of clase
        start_xpath (int): start number of xpath
        end_xpath (int): end number of xpath

    Returns:
        dict: dictionary with keys and xpaths
    """

    c = Colors()

    range_clases = range(start_clases, end_clases)
    range_xpaths = ["%.2d" % i for i in range(start_xpath, end_xpath)]

    print(f"{c.yellow}The dictionary will look like this{c.reset}")

    clases = {
        f'clase_{clase}": f"//*[@id="Grid1ContainerRow_00{xpath}"]/td[11]'
        for (clase, xpath) in zip(range_clases, range_xpaths)
    }
    pprint(clases)
    return clases


if __name__ == "__main__":
    create_clases_dictionary(3, 9, 3, 7)
