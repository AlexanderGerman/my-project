import asyncio
from transform_link import transform_link
from fetch_channel_info import fetch_channel_info


async def main():
    link = "https://t.me/yandex"
    transformed_link = transform_link(link)

    channel_info = await fetch_channel_info(transformed_link)

    print(f"Название канала: {channel_info['title']}")
    print(f"Описание канала: {channel_info['description']}")
    print(f"Количество подписчиков: {channel_info['subscribers_count']}")


if __name__ == "__main__":
    asyncio.run(main())
