import clipboard
import urllib.request, urllib.parse, urllib.error
import Image
import photos
import io

# Given an image URL in the clipboard, save the image to the iOS Camera Roll with Pythonista. Simple script with no error checks or other settings.

URL = clipboard.get()

file = Image.open(io.StringIO(urllib.request.urlopen(URL).read()))

photos.save_image(file)

print('Image Saved')

