# Haugene-Mouse

![image](readme_image_ignore.jpg)This is a simple script to automatically download torrents from MyAnonamouse rss feeds. The most sensible use case would be for downloading periodicals or other frequently updated rss feeds.

It's ideally designed for using alongside legendary [Haugene torrent container](https://registry.hub.docker.com/r/haugene/transmission-openvpn) since you can expose a proxy service on the container then use that proxy within the script http requests - ensuring that the rss feed is accessed from the same ip that Transmission uses.

### How it works
The script downloads the torrents from the rss feeds and adds them to your Transmission downloads folder as normal. However, it also copies the completed files to another folder of your choosing (rss_completed_path). The benefit of this is that it seperates your rss files from all the other torrents you have in Transmission downloads folder. This way, since i'm running the Haugene container on a server, i can conveniently rsync the rss_completed_path folder to my laptop while keeping any seeding torrents in the original Transmission downloads folder.




## Requirements
* Requires Python3
* No additional packages needed

## Running the script

``` r
git clone https://github.com/oregonpillow/Haugene-Mouse.git
```

### 1. Modify the setup parameters in rss_downloader.py:

``` r
#Set up parameters
proxies = {
'http': '<ip>:<port>',
'https': '<ip>:<port>'
}

transmission_completed_path = '<path>' #transmission's completed download folder
transmission_watch_path = '<path>' #transmission's monitored/watched downloads fodler
rss_completed_path = '<path>' #path to where successfully downloaded rss torrents should be copied to

rss_feeds = [
'<feed url>', #rss_feed1
'<feed url>', #rss_feed2
'<feed url>', #rss_feed3
]

```

### 2. Additionally, you can modify:

* 2.1 [latest_files (int)](https://github.com/oregonpillow/Haugene-Mouse/blob/main/rss_downloader.py#L42):
``` r
latest_files = 10
```
sets how many of the most recent files on the rss feed you want to download. Useful if you only want to download the most recent files each time.


* 2.2 [cleanup (int)](https://github.com/oregonpillow/Haugene-Mouse/blob/main/rss_downloader.py#L128):
``` r
cleanup(rss_completed_path,30)
```
sets how many files can live in your rss_completed_path folder. Helps prevent the folder becoming bloated over time. A sensible upper limit would be:
latest_files * len(rss_feeds) since this insures that all files you want to download can fit in the download folder. But setting to smaller number is fine if you want to limit how many files you keep there at any given time.


### 3. Run the script using python

``` r
python rss_downloader.py
```

### References
* @jcul https://github.com/jcul/bencode - script to easiely decode .torrent file and extract torrent file or torrent folder name

* @ Henry Koch https://www.henrykoch.de/en/python-remove-oldest-files-in-a-directory-only-a-defined-count-of-them-remains - Simple function to sort files in folder by date then keep only the most recent number. Used to prevent rss_completed_path becoming bloated over time with accumulating rss downloads. 
