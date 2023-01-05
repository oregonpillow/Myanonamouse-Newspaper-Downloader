import yaml
import os


class AnonamouseDownloader():

    def __init__(self):

        # read config
        with open("rss_config.yml", "r") as config:
            self.config = yaml.safe_load(config)

        # load torrent guids already downloaded
        guid_file = self.config['guid_path']
        if not os.path.exists(guid_file):
            with open(guid_file, 'w'): pass

        with open(guid_file) as f:
            content = f.readlines()
            guids_lst = [x.rstrip() for x in content]
            print(len(guids_lst))

        # make saved data folders
        for feed in self.config['rss_feeds']:
            save_path = os.path.join(self.config['copy_path'], feed.split(':')[-1])
            if not os.path.exists(save_path):
                os.makedirs(save_path)


        self.downloader()

    #def path_validator(self):
    #    pdf_fpath = os.path.join(self.config['completed_path'], self.pdf_fname)
    #    torrent_fname = os.path.join(self.config['watch_path'], self.pdf_fname) + '.torrent'
    #    paper_fpath = rss_feeds[url] + pdf_fname



    def get_request(self, url)

        """
        Construct request for an rss url
        """

        if (self.config['proxy_host'] and self.config['proxy_port']):
            prox = f"{self.config['proxy_host']}:{self.config['proxy_port']}"
            proxies = {'http': prox, 'https': prox}
            if (self.config['proxy_user'] and self.config['proxy_pass']):
                auth = HTTPProxyAuth(self.config['proxy_user'], self.config['proxy_pass'])
                rss_get = requests.get(url, proxies=proxies, auth=auth)
            else:
                rss_get = requests.get(url, proxies=proxies)
        else:
            rss_get = requests.get(url)
            
        return rss_get



    def downloader(self, url=None):
        """


        "




        '''
        rss_get       = requests.get(url,proxies=proxies)




        xml           = rss_get.text
        root          = ET.fromstring(xml)
        new_links     = []
        items         = root.findall('./channel/item')[:latest_issues]
        for item in items:
            guid  = item.find('guid').text.split('/t/')[-1]
            if guid in guids_lst:
                continue
            else:
                guids_lst.append(guid)
                a = open(guids, 'w')
                for i in guids_lst:
                    a.write(i + "\n")
                a.close()
            title = item.find('title').text
            link  = item.find('link').text
            new_links.append(link)
        '''






AnonamouseDownloader()