import requests
import random

def memer():
    url = "https://meme-api.com/gimme/ProgrammerHumor"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"Server didn't responded. {response.status_code}")
        return None

    data = response.json()
    meme = {
        "title": data.get('title'),
        "image": data.get('url')
    }

    return meme


    # OLD MEME
    # url = "https://www.reddit.com/r/ProgrammerHumor/top.json?limit=5&t=day"

    # headers = {
    #     "User-Agent": "NewFlaskapp/2.0"
    # }
    # response = requests.get(url, headers=headers)

    # data = response.json()
    # memes = []

    # for post in data["data"]["children"]:
    #     post_data = post["data"]

    #     post_hint = post_data.get("post_hint")
    #     url = post_data.get("url", "")

    #     is_image = (
    #         post_hint == "image"
    #         or url.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
    #     )

    #     if is_image:
    #         meme_data = {"title": post_data.get("title"), "image": url}
    #         memes.append(meme_data)


    # meme = random.choice(memes) if memes else None
