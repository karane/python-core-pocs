import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path


# CSV EXAMPLE
def write_csv(filename):
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Paris"},
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Wrote {len(data)} rows to {filename}")


def read_csv(filename):
    with open(filename, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    print("Read from CSV:")
    for row in rows:
        print(row)
    return rows


# JSON EXAMPLE
def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Wrote JSON to {filename}")


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("Read from JSON:")
    for item in data:
        print(item)
    return data


# XML EXAMPLE
def write_xml(filename, data):
    root = ET.Element("people")

    for person in data:
        person_elem = ET.SubElement(root, "person")
        for key, value in person.items():
            child = ET.SubElement(person_elem, key)
            child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"Wrote XML to {filename}")


def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data = []
    for person_elem in root.findall("person"):
        person = {child.tag: child.text for child in person_elem}
        data.append(person)

    print("Read from XML:")
    for item in data:
        print(item)
    return data


def main():
    base = Path(".")
    csv_file = base / "people.csv"
    json_file = base / "people.json"
    xml_file = base / "people.xml"

    # CSV
    write_csv(csv_file)
    csv_data = read_csv(csv_file)

    # JSON
    write_json(json_file, csv_data)
    json_data = read_json(json_file)

    # XML
    write_xml(xml_file, json_data)
    xml_data = read_xml(xml_file)

    print("\nData successfully converted across CSV → JSON → XML")


if __name__ == "__main__":
    main()
