
# # import random
# import urllib.request
# def download_image_url(url):
# 	# name=random.randrange(1,1000)
# 	full_name='mungda'+'.jpg'
# 	urllib.request.urlretrieve(url,full_name)
# download_image_url('https://a10.gaanacdn.com/images/song/73/25433873/crop_175x175_1549281585.jpg')


#-----------------------------------------------------

import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

path = "mungda.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()
