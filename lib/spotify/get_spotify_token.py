import spotipy
import spotipy.util as util


def (username):
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope)
    if token:
        return spotipy.Spotify(auth=token)
    else:
        print "Can't get token for", username
