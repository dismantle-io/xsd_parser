import json
from lxml import etree


def xsd_to_dict(element):
    data = {"type": element.tag}

    if element.text and element.text.strip():
        data["text"] = element.text.strip()

    if element.attrib:
        data["attributes"] = element.attrib

    children = list(element)
    if children:
        data["children"] = [xsd_to_dict(child) for child in children]

    return data


def xsd_to_json(input_file):
    with open(input_file, "r") as file:
        tree = etree.parse(file)
        root = tree.getroot()
        parsed_data = xsd_to_dict(root)

    output_file = input_file.rsplit(".", 1)[0] + ".json"
    with open(output_file, "w") as file:
        json.dump(parsed_data, file, indent=4)


if __name__ == "__main__":
    xsd_file = input("Enter the path to the XSD file: ")
    xsd_to_json(xsd_file)
    print(f"JSON output saved to {xsd_file.rsplit('.', 1)[0] + '.json'}")
