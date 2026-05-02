import pandas as pd
import requests
import os
import time

df = pd.read_csv('galaxy_truth_table.csv')

# Between 0.4 to 0.6 means split in vote: 
# Closer to 0 indicates features (e.g., disks, spiral arms, etc)
# Closer to 1 indicates smoothness

uncertain_classifications = df[df['t01_smooth_or_features_a01_smooth_debiased'].between(0.4, 0.6)]

sample = uncertain_classifications.sample(1500)

output_dir = 'galaxyZoo2Images'
os.makedirs(output_dir, exist_ok=True)

# Galaxy 2 images are from the sdss 
base_url = "https://skyserver.sdss.org/dr18/SkyServerWS/ImgCutout/getjpeg"

for index, row in sample.iterrows():
    params = {
        'ra': row['ra'],
        'dec': row['dec'],
        'width': 424,
        'height': 424,
        'scale': 0.4
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            file_path = os.path.join(output_dir, f"galaxy_{index}.jpg")
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else: 
            print(f"Failed for galaxy_{index}.jpg: Status {response.status_code}")
    except Exception as e:
        print(f"Error at index {index}: {e}")

    time.sleep(0.2) 

print("Done! Check your ''galaxyZoo2Images'' folder.") #Just for confirmation for me 
    