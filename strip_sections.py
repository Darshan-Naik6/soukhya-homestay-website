import os

files_to_remove = {
    'rooms.html': ['about ', 'experience ', 'why-us ', 'gallery ', 'location '],
    'gallery.html': ['about ', 'experience ', 'rooms ', 'why-us ', 'location '],
    'contact.html': ['about ', 'experience ', 'rooms ', 'why-us ', 'gallery ']
}

for filename, sections in files_to_remove.items():
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for sec in sections:
        start_idx = content.find(f'<section class="{sec}')
        if start_idx == -1:
            continue
            
        # Find preceding comment
        comment_start = content.rfind('<!--', 0, start_idx)
        if comment_start != -1 and (start_idx - comment_start) < 100:
            start_idx = comment_start
            
        # Also remove preceding whitespace
        while start_idx > 0 and content[start_idx-1] in [' ', '\t', '\n', '\r']:
            start_idx -= 1
            
        end_idx = content.find('</section>', start_idx)
        if end_idx != -1:
            end_idx += 10 # length of </section>
            content = content[:start_idx] + content[end_idx:]
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sections successfully removed from rooms.html, gallery.html, and contact.html.")
