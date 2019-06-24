import json
import os

import asks
from asks import Session
from quart import request, Response
from quart_trio import QuartTrio

ENABLE_DEBUG = bool(os.environ.get('ROCKETCHAT_WEBHOOK_PROXY_DEBUG', False))
TARGET_URL = os.environ.get("ROCKETCHAT_WEBHOOK_PROXY_TARGET")
if not TARGET_URL:
    raise RuntimeError("Required env variable ROCKETCHAT_WEBHOOK_PROXY_TARGET is missing.")

asks.init("trio")
session = Session(connections=8)
app = QuartTrio(__name__)


@app.route("/<token_a>/<token_b>", methods=["POST"])
async def webhook(token_a, token_b):
    request_data = await request.get_json(force=True)
    if ENABLE_DEBUG:
        print(f"Request data:\n{json.dumps(request_data, indent=2)}")
    target_url = f"{TARGET_URL}/{token_a}/{token_b}"
    response = await session.post(target_url, json=request_data)
    return Response(response.text, content_type=response.headers["content-type"])


if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)
