# This is a Pythonista script that will download an image, given its URL, and place that
# into the clipboard.
#
# So: from Image URL in clipboard to actual Image in clipboard.
#
# (c) 2014 Dexter Ang. MIT License.
#

import clipboard
import urllib.request, urllib.error, urllib.parse
import webbrowser
from io import StringIO
from PIL import Image

img_download = urllib.request.urlopen(clipboard.get())
img_string = StringIO(img_download.read())
img = Image.open(img_string)
clipboard.set_image(img)

