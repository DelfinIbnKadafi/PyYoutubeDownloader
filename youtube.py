import yt_dlp

def meta_data(url):
  ydl_opts = {
   "quiet": True,
   "no_warnings": True
  }
  
  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(url, download=False)

    print("Title    :", info.get("title"))
    print("Uploader :", info.get("uploader"))
    print("Views    :", info.get("view_count"))
    print("Duration :", info.get("duration"), "seconds") 
    return True
  
  except yt_dlp.utils.DownloadError as e:
    print("Failed to get youtube vidio information.")
    print("Error:", e)
    return False

def download_mp4(url):
  ydl_opts = {
   'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
   'quiet': True,
   'no_warnings': True,
   'outtmpl': 'downloads/%(title)s.%(ext)s'
  }
    
  print("Downloading...")
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print("Succesfully Download File!")

def download_mp3(url):
  ydl_opts = {
   'format': 'bestaudio/best',
   'quiet': True,
   'no_warnings': True,
   'outtmpl': 'downloads/%(title)s.%(ext)s',
   'postprocessors': [
     {
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192'
     }
   ]
  }

  print("Downloading...")
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print("Succesfully Download File!")