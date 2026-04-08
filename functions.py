FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items
    """

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__": # When ran directly, value of name is main.
    # When ran from a different file, value of main is name of script in which it is located, e.g. functions.
    print("Hello from functions")