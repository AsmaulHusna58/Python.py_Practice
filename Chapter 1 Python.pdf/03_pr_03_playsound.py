from playsound3 import playsound

# Play sounds from disk
playsound("C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\Chapter 1 Python.pdf\\play.mp3")

'''
# or play sounds from the internet.
playsound("http://url/to/sound/file.mp3")

# You can play sounds in the background
sound = playsound("/path/to/sound/file.mp3", block=False)

# and check if they are still playing
if sound.is_alive():
    print("Sound is still playing!")

# and stop them whenever you like.
sound.stop()
'''