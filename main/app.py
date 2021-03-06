import logging
import os
import re
import sys
import requests
from flask import Flask, request, render_template, redirect, url_for
sys.path.append(os.path.abspath("."))
from lib.ask_me.question_model import AskMetafilterQuestion, BASE_ASKME_URL, RANDOM_ASKME_URL, ASKME_URL_PATTERN
from lib.spotify.connection import SpotifyConnection
from lib.spotify.playlist import SpotifyPlaylist
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
sp = SpotifyConnection(
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET
)


@app.route('/')
def question_input():
    return render_template('home.html')


@app.route('/songs/<int:ask_me_id>')
def get_recs(ask_me_id):
    url = BASE_ASKME_URL.format(ask_me_id)
    try:
        logger.debug('Identified AskMeId %s', ask_me_id)
        q = AskMetafilterQuestion(url)
    except IndexError:
        logger.warn(
            'Got an IndexError for AskMeId %s, which is expected for AskMe URLs that are no longer valid.',
            ask_me_id)
        return render_template('missing.html', url=url)

    tracks = sp.get_tracks_from_recommendations(q.get_recommendations())
    logger.debug('Creating playlist with %s tracks from url', (tracks))
    srclink = SpotifyPlaylist(q.alphanumeric_posttitle, tracks).embed_link
    return render_template(
        'recs.html',
        items=tracks,
        question=q,
        srclink=srclink)


@app.route('/search', methods=['POST'])
def hit_button():
    _url = request.form['ask_me_url'].lower()
    logger.debug('got URL input: %s', _url)
    # check if we were given an ask metafilter question
    url_match = re.match(ASKME_URL_PATTERN, _url)
    if not url_match:
        logger.warn('Got a non-askmetafilter URL: %s', _url)
        return render_template(
            'sorry.html',
            url=_url,
            sample_url=requests.get(RANDOM_ASKME_URL).url)
    ask_me_id = url_match.group(3)
    return redirect(url_for('get_recs', ask_me_id=ask_me_id))
