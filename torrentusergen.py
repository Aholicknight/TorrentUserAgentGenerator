import requests
from bs4 import BeautifulSoup
import random
import string

# Function to generate a random alphanumeric string of given length
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# URL of the qBittorrent download page
url = "https://www.qbittorrent.org/download"

print("qBittorrent torrent user agent generator")
print("=======================================")
print("This script will generate a torrent user agent for use with Tixati or any other torrent client that lets you spoof your user agent.")
print("The user agent will be generated based on the latest version of qBittorrent available on the download page.")
print("The script will also generate a random 12 length peer ID and an xfer_peerid.")
print("=======================================")
print("")
input("To continue with the generation, press enter. To exit, press CTRL+C.")
print("Connecting to", url)

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful (HTTP 200 OK) and exit if not
if response.status_code != 200:
    print("Cannot connect to qBittorrent download page:", response.status_code)
    exit()

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the latest version number
latest_version_tag = soup.select_one("p.releaseParagraph strong a")
latest_version = latest_version_tag.get_text().split("v")[1]

# Display the latest version number
print("Latest version number:", latest_version)

# Generate the torrent user agent
user_agent = f"qBittorrent/{latest_version}"

# Generate the peer ID
peer_id_prefix = f"-qB{latest_version.replace('.', '')}0-"
peer_id = peer_id_prefix + generate_random_string(11) + "0"

# Generate the xfer_peerid
xfer_peer_id = peer_id

# Print the result
print(f"header:%0D%0AUser-Agent: {user_agent}")
print(f"peerid:{peer_id}")
print(f"xfer_peerid:{xfer_peer_id}")

# Wait for user input to exit
input("Press enter to exit")
