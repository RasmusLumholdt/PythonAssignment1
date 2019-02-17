import json
import urllib.request as urllib
import io


url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'


def create_structure():

    structure = {}
    with urllib.urlopen(url) as dlFile:
        data = dlFile.read().decode('utf-8')
        cleanData = data.strip("\r")
        f = io.StringIO(cleanData)
        lines = f.readlines()

        for x in range(1, len(lines)):
            line = lines[x]
            values = list(map(int, line.split(",")))

            # the pointer variable holds the current dict
            pointer = structure
            # iterate through the first 3 values
            for y in range(3):
                value = values[y]
                if pointer.get(value) is not None:
                    # if the next pointer already exists, we just move to that pointer
                    pointer = pointer.get(value)
                else:
                    # if the pointer does not exist, we create a new dict, and move to it using the pointer
                    pointer[value] = {}
                    pointer = pointer[value]

            # set the innermost value in the final pointer dict
            pointer[values[3]] = values[4]

    return structure


def print_structure(structure):
    print(json.dumps(structure, indent=4))


structure = create_structure()
print_structure(structure)
