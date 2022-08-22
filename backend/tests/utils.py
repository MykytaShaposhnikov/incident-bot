import os


def get_mock_server_mode() -> str:
    """Returns a str representing the mode.
    :return: threading/multiprocessing
    """
    mode = os.environ.get("BOLT_PYTHON_MOCK_SERVER_MODE")
    if mode is None:
        # We used to use "multiprocessing"" for macOS until Big Sur 11.1
        # Since 11.1, the "multiprocessing" mode started failing a lot...
        # Therefore, we switched the default mode back to "threading".
        return "threading"
    else:
        return mode