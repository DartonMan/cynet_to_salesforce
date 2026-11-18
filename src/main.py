from fastapi import FastAPI, Request
from pathlib import Path
import logging
import sys

LOG_FILE = "cynet.log"
LOG_DIR = "var/log"

root_dir = Path(__file__).resolve().parent

log_dir = root_dir / LOG_DIR
log_dir.mkdir(parents=True, exist_ok=True)

logfile = log_dir / LOG_FILE

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(logfile, mode="a"),
    ],
)

app = FastAPI()

@app.post("/webhook")
async def cynet_webhook(request: Request):
    body = await request.body()

    logging.debug(f"Headers: {dict(request.headers)}")
    logging.debug(f"Payload: {body.decode('utf-8')}")

    return {"status": "ok"}

#if __name__ == "__main__":
#    import uvicorn
#
#    uvicorn.run(
#        app,
#        host="0.0.0.0",
#        port=8000
#    )
