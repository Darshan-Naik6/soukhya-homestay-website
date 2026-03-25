import os

files = ['index.html', 'about.html', 'rooms.html', 'gallery.html', 'contact.html']

for fn in files:
    if not os.path.exists(fn): continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fixed logo replacement
    content = content.replace('logo.jpg', 'soukhya_logo.jpeg')
    
    # Missing hero / background / gallery replacements
    content = content.replace('balcony.jpeg', 'about.png')
    content = content.replace('river1.jpeg', 'river.png')
    content = content.replace('sideView.jpeg', 'darshan_image.jpeg')
    content = content.replace('coupleRoom2.jpeg', 'village.png')

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Images replaced across HTML files.")
