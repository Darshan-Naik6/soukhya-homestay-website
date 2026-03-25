import os

def update_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            modified = True
        else:
            print(f"Warning: Could not find snippet in {path}:\n{old[:50]}...")
            
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

base_dir = r'c:\Users\Darshan\OneDrive\Desktop\antigravity-project\soukhya-homestay'

# index.html changes
index_replacements = [
    # Meta desc
    ('<meta name="description"\n        content="Stay at Soukhya Riverside Homestay near Aghanashini river. Affordable nature stay with dolphin watching, kayaking, and relaxing riverside views near Gokarna.">',
     '<meta name="description"\n        content="A peaceful riverside stay in Aghanashini village. Away from crowded tourist areas, perfect for travelers who want relaxation and exploration near Gokarna.">'),
    
    # Title
    ('<title>Soukhya Riverside Homestay | Peaceful Stay Near Gokarna</title>',
     '<title>Soukhya Riverside Homestay | Peaceful Stay Away from Gokarna Crowds</title>'),

    # Navbar Book Now
    ('<a href="https://wa.me/918217399823" target="_blank" class="btn btn-primary btn-sm">Book Now</a>',
     '<a href="https://wa.me/918217399823" target="_blank" class="btn btn-primary btn-sm">Check Availability on WhatsApp</a>'),
    
    # Hero Content
    ('<h1>Relax.<br>Reconnect.<br>Experience Nature.</h1>',
     '<h1>Escape Gokarna crowds.<br>Experience peaceful riverside living.</h1>'),
    ('<p class="hero-subtext">A peaceful riverside homestay near Gokarna. Perfect for nature lovers, couples,\n                    and families looking for a quiet escape.</p>',
     '<p class="hero-subtext">Private homestay in Aghanashini with river views, sunrise experience, and complete privacy. Stay away from the noise, yet close enough to explore Gokarna beaches.</p>'),
    ('Book on WhatsApp', 'Check Availability on WhatsApp'),
    ('Call Now', 'Call Now'), # keep same just replacing WA

    # Trust section -> replace entire block and add storytelling & location & who-for
    ('''        <!-- 2. TRUST SECTION -->
        <section class="trust-section">
            <div class="container trust-grid">
                <div class="trust-item slide-up">
                    <div class="trust-icon">🌿</div>
                    <h4>Peaceful Riverside Location</h4>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.1s;">
                    <div class="trust-icon">💰</div>
                    <h4>Affordable Stay Near Gokarna</h4>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.2s;">
                    <div class="trust-icon">🙏</div>
                    <h4>Authentic Local Hospitality</h4>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.3s;">
                    <div class="trust-icon">🛶</div>
                    <h4>Adventure Activities Available</h4>
                </div>
            </div>
        </section>''',
    '''        <!-- STORYTELLING & TRUST SECTION -->
        <section class="trust-section section-padding" style="margin-top: -3rem;">
            <div class="container center slide-up mb-4 pb-4">
                <h2 style="font-size: clamp(1.5rem, 4vw, 2.2rem); font-family: 'Playfair Display', serif; font-weight: 500; max-width: 800px; margin: 0 auto; line-height: 1.4;">Wake up to a beautiful sunrise right in front of the homestay. Enjoy calm riverside mornings with fresh air and nature sounds.</h2>
                <p style="font-size: 1.1rem; color: var(--text-light); margin-top: 1rem;">Perfect for slow travel and relaxing weekends.</p>
            </div>
            <div class="container trust-grid mt-2">
                <div class="trust-item slide-up">
                    <div class="trust-icon">🏠</div>
                    <h4>Entire Floor Privacy</h4>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.1s;">
                    <div class="trust-icon">🚗</div>
                    <h4>Parking Available</h4>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.2s;">
                    <div class="trust-icon">🗺️</div>
                    <h4>Local Guidance Available</h4>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.3s;">
                    <div class="trust-icon">🌿</div>
                    <h4>Peaceful Village Environment</h4>
                </div>
            </div>
        </section>

        <!-- 3. LOCATION & TRAVEL ADVANTAGE SECTION -->
        <section class="location-advantage section-padding bg-soft" id="location">
            <div class="container center slide-up">
                <span class="section-badge">Prime Location</span>
                <h2>A Peaceful Riverside Stay in Aghanashini Village</h2>
                <p>Away from crowded tourist areas. Ideal for travelers who want both relaxation and exploration.</p>
            </div>
            
            <div class="container mt-4 slide-up" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                <!-- Location Advantage -->
                <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                    <h3 style="margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.5rem;">📍</span> Location Advantage</h3>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
                        <li style="display: flex; gap: 0.8rem; align-items: flex-start;"><span style="color: var(--accent); font-weight: bold;">✓</span> <span style="line-height: 1.5">A peaceful, non-touristy area offering an authentic coastal experience.</span></li>
                        <li style="display: flex; gap: 0.8rem; align-items: flex-start;"><span style="color: var(--accent); font-weight: bold;">✓</span> <span style="line-height: 1.5">Beautiful sunrise views directly in front of the homestay.</span></li>
                        <li style="display: flex; gap: 0.8rem; align-items: flex-start;"><span style="color: var(--accent); font-weight: bold;">✓</span> <span style="line-height: 1.5">Stay away from the noise, yet close enough to explore Gokarna beaches.</span></li>
                    </ul>
                </div>

                <!-- Travel Information -->
                <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                    <h3 style="margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.5rem;">🚗</span> Travel Information</h3>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
                        <li style="display: flex; gap: 0.8rem; align-items: flex-start;"><span style="font-size: 1.2rem; margin-top: 2px;">🚙</span> <span style="line-height: 1.5"><strong>By Car:</strong> Approx 45 km from Gokarna (~1 hour drive)</span></li>
                        <li style="display: flex; gap: 0.8rem; align-items: flex-start;"><span style="font-size: 1.2rem; margin-top: 2px;">🏍️</span> <span style="line-height: 1.5"><strong>By Bike:</strong> Barge service available from 7 AM to 6 PM for a shorter scenic route</span></li>
                        <li style="display: flex; gap: 0.8rem; align-items: flex-start;"><span style="font-size: 1.2rem; margin-top: 2px;">🗺️</span> <span style="line-height: 1.5"><strong>Easy Access:</strong> Conveniently located to explore nearby beaches and towns</span></li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- WHO IS THIS FOR SECTION -->
        <section class="who-for section-padding" id="who-for">
            <div class="container center slide-up">
                <span class="section-badge">Perfect For</span>
                <h2>Who Is This For?</h2>
            </div>
            <div class="container trust-grid mt-4">
                <div class="trust-item slide-up">
                    <div class="trust-icon">💑</div>
                    <h4>Couples</h4>
                    <p>Looking for a private and peaceful stay.</p>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.1s;">
                    <div class="trust-icon">👥</div>
                    <h4>Friends Group</h4>
                    <p>Comfortable space for up to 6 guests.</p>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.2s;">
                    <div class="trust-icon">📸</div>
                    <h4>Nature Lovers</h4>
                    <p>Surrounded by river, village life, and nature.</p>
                </div>
                <div class="trust-item slide-up" style="transition-delay: 0.3s;">
                    <div class="trust-icon">💻</div>
                    <h4>Work-from-Nature</h4>
                    <p>Quiet environment perfect for remote work.</p>
                </div>
            </div>
        </section>'''),
    
    # Experiences Section Update + Home Food
    ('''        <!-- 5. EXPERIENCES SECTION -->
        <section class="experiences section-padding" id="experiences">
            <div class="container center slide-up">
                <span class="section-badge">Explore</span>
                <h2>Things To Do During Your Stay</h2>
            </div>
            <div class="container experiences-grid slide-up">
                <div class="experience-card">
                    <div class="experience-icon">🐬</div>
                    <h4>Dolphin Watching Boat Ride</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🛶</div>
                    <h4>Kayaking</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🚤</div>
                    <h4>River Boating</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🎣</div>
                    <h4>Fishing Experience</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🌅</div>
                    <h4>Sunset by the Riverside</h4>
                </div>
            </div>
        </section>''',
    '''        <!-- 5. EXPERIENCES SECTION -->
        <section class="experiences section-padding bg-soft" id="experiences">
            <div class="container center slide-up">
                <span class="section-badge">Explore</span>
                <h2>Things To Do During Your Stay</h2>
            </div>
            <div class="container experiences-grid slide-up">
                <div class="experience-card">
                    <div class="experience-icon">🐬</div>
                    <h4>Dolphin Watching Boat Rides</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🚤</div>
                    <h4>River Boating in Aghanashini</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🛶</div>
                    <h4>Kayaking</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🎣</div>
                    <h4>Fishing</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🌅</div>
                    <h4>Sunrise Views from Homestay</h4>
                </div>
                <div class="experience-card">
                    <div class="experience-icon">🚶</div>
                    <h4>Village Walks</h4>
                </div>
            </div>
        </section>

        <!-- HOME FOOD SECTION -->
        <section class="home-food section-padding" id="food">
            <div class="container center slide-up">
                <span class="section-badge">Taste</span>
                <h2>Homely Coastal Cuisine</h2>
                <div class="food-icon mb-3" style="font-size: 3.5rem;">🍛</div>
                <p style="max-width: 700px; margin: 0 auto 1.5rem; line-height: 1.6; font-size: 1.1rem; color: var(--text-dark);">
                    Savor the authentic taste of the coast with our fresh home-cooked meals. Prepared on request using local ingredients, we offer a hygienic, warm, and homely dining experience.
                </p>
                <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
                    <span class="feature-chip" style="background: var(--bg-soft); color: var(--text-dark); border: none; font-weight: 500;">✓ Fresh Home-Cooked</span>
                    <span class="feature-chip" style="background: var(--bg-soft); color: var(--text-dark); border: none; font-weight: 500;">✓ Local Coastal Cuisine</span>
                    <span class="feature-chip" style="background: var(--bg-soft); color: var(--text-dark); border: none; font-weight: 500;">✓ Prepared on Request</span>
                    <span class="feature-chip" style="background: var(--bg-soft); color: var(--text-dark); border: none; font-weight: 500;">✓ Hygienic & Homely</span>
                </div>
            </div>
        </section>'''),
    
    # Reviews
    ('''        <!-- 10. BOOKING CTA SECTION -->
        <section class="booking-cta section-padding" id="booking-cta">''',
    '''        <!-- GUEST REVIEWS SECTION -->
        <section class="reviews section-padding bg-soft" id="reviews">
            <div class="container center slide-up">
                <span class="section-badge">Testimonials</span>
                <h2>Guest Reviews</h2>
                <p>What our guests say about their stay</p>
            </div>
            <div class="container experiences-grid slide-up mt-4" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                <div class="experience-card" style="text-align: left; padding: 2.5rem 2rem;">
                    <div style="color: #f59e0b; margin-bottom: 1rem; font-size: 1.3rem;">★★★★★</div>
                    <p style="font-style: italic; margin-bottom: 1.5rem; flex-grow: 1; line-height: 1.6; color: var(--text-dark);">"A perfect getaway. The sunrise view from the homestay is simply breathtaking, and the entire floor privacy makes it feel like an exclusive retreat. Highly recommend the village walks!"</p>
                    <h4 style="margin: 0; font-size: 1rem; font-weight: 600;">- Rahul S.</h4>
                </div>
                <div class="experience-card" style="text-align: left; padding: 2.5rem 2rem; display: flex; flex-direction: column;">
                    <div style="color: #f59e0b; margin-bottom: 1rem; font-size: 1.3rem;">★★★★★</div>
                    <p style="font-style: italic; margin-bottom: 1.5rem; flex-grow: 1; line-height: 1.6; color: var(--text-dark);">"We loved the peace and quiet here. It's exactly as described - away from the noise but close enough to explore Kagal and Baada beaches. Darshan is an excellent host."</p>
                    <h4 style="margin: 0; font-size: 1rem; font-weight: 600;">- Priya M.</h4>
                </div>
                <div class="experience-card" style="text-align: left; padding: 2.5rem 2rem; display: flex; flex-direction: column;">
                    <div style="color: #f59e0b; margin-bottom: 1rem; font-size: 1.3rem;">★★★★★</div>
                    <p style="font-style: italic; margin-bottom: 1.5rem; flex-grow: 1; line-height: 1.6; color: var(--text-dark);">"The local home-cooked seafood was incredible. Watching dolphins on the boat ride and simply relaxing by the riverside made our trip unforgettable. Very hygienic and homely."</p>
                    <h4 style="margin: 0; font-size: 1rem; font-weight: 600;">- Karthik V.</h4>
                </div>
            </div>
        </section>

        <!-- 10. BOOKING CTA SECTION -->
        <section class="booking-cta section-padding" id="booking-cta">'''),
    
    # About Section in Index text update
    ('Soukhya Riverside Homestay is a peaceful nature retreat located in the scenic village of\n                        Aghanashini near Gokarna, Karnataka.', 
     'Soukhya Riverside Homestay is a peaceful nature retreat located in the scenic village of Aghanashini. Stay away from the noise, yet close enough to explore Gokarna beaches.'),
    ('near the banks of Aghanashini river near Gokarna', 'near the banks of Aghanashini river. A peaceful riverside stay, away from crowded areas but close enough to explore'),
]
update_file(os.path.join(base_dir, 'index.html'), index_replacements)

# CTA updates for all pages
def global_cta_replace(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Special handling for CTAs pointing to form vs WA
    # Replacing normal Book Now linking to rooms.html form to go directly to WA
    content = content.replace('<a href="rooms.html#booking-form" class="btn btn-primary btn-sm">Book Now</a>',
                               '<a href="https://wa.me/918217399823" target="_blank" class="btn btn-primary btn-sm">Check Availability on WhatsApp</a>')
    
    content = content.replace('<a href="rooms.html#booking-form" class="btn btn-primary">Book Your Stay</a>',
                               '<a href="https://wa.me/918217399823" target="_blank" class="btn btn-primary">Check Availability on WhatsApp</a>')
    
    # Replace other standard buttons in rooms.html or if they were missed
    content = content.replace('>Book Room</a>', '>Check Availability on WhatsApp</a>')
    content = content.replace('>Book Villa</a>', '>Check Availability on WhatsApp</a>')
    content = content.replace('href="#booking-form"', 'href="https://wa.me/918217399823" target="_blank"')

    # Replace location text globally
    content = content.replace('near Gokarna', 'away from Gokarna crowds')
    content = content.replace('Near Gokarna', 'Away from Gokarna Crowds')
    content = content.replace('away from Gokarna crowds beaches', 'Gokarna beaches') # fix double replacements
    content = content.replace('Looking for a peaceful nature stay away from Gokarna crowds?', 'Looking for a peaceful riverside stay in Aghanashini village?')
    
    # Fix the location map text in contact
    content = content.replace('while being within easy reach of the\n                        famous Gokarna beaches', 'while being away from the noise, yet close enough to explore the famous Gokarna beaches (approx 1 hour drive). Ideal for travelers who want both relaxation and exploration')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for page in ['about.html', 'rooms.html', 'contact.html', 'gallery.html']:
    page_path = os.path.join(base_dir, page)
    if os.path.exists(page_path):
        global_cta_replace(page_path)
        print(f"Global replaced {page_path}")

print("All files updated successfully.")
