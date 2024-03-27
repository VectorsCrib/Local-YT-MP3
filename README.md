# Local-YT-MP3
Need a yt video converted to mp3 or other? Locally do so with the tool contained in this repo.

# When ```main.py``` is running paste this into your terminal, but change ```https://www.youtube.com/watch?v=xxxxx``` with the url of your video...
curl -X POST -F "url=https://www.youtube.com/watch?v=xxxxx" http://127.0.0.1:5000/download --output downloaded_video.mp3
# If it is not running. It wont download the youtube video as an mp3.




# Optional:
If you want to download to a specific folder, change the ```path = f"C:\\Users\\{user}\\Downloads\\"``` line to a different location.

Thank you!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-donate-yellow.svg)]([https://www.buymeacoffee.com/yourusername](https://www.buymeacoffee.com/kendallbak2))
