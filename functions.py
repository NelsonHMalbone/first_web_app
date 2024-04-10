FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # added file name to the filepath
    """read a text file and return the list of
    to-do items.
    """
    # filepath = 'todos1.txt' # this throws an error of fileNotFound look in blue book
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # this is local try to change to Filepath but threw an error look in blue book


# but if you have it as filepath and then todos_arg it will not be optimised
def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do item list in the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("running this file dirct")
    print(get_todos())
