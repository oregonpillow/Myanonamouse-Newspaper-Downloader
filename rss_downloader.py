import csv
import requests
import xml.etree.ElementTree as ET
import os
import shutil
import time
import bencode
from multiprocessing.pool import ThreadPool

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

'''

*** Nothing else to change below this line ***

'''



def rss_downloader(url):
	'''
	Parses rss feeds from myanonamouse.net and downloads the most recent files .
			Parameters:
					url (str): url of rss feed
			Returns:
					None
	'''
	latest_files = 10 #latest_files (int): number of most recent torrents to download from the rss feed

	rss_get=requests.get(url,proxies=proxies)
	xml=rss_get.text

	root = ET.fromstring(xml)
	titles = []
	for title in root.findall('./channel/item/title'):
		titles.append(title.text)

	links = []
	for link in root.findall('./channel/item/link'):
		links.append(link.text)

	titles = titles[:latest_files]
	links = links[:latest_files]

	results_dict = dict(zip(titles, links))

	for title in results_dict:
		#parse the file name from torrent file
		torrent_get=requests.get(results_dict[title],proxies=proxies, stream=True)
		torrent_content = bencode.decode(torrent_get.content)
		torrent_file_name = (torrent_content[0][b'info'][b'name']).decode('utf-8')

		#concatinate paths
		transmission_completed_file = transmission_completed_path + torrent_file_name
		torrent_file_name = transmission_watch_path + title + '.torrent'
		successful_move_path = rss_completed_path + torrent_file_name

		#main logic. Moves files to rss_completed_path or downloads file if missing. 
		if os.path.isfile(transmission_completed_file):
			if os.path.isfile(successful_move_path):
				continue
			else:
				shutil.copy(transmission_completed_file, rss_completed_path)
		else:
			print(f'Downloading: {title}')
			torrent_get=requests.get(results_dict[title],proxies=proxies, stream=True)
			file = open(torrent_file_name, "wb")
			file.write(torrent_get.content)
			file.close()
			while os.path.isfile(transmission_completed_file) == False:
				time.sleep(1)
				if os.path.isfile(transmission_completed_file):
					break
				if os.path.isdir(transmission_completed_file):
					break
			if os.path.isfile(transmission_completed_file):
				if os.path.isfile(successful_move_path):
					continue
				else:
					shutil.copy(transmission_completed_file, rss_completed_path)



def cleanup(path, max_files):
	'''
	credit to Henry Koch
	https://www.henrykoch.de/en/python-remove-oldest-files-in-a-directory-only-a-defined-count-of-them-remains
	Simple function to sort files in folder by date then keep only the most recent number of <max_files>.
	Prevents a folder getting too bloated.
			Parameters:
					path (str): path of folder to cleanup
					max_files (int): number of most recent files to keep
			Returns:
					None
	'''
	
	def sorted_ls(path=path, max_files=max_files):
		mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
		return list(sorted(os.listdir(path), key=mtime))
 
	del_list = sorted_ls()[0:(len(sorted_ls(path))-max_files)]
	for dfile in del_list:
		os.remove(path + '/' + dfile)




if __name__ == "__main__":
	threads = len(rss_feeds)
	for i in ThreadPool(threads).imap_unordered(rss_downloader, rss_feeds):
		pass
	print('--- Downloads Complete ---')
	print('Running cleanup...')
	cleanup(rss_completed_path,30) #optional
	print('Done.')
