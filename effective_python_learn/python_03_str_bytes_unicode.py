# coding: utf-8
# str bytes unicode learn
def to_str(bytes_or_str):
    """
    python 3 接受str或bytes, return str 方法
    :param bytes_or_str: str or bytes string
    :return: instance of str
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str):
    """
    python 3 receive str or bytes, return bytes ,
    :param bytes_or_str: str or bytes string
    :return: instance of bytes
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value
