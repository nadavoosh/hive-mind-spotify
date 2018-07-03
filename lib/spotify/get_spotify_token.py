import spotipy
import spotipy.util as util


def get_token(username):
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope)
    if token:
        return spotipy.Spotify(auth=token)
    else:
        print "Can't get token for", username

# https://github.com/drshrey/spotify-flask-auth-example/blob/master/main.py