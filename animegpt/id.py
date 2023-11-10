import requests
import os
import csv
from dotenv import load_dotenv


   
parent_directory = parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
new_folder_path = os.path.join(parent_directory, 'data')

try:
    os.makedirs(new_folder_path)
except FileExistsError:
    print(f"Folder already exists at {new_folder_path}")


url_anime = 'https://api.myanimelist.net/v2/anime/ranking?ranking_type=bypopularity&limit=500}'

num_anime = 0

total_anime = 10000

filename = new_folder_path + '/id.csv'
load_dotenv()

MAL_ID = os.environ.get('mal_id')

while num_anime <= total_anime:
    anime_details = requests.get(url_anime, headers={'X-MAL-CLIENT-ID' : MAL_ID }).json()
    url_anime = anime_details['paging']['next']
    for entry in anime_details['data']:
        anime_title = entry['node']['title']
        anime_id = entry['node']['id']
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([anime_id, anime_title])
        num_anime += 1
    
            
        
        
        
        




