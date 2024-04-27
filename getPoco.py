import requests
from bs4 import BeautifulSoup

# Start a session
session = requests.Session()

# Initial URL to connect
url1 = 'https://poco.is.tue.mpg.de/'
# URL to navigate to after initial connection
url2 = 'https://poco.is.tue.mpg.de/download.php'
# Final URL from where to download the file
download_url = 'https://download.is.tue.mpg.de/download.php?domain=poco&resume=1&sfile=data.zip'

# Access the initial URL
response1 = session.get(url1)
if response1.status_code != 200:
    print("Failed to connect to initial URL")
    exit()

# Optionally process the page
# soup1 = BeautifulSoup(response1.text, 'html.parser')

# Access the second URL
response2 = session.get(url2)
if response2.status_code != 200:
    print("Failed to navigate to download page")
    exit()

# Download the file
download_response = session.get(download_url)
if download_response.status_code == 200:
    with open('downloaded_file.zip', 'wb') as f:
        f.write(download_response.content)
    print("File downloaded successfully!")
else:
    print("Failed to download the file. Status code:", download_response.status_code)
