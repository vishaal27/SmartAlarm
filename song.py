import pygame
import requests
import wget
import os
from bs4 import BeautifulSoup


def select_song():
    # This function will pass a search query to "https://archive.org/" and collect all the
    # search results. It, then asks user to choose a song from the search results.

    # It returns a list : [<an number>, <title of the song>, <link to the song>]

    query = input("Enter the name of the song : ")
    query_link = "https://archive.org/search.php?query=" + query + "&and[]=mediatype%3A\"audio\""
    try:
        r = requests.get(query_link)
    except:
        input("Network connection failed. Please try refreshing your connection.")
        exit()

    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("a")
    count = 1
    song_details = []
    current_song = []

    for link in links:
        title = link.get('title')
        address = link.get('href')

        try:
            if address[1] == 'd' and address[2] == 'e' and not "opensource" in address and not title == None:
                # The above written if statement is hardcoded wrt observations. It just works nicely.
                download_page = "https://archive.org" + address
                current_song.append(str(count))
                current_song.append(title)
                current_song.append(download_page)
                song_details.append(current_song)
                current_song = []
                count += 1
        except:
            pass

    for song in song_details:
        message = song[0] + '. ' + song[1]
        print(message)

    selected_song = input("I wish to download song number : ")
    song_selected = False

    for song in song_details:
        if song[0] == selected_song:
            selected_song = song
            song_selected = True

    if song_selected is False:
        print("Incorrect song number entered.")

    return selected_song


def fetch_download_url(url):
    # This function returns the exact download link to the song.

    try:
        r = requests.get(url)
    except:
        print("Could not download the song")
        exit()

    download_link_found = False
    download_link = ''
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("a")

    for link in links:
        add = link.get("href")
        try:
            length = len(add)
        except:
            pass

        try:
            if ".mp3" in add and "download/" in add:
                download_link = "https://archive.org" + add
                download_link_found = True
                break
        except:
            pass

    if download_link_found is False:
        print("Could not download the song")

    return download_link


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)  # setup mixer to avoid sound lag
    pygame.init()

    song = select_song()  # Select the song to play
    song_url = fetch_download_url(song[2])  # song[2] contains the url to the selected song.
    print("Downloading your song now..\n\n")

    file_name = wget.download(song_url)
    print("\nSong downloaded.. Playing..")

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play(-1)
        while pygame.mixer.music.get_busy():
          pygame.time.Clock().tick(10)

        os.remove(file_name)  # Delete the downloaded song file after playing the song
        print("You just heard your favourite song..")

    except KeyboardInterrupt:
        os.remove(file_name)  # Delete the downloaded song file before exit
