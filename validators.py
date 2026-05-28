def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide both name and phone."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide a name."
    return inner
#test