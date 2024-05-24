from datetime import datetime
from fastapi import FastAPI, BackgroundTasks

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="后台任务处理接口",
    description=description,
    version="0.0.1",
    contact={
        "name":"he",
        "url":"http://12.com"
    },
    license_info={
        "name":"Apache 3.0",
        "url":"https://xxxx"
    },
    # # docs_url="/documentation", 
    # docs_url=None,
)


def write_notification(email: str, message=""):
    with open("log.txt",mode="a+") as email_file:
        content = f"{datetime.today()} Notification for {email}: {message}\n"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_task: BackgroundTasks):
    background_task.add_task(write_notification, email, message="some notification.")
    return {"message":"Notification send in the background."}