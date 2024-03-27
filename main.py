from flask import Flask, request, send_file
from pytube import YouTube
from moviepy.editor import *
import os
import getpass
 
user = getpass.getuser()
 
app = Flask(__name__)
path = f"C:\\Users\\{user}\\Downloads\\"
@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    if not url:
        return "URL is required", 400

    try:
        yt = YouTube(url)
        # Download video
        video_stream = yt.streams.filter(only_audio=True).first()
        download_path = path + video_stream.download()
        
        # Convert to MP3
        mp3_filename = download_path.split(".")[0] + ".mp3"
        video_clip = AudioFileClip(download_path)
        video_clip.write_audiofile(mp3_filename)
        video_clip.close()
        
        # Remove the original download
        os.remove(download_path)

        return send_file(mp3_filename, as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
