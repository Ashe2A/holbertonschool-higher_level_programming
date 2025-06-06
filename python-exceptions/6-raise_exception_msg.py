#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raises a type exception with a message

    Args:
        message (str, optional): The message of the exception.
            Defaults to empty string.

    Raises:
        NameError: name exception with message
    """
    raise NameError(message)
