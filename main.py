from fastapi import FastAPI, Request
from pytube import YouTube
from pytube import Playlist

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

    
@app.get("/{link:path}")
def read_item(link: str):
    #result = numinwords(num,lang='en_IN')
    yt = YouTube(link)
    name = yt.title
    preview = yt.thumbnail_url
    upload = yt.author
    #des = yt.description
    return {"title": name ,
           "thumbnail": preview,
           "uploaded" : upload,
    }