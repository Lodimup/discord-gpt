def chunk_message(message, chunk_size):
    """
    Splits a given message into chunks of a specified size and yields those chunks one by one.

    Args:
    message (str): The message to split into chunks.
    chunk_size (int): The size of each chunk.

    Yields:
    str: A chunk of the message.
    """
    for i in range(0, len(message), chunk_size):
        yield message[i:i+chunk_size]
