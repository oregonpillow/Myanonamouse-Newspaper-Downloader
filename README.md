# Haugene-Mouse
This is a simple script to automatically download torrents from MyAnonamouse rss feeds. The most sensible use case would be for downloading periodicals or other frequently updated rss feeds.

It's ideally designed for using alongside legendary Haugene torrent container: https://github.com/haugene/docker-transmission-openvpn since you can expose a proxy service on the container then use that proxy within the script http requests - ensuring that the rss feed is accessed from the same ip that Transmission uses.

### How it works
The script downloads the torrents from the rss feeds and adds them to your Transmission downloads folder as normal. However, it also copies the completed files to another folder of your choosing (rss_completed_path). The benefit of this is that it seperates your rss files from all the other torrents you have in Transmission downloads folder. This way, since i'm running the Haugene container on a server, i can conveniently rsync the rss_completed_path folder to my laptop while keeping any seeding torrents in the original Transmission downlods folder.


### References
* @jcul https://github.com/jcul/bencode - script to easiely decode .torrent file and extract torrent file or torrent folder name

* @ Henry Koch https://www.henrykoch.de/en/python-remove-oldest-files-in-a-directory-only-a-defined-count-of-them-remains - Simple function to sort files in folder by date then keep only the most recent number. Used to prevent rss_completed_path becoming bloated over time with accumulating rss downloads. 
