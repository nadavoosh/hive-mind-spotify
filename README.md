# hive-mind-spotify

This small webserver takes an [AskMetaFilter](ask.metafilter.com) URL as an input, parses the responses to try to identify song recommendations, and searches spotify for those recommendations. 

The result is a spotify playlist generated by the OP. When the question was actually about songs, this ususally produces a playlist of the right flavor. When the question was about something else entirely, the playlist is too. 

# Running locally
You need to have a youtube API key (you can gneerate one [here](https://console.developers.google.com/apis/dashboard)). Then:
```
export YOUTUBE_API_KEY=<your-key>
make install-deps
python main/__init__.py
```
