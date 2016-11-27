# hive-mind-spotify

This small webserver takes an [AskMetaFilter](ask.metafilter.com) URL as an input, parses the responses to try to identify song recommendations, and searches spotify for those recommendations. 

The result is a spotify playlist generated by the OP. When the question was actually about songs, this ususally produces a playlist of the right flavor. When the question was about something else entirely, the playlist is too. 

# Running locally
`make install-deps` to install the required python packages. You also need to have a youtube API key (you can gneerate one [here](https://console.developers.google.com/apis/dashboard)). Set it with `export YOUTUBE_API_KEY=<your-key>`
Then just run
```
python main/__init__.py
``` 
to start the local flask server. 
