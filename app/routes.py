from flask import Blueprint, render_template, request
from app.models import Artwork
from app.scraper import scrape_art
from app import models

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form.get('action')
        search = request.form.get('search', '')
        # Clear all artworks before repopulating
        models.Artwork.query.delete()
        models.db.session.commit()
        if action == 'randomize':
            from app.scraper import scrape_random_art
            scrape_random_art()
            return render_template('gallery.html', artworks=Artwork.query.all(), search='Random Selection')
        else:
            scrape_art(search)
            return render_template('gallery.html', artworks=Artwork.query.all(), search=search)
    return render_template('index.html')

@bp.route('/gallery')
def gallery():
    artworks = Artwork.query.all()
    return render_template('gallery.html', artworks=artworks)