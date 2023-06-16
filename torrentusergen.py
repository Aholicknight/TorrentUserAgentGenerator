import requests
from bs4 import BeautifulSoup
import random
import string

# Function to generate a random alphanumeric string of given length
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to get the latest version number from the website
def get_latest_version():
    # URL of the qBittorrent download page
    url = "https://www.qbittorrent.org/download"

    print("Going on", url)

    # Send a GET request to the page
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the latest version number
    latest_version_tag = soup.select_one("p.releaseParagraph strong a")
    latest_version = latest_version_tag.get_text().split("v")[1]

    return latest_version

# Prompt the user for version selection
def prompt_version_selection():
    print("qBittorrent torrent user agent generator")
    print("=======================================")
    print("This script will generate a torrent user agent for use with Tixati or any other torrent client that lets you spoof your user agent.")
    print("The user agent will be generated based on the latest version of qBittorrent available on the download page.")
    print("The script will also generate a random 12 length peer ID and an xfer_peerid.")
    print("=======================================")
    print("")
    print("1: Use the latest version of qBittorrent")
    print("2: Select an older version of qBittorrent")

    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            return get_latest_version()
        elif choice == "2":
            return select_older_version()
        else:
            print("Invalid choice. Please try again.")

# Select an older version from v3.0.0 to v4.5.2
def select_older_version():
    while True:
        version = input("Enter the version number (v3.0.0 to v4.5.2): ")
        if version >= "3.0.0" and version <= "4.5.2":
            return version
        else:
            print("Invalid version. Please try again.")

# Main program
def main():
    # Prompt version selection
    version_number = prompt_version_selection()

    # If the version is newer than v4.5.2, print "Current version number" instead of "Selected version number"
    if version_number > "4.5.2":
        print("Current version number:", version_number)

        # Ask the user to press enter to continue
        #input("Press enter to continue generating the user agent")
    
    # Remove the message "Current version number" if the version is v4.5.2 or older
    else:
        print("Selected version number:", version_number)

        # Ask the user to press enter to continue
        input("Press enter to continue generating the user agent")

    # Generate the torrent user agent
    user_agent = f"qBittorrent/{version_number}"

    # Generate the peer ID
    peer_id_prefix = f"-qB{version_number.replace('.', '')}0-"
    peer_id = peer_id_prefix + generate_random_string(11) + "0"

    # Generate the xfer_peerid
    xfer_peer_id = peer_id

    # Print the result
    print(f"header:%0D%0AUser-Agent: {user_agent}")
    print(f"peerid:{peer_id}")
    print(f"xfer_peerid:{xfer_peer_id}")

    # Wait for user input to exit
    input("Press enter to exit")

# Run the main program
if __name__ == "__main__":
    main()
