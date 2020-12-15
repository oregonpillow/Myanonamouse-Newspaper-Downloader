# Haugene-Mouse
This is a simple script to automatically download torrents from myanonamouse rss feeds. The most sensible use case would be for downloading periodicals or other frequently updated rss feeds.

It's ideally designed for using alongside the legendary Haugene torrent container: https://github.com/haugene/docker-transmission-openvpn since you can expose a proxy service on the container then use that proxy within the script http requests - ensuring that the rss feed is accessed from the same ip that Transmission uses.

### How it works
The script downloads the torrents from the rss feeds and adds them to your Transmission downloads folder as normal. However, it also copies the completed files to another folder of your choosing (rss_completed_path). The benefit of this is that it seperate your rss files from all the other torrents you have in Transmission downloads folder. This way, since i'm running the Haugene container on a server, i can conveniently rsync the rss_completed_path folder to my laptop while keeping any seeding torrents in the original Transmission downlods folder.


