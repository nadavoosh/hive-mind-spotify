"use strict";
const baseSpotifyUri = "https://api.spotify.com/v1";
const secret = window.location.hash.substr(1);
const accessToken = secret.split("&")[0].split("=")[1];

async function spotifyRequest(url, method) {
  const headers = {
    Authorization: "Bearer " + accessToken,
    "Content-Type": "application/json"
  };
  if (!method) {
    method = "GET";
  }
  let response = await fetch(url, { headers });
  let data = await response.json();
  return data;
}

async function getUrlForUser() {
  const data = await spotifyRequest(`${baseSpotifyUri}/me`);
  return data.href;
}

async function createPlaylist(url, body) {
  let headers = {};
  headers = {
    Authorization: "Bearer " + accessToken,
    "Content-Type": "application/json"
  };

  let response = await fetch(`${url}/playlists`, {
    headers,
    method: "POST",
    body: JSON.stringify(body)
  });
  let data = await response.json();
  return data;
}

async function addTracksToPlaylist(playlistURL, trackArray) {
  let headers = {};
  headers = {
    Authorization: "Bearer " + accessToken,
    "Content-Type": "application/json"
  };

  var url = new URL(
    `${playlistURL}/tracks?uris=${encodeURIComponent(trackArray)}`
  );

  let response = await fetch(url, {
    headers,
    method: "POST"
  });
  let data = await response.json();
  return data;
}

async function buildPlaylists() {
  const url = await getUrlForUser();
  const playlistInfo = {
    name: "testing",
    public: false
  };
  const playlist = await createPlaylist(url, playlistInfo);
  console.log(playlist.href)
  const uris = JSON.parse(document.getElementById("uris").dataset.uris);
  console.log(uris)
  await addTracksToPlaylist(playlist.href, uris.join(","));
}

//   https://developer.spotify.com/documentation/web-api/reference/follow/unfollow-playlist/
buildPlaylists();
