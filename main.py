from email.message import EmailMessage

import aiosmtplib
import uvicorn
from envparse import env

from fastapi import Body, FastAPI
from pydantic import BaseModel
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

env.read_envfile()

GMAIL_USER = env.str('GMAIL_USER')
GMAIL_PASSWORD = env.str('GMAIL_PASSWORD')
HOST_NAME = env.str('HOST_NAME')
PORT = env.int('PORT')
FROM = env.str('FROM')
TO = env.str('TO')

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Mail(BaseModel):
    subject: str
    body: str


@app.post("/send-email")
async def send_email(mail: Mail = Body(None, embed=True)):
    message = EmailMessage()
    message["From"] = FROM
    message["To"] = TO
    message["Subject"] = mail.subject
    message.set_content(mail.body)

    await aiosmtplib.send(message,
                          hostname=HOST_NAME,
                          port=PORT,
                          start_tls=True,
                          username=GMAIL_USER,
                          password=GMAIL_PASSWORD)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={
        'result': True
    })


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
