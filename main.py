from youtube import *

def main():
  print("> Welcome to PyYouTubeDownloader, download youtube MP3/MP4 here!")
  choice = "yamete"
  
  while choice != "break":
    url = input("Input Youtube URL : ")
  
    if not meta_data(url):
      continue
    
    choice = input("Download [y/n] : ")
  
    if choice == 'y':
      choice = input("Format MP4/MP3 : ")
  
      if choice == "MP4":
        download_mp4(url)
      elif choice == "MP3":
        download_mp3(url)
        
    elif choice == 'n':
      continue
    elif choice == "break":
      break
    else:
      continue
      
main()