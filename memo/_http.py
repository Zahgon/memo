from functools import wraps

import httpx


def memweb(url: str):
    """
    Remembers input/output of a function by sending it over http to an endpoint.

    Important:
        Note that this decorator requires an extra dependeny. Ensure it is installed
        properly by running either;

        ```
        python -m pip install "memo[web]"
        ```

        You can also install it by installing all optional dependencies.

        ```
        python -m pip install "memo[all]"
        ```

    Arguments:
        url: web url to post json to
    """
    pass
