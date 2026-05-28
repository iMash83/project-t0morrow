import pickle

from contacts import AddressBook


def save_data(book, filename="data/addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print(f"Address book saved to '{filename}'. It will be loaded on the next app run.")


def load_data(filename="data/addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            book = pickle.load(f)
        print(f"Address book loaded from '{filename}'.")
        return book
    except FileNotFoundError:
        return AddressBook()
