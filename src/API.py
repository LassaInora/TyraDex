import ctypes
import os
import pathlib
import platform
import subprocess

import requests

import src.TyradexErrors
from src.tdx_file import TDXFile

_CACHE_FOLDER = pathlib.Path(os.path.join(os.path.expanduser("~"), ".TyraDex"))
if not os.path.exists(_CACHE_FOLDER):
    os.makedirs(_CACHE_FOLDER)
    if platform.system() == "Windows":  # Windows
        ctypes.windll.kernel32.SetFileAttributesW(_CACHE_FOLDER, 0x02)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["chflags", "hidden", _CACHE_FOLDER])

class Tyradex:
    _URL = "https://tyradex.app/api/v1/"

    _HEADER = {
        "User-Agent": "Tyradex For Python Version 1.0-alpha",
        "From": "https://github.com/LassaInora/TyraDex",
        'Content-type': 'application/json'
    }

    @classmethod
    def call(cls, endpoint: str) -> dict | None:
        cache = TDXFile.get(endpoint)
        if not cache.exists or not cache.is_valid:
            request = requests.get(cls._URL + endpoint, headers=cls._HEADER)
            try:
                rjson = request.json()
            except requests.exceptions.JSONDecodeError:
                rjson = {
                    "status": request.status_code,
                    "message": request.reason
                }
            if isinstance(rjson, dict) and rjson.get('status') == 404:
                src.TyradexErrors.PageNotFound(endpoint).print()
                return None
            else:
                cache.update(request.json())
        return cache.data




if __name__ == '__main__':
    print(Tyradex.call('pokemon'))