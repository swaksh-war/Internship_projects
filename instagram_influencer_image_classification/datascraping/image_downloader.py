import requests
import time
import pandas as pd
path_to_csv = input('Enter the csv file path that will download photos: ')
all_links = pd.read_csv(str(path_to_csv))
for link in all_links['links']:

    r = requests.get(link)

    with open("data/influencial/influencer"+str(time.time())+".png", 'wb') as f:
        f.write(r.content)
