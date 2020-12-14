# Haugene-Mouse
This is a simple script to automatically download torrents from myanonamouse rss feeds.

It's ideally designed for using alongside the legendary Haugene torrent container: https://github.com/haugene/docker-transmission-openvpn since you can expose a proxy service on the container then and use it within the script for the downloads.

The script downloads the torrents on the rss feeds and adds them to your Transmission downloads folder as normal. However, it also copies the completed rss files to another folder of your choosing (rss_completed_path) since this makes it more convient imo to seperate your rss files from all the other torrents you add to Transmission.


