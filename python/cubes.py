from xml.etree import ElementTree


def color_counter(xml):
    root = ElementTree.fromstring(xml)

    dct = {"red": 0, "green": 0, "blue": 0}

    def count(cube, level):
        dct[cube.get("color")] += level
        for child in cube:
            count(child, level + 1)

    count(root, 1)

    print(f"{dct['red']} {dct['green']} {dct['blue']}")


xml = input()

color_counter(xml)
