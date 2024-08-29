import aiohttp
from bs4 import BeautifulSoup


async def fetch_channel_info(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()

            soup = BeautifulSoup(html, 'html.parser')

            title_tag = soup.find('span', {'dir': 'auto'})
            title = title_tag.text.strip() if title_tag else "Не найдено"

            description_tag = soup.find('div', {'class': 'tgme_channel_info_description'})
            description = description_tag.text.strip() if description_tag else "Не найдено"

            subscribers_tag = soup.find('span', {'class': 'counter_value'})
            subscribers_count = subscribers_tag.text.strip() if subscribers_tag else "Не найдено"

            return {
                'title': title,
                'description': description,
                'subscribers_count': subscribers_count
            }
