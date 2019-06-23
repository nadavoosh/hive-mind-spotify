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

async function unfollowPlaylist(url, playlistId) {
  let headers = {};
  headers = {
    Authorization: "Bearer " + accessToken,
    "Content-Type": "application/json"
  };

  let response = await fetch(`${url}/playlists/${playlistId}/followers`, {
    headers,
    method: "DELETE"
  });
  let data = await response.json();
  return data;
}

async function unfollow() {
  const url = await getUrlForUser();
//   const playlistId = JSON.parse(document.getElementById("playlist").dataset.playlistId);
  const playlist = await unfollowPlaylist(url, '1Dk0jmISrYpKtgS0VRZQiQ');
  await addTracksToPlaylist(playlist.href, uris.join(","));
}

unfollow();
