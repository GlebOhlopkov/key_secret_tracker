
def replace_symbols(secret_key: str) -> str:
    """
    This function filter special {secret_key} from extra symbols
    :param secret_key: str
    :return:
    Working {secret_key}
    """
    # Bad symbols for secret_key
    symbols = '/=?'

    for symbol in symbols:
        secret_key = secret_key.replace(symbol, "")

    return secret_key
