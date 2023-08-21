from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()
# 路径是相对于 main.py
file_path = "./file/dog.mp4"


async def fake_video_streamer():
    for i in range(100):
        yield b"some fake video bytes"


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())


@app.get("/video")
def video():
    def iter_file():
        with open(file_path, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iter_file(), media_type="video/mp4")
