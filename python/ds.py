import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context


# Force TLS 1.2
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context()
        context.options |= 0x4  # OP_LEGACY_SERVER_CONNECT (for older servers)
        kwargs["ssl_context"] = context
        return super().init_poolmanager(*args, **kwargs)


session = requests.Session()
session.mount("https://", TLSAdapter())

client_id = "c6425084@urhen.com"
client_secret = "bugmenot"

proxies = {
    "http": None,
    "https": None,
}

r = session.post(
    "https://api.artsy.net/api/tokens/xapp_token",
    data={"client_id": client_id, "client_secret": client_secret},
    proxies=proxies,
)

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

print(j)
