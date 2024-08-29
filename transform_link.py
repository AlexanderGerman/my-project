def transform_link(link: str) -> str:

    if link.startswith("https://t.me/"):
        transformed_link = link.replace("https://t.me/", "https://t.me/s/")
        return transformed_link
    else:
        raise ValueError("Invalid Telegram link format.")
