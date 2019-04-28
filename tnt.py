class l_row:
    def __init__(self, row):
        self.hint = row[0]
        self.spaces = row[1:]

# What does a tree need to know?
    # Does it need to know it's position in the campground?
    # Does it need to know all the information about the level?
class l_tree:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.has_tent = False

    def count_free_spaces(self):
        # l_tree really needs to interact with level to get this information.
        pass

    def get_free_spaces(self):
        pass


class level:
    """
    each row, and each column, has 1 metadata field, and x - 1 fields.
    """
    def __init__(self, level):
        self.level = level

        # initialize row data
        self.rows = []
        for row in self.level:
            if row[0] == " ":
                # this row only has column metadata, so
                continue
            self.rows.append(l_row(row))

        # initialize tree data
        self.trees = []
        for row in self.level:
            for space in row:
                if space == "T":
                    self.trees.append(l_tree())

    def grassify(self, row):
        for space in row.spaces:
            i = row.spaces.index(space)
            row.spaces.pop(i)
            row.spaces.insert(i, "G")

    def print_level(self):
        for row in self.rows:
            print(row.hint, row.spaces)
        print(" ")

level_one = [
    [" ", "2", "0", "1", "1", "1"],
    ["1", " ", " ", " ", " ", " "],
    ["1", " ", "T", " ", "T", " "],
    ["0", " ", " ", " ", " ", " "],
    ["2", "T", "T", " ", " ", " "],
    ["1", " ", " ", " ", " ", "T"]
]


l1 = level(level_one)
l1.print_level()

for row in l1.rows:
    if row.hint == "0":
        l1.grassify(row)

l1.print_level()
