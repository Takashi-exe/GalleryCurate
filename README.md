# Art Gallery Curator

A Flask-based web application that scrapes artwork from The Metropolitan Museum of Art's collection and curates a personalized gallery based on user search queries.

## Features
- Search for artworks by artist, style, or keyword.
- Scrape artwork details (title, image, style, year) from The Met's website.
- Store artworks in a SQLite database.
- Display curated artworks in a responsive gallery interface using Bootstrap.
- Respectful scraping with error handling and duplicate prevention.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/art-gallery-curator.git
   cd art-gallery-curator
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python run.py
   ```
4. Open `http://localhost:5000` in your browser.

## Usage
- On the home page, enter a search term (e.g., "Monet", "Impressionism").
- Click "Search" to scrape and display matching artworks.
- View the full gallery at `/gallery`.

## Notes
- The scraper respects The Met's terms of service by using appropriate headers and minimal requests.
- Consider using The Met's public API for production to avoid scraping issues.
- Images are sourced directly from The Met's website; ensure compliance with usage policies.

## Screenshots
(Include screenshots or a GIF of the app in action)

## License
MIT License