# This file is automatically @generated by Lapidary and should not be changed by hand.

from collections.abc import Iterable
from typing import Union

import httpx
import httpx_auth
import lapidary.runtime.auth
from lapidary.runtime import NamedAuth
from typing_extensions import Literal


def api_key_tokenAuth(api_key: str) -> NamedAuth:
    return 'tokenAuth', lapidary.runtime.auth.HeaderApiKey(
        api_key=api_key,
        header_name='Authorization',
    )
