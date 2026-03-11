import requests
from config import BOT_TOKEN, CHANNEL_ID


def send_photo(photo_path):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    with open(photo_path, "rb") as photo:
        requests.post(
            url,
            data={"chat_id": CHANNEL_ID},
            files={"photo": photo}
        )
