import json, sys

def keys_to_kingdom(filename):
    with open(filename, 'r') as filepointer:
        json_blob = json.loads(filepointer.read())
        if "key" in json_blob.keys():
            return "the keys are the password"


if __name__ == "__main__":
    filename = sys.argv[1]
    blah_blah = keys_to_kingdom(filename)
    print(blah_blah)