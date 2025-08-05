import requests
from bs4 import BeautifulSoup
from app import db
from app.models import Artwork
import random

def catch_error(func, default="N/A"):
    try:
        return func()
    except (AttributeError, TypeError, IndexError):
        return default

def scrape_art(search=""):
    if search:
        search = search.replace(" ", "+")
        url = f"https://www.metmuseum.org/art/collection/search?q={search}"
    else:
        url = "https://www.metmuseum.org/art/collection/search"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        art_items = soup.find_all('figure', class_='collection-object_collectionObject__SuPct')
        artworks = []

        for art in art_items:
            img_url = catch_error(lambda: art.find('img', class_='collection-object_image__XVQPm collection-object_gridView__8kZLF')['src'])
            title = catch_error(lambda: art.find('div', class_='collection-object_title__1MnJJ').text)
            style = catch_error(lambda: art.find('div', class_='collection-object_culture__BaSXn').text)
            year = catch_error(lambda: art.find('div', class_='collection-object_body__cW9co').find_all('div')[1].text)

            # Check if artwork already exists to avoid duplicates
            existing = Artwork.query.filter_by(title=title, image_url=img_url).first()
            if not existing:
                artwork = Artwork(
                    title=title,
                    image_url=img_url,
                    style=style,
                    year=year
                )
                db.session.add(artwork)
                artworks.append(artwork)

        db.session.commit()
        return artworks

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def scrape_random_art():
    # Fetch the first page of the collection and shuffle the results for randomness
    url = "https://www.metmuseum.org/art/collection/search"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        art_items = soup.find_all('figure', class_='collection-object_collectionObject__SuPct')
        artworks = []
        random.shuffle(art_items)
        for art in art_items[:12]:  # Limit to 12 random artworks
            img_url = catch_error(lambda: art.find('img', class_='collection-object_image__XVQPm collection-object_gridView__8kZLF')['src'])
            title = catch_error(lambda: art.find('div', class_='collection-object_title__1MnJJ').text)
            style = catch_error(lambda: art.find('div', class_='collection-object_culture__BaSXn').text)
            year = catch_error(lambda: art.find('div', class_='collection-object_body__cW9co').find_all('div')[1].text)
            existing = Artwork.query.filter_by(title=title, image_url=img_url).first()
            if not existing:
                artwork = Artwork(
                    title=title,
                    image_url=img_url,
                    style=style,
                    year=year
                )
                db.session.add(artwork)
                artworks.append(artwork)
        db.session.commit()
        return artworks
    except Exception as e:
        return []
