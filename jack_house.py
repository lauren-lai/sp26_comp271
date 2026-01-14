PREFIX = "This is the"
SUFFIX = "house that Jack built."

ITEMS = ["", "malt", "rat", "cat", "dog"]
ACTIONS = ["", "lay in", "ate", "killed", "worried"]

# each verse builds on the previous one
malt_string = f"{ITEMS[1]} that {ACTIONS[1]} in the {SUFFIX}"
rat_string = f"{ITEMS[2]} that {ACTIONS[2]} in the {malt_string}"
cat_string = f"{ITEMS[3]} that {ACTIONS[3]} in the {rat_string}"
dog_string = f"{ITEMS[4]} that {ACTIONS[4]} in the {cat_string}"

def print_stanza(verse):
    print(f"{PREFIX} {verse}\n")

# first stanza only has prefix and suffix
def first_stanza():
    print(f"{PREFIX} {SUFFIX}\n")


# iterates through ITEMS list to print each verse
def other_stanzas():
    previous = f"{SUFFIX}"

    for i in range(1, len(ITEMS)):
        current = f"{ITEMS[i]} that {ACTIONS[i]} the {previous}"

        print(f"{PREFIX} {current}\n")
        previous = current

first_stanza()
other_stanzas()