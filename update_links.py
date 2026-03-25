import os
import re

html_files = ["index.html", "about.html", "rooms.html", "gallery.html", "contact.html"]

nav_original = """<nav class="nav-links">
                <a href="#about">About</a>
                <a href="#experience">Experience</a>
                <a href="#why-us">Why Us</a>
                <a href="#gallery">Gallery</a>
                <a href="#location">Location</a>
                <a href="#contact" class="btn btn-primary btn-sm">Book Now</a>
            </nav>"""

nav_new = """<nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="about.html">About</a>
                <a href="rooms.html">Rooms</a>
                <a href="gallery.html">Gallery</a>
                <a href="contact.html">Contact Us</a>
                <a href="rooms.html#booking-form" class="btn btn-primary btn-sm">Book Now</a>
            </nav>"""

footer_original = """<div class="footer-links">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#experience">Accommodation</a></li>
                    <li><a href="#gallery">Gallery</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>"""

footer_new = """<div class="footer-links">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="rooms.html">Rooms</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </div>"""

for f in html_files:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Replace Nav and Footer
        content = content.replace(nav_original, nav_new)
        content = content.replace(footer_original, footer_new)
        
        # Replace inline CTAs
        content = content.replace('href="#contact" class="btn btn-primary"', 'href="rooms.html#booking-form" class="btn btn-primary"')
        content = content.replace('href="#contact" class="btn btn-secondary', 'href="contact.html" class="btn btn-secondary')
        
        # The navbar Book Now was changed explicitly.
        
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)

print("Nav and Footer updated manually in all files.")
