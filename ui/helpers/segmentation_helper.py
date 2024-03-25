import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# interact with FastAPI endpoint
backend = "http://fastapi:8000/predict"

def process(image, server_url: str = backend):

    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r