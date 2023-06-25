import aiohttp
import asyncio

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_data = await response.read()
            return image_data

image_urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    'https://example.com/image3.jpg',

]

async def download_images(image_urls):
    tasks = []
    for url in image_urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)
    images = await asyncio.gather(*tasks)
    return images

loop = asyncio.get_event_loop()
downloaded_images = loop.run_until_complete(download_images(image_urls))
print(downloaded_images)
