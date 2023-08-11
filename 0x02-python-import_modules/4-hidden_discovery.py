#!/usr/bin/python3
if __name__ == "__main__":

    # Import module from hidden_4.pyc
    import hidden_4

    for item in dir(hidden_4):
        if not item.startswith("__"):
            print(item)
