// Main JavaScript for Soukhya Homestay Website

document.addEventListener('DOMContentLoaded', () => {

    // 1. Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            
            // Animate hamburger to X (simplified)
            const spans = menuToggle.querySelectorAll('span');
            if (navLinks.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    }

    // 2. Sticky Navbar Effect on Scroll
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Reveal Animations on Scroll
    // Uses Intersection Observer to add 'is-visible' class when elements enter viewport
    const revealElements = document.querySelectorAll('.slide-up, .fade-in');
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };
    
    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Stop observing once revealed
            }
        });
    }, revealOptions);
    
    // Trigger hero fade-in immediately
    setTimeout(() => {
        const heroElements = document.querySelectorAll('.hero .fade-in');
        heroElements.forEach(el => el.classList.add('is-visible'));
    }, 100);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // 4. Smooth Scrolling for Anchor Links (with offset for fixed header)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Close mobile menu if open
                if (navLinks.classList.contains('active')) {
                    menuToggle.click();
                }
                
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
  
                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });

    // 5. Dynamic Pricing Calculator
    const checkInInput = document.getElementById('checkIn');
    const checkOutInput = document.getElementById('checkOut');
    const adultsInput = document.getElementById('adults');
    const childrenInput = document.getElementById('children');
    const priceDetails = document.getElementById('priceDetails');
    const estimatedTotal = document.getElementById('estimatedTotal');

    function calculateTotal() {
        if (!checkInInput || !checkOutInput || !adultsInput || !childrenInput || !estimatedTotal) return;

        const checkIn = new Date(checkInInput.value);
        const checkOut = new Date(checkOutInput.value);
        const adults = parseInt(adultsInput.value) || 0;
        const children = parseInt(childrenInput.value) || 0;

        // Reset if dates are invalid
        if (isNaN(checkIn.getTime()) || isNaN(checkOut.getTime()) || checkIn >= checkOut) {
            priceDetails.textContent = "Please select valid check-in and check-out dates";
            estimatedTotal.textContent = "--";
            return;
        }

        const nights = Math.ceil((checkOut - checkIn) / (1000 * 60 * 60 * 24));
        const totalGuests = adults + children;
        
        if (totalGuests === 0) {
            priceDetails.textContent = "Please add at least 1 guest";
            estimatedTotal.textContent = "--";
            return;
        }

        let totalAmount = 0;
        let weekdays = 0;
        let weekends = 0;

        // Calculate nights and identify weekends (Fri, Sat, Sun)
        let currentDate = new Date(checkIn);
        for (let i = 0; i < nights; i++) {
            const dayOfWeek = currentDate.getDay(); // 0 is Sunday, 5 is Friday, 6 is Saturday
            if (dayOfWeek === 0 || dayOfWeek === 5 || dayOfWeek === 6) {
                weekends++;
            } else {
                weekdays++;
            }
            currentDate.setDate(currentDate.getDate() + 1);
        }

        // Tiered Pricing logic for first 4 guests
        const baseGuests = Math.min(totalGuests, 4);
        
        const weekdayRates = { 1: 800, 2: 1000, 3: 1250, 4: 1500 };
        const weekendRates = { 1: 1000, 2: 1500, 3: 1750, 4: 2000 };

        const baseWeekdayRate = weekdayRates[baseGuests];
        const baseWeekendRate = weekendRates[baseGuests];

        totalAmount += (baseWeekdayRate * weekdays) + (baseWeekendRate * weekends);

        // Additional Guests (beyond 4)
        let extraAdults = 0;
        let extraChildren = 0;

        if (totalGuests > 4) {
            // Allocate the first 4 "slots" to adults first, then children
            const baseAdults = Math.min(adults, 4);
            extraAdults = adults - baseAdults;
            
            // If adults took all 4 slots, all children are extra. 
            // If adults took < 4 slots, children fill the remainder, and the rest are extra.
            const remainingBaseSlots = 4 - baseAdults;
            const baseChildren = Math.min(children, remainingBaseSlots);
            extraChildren = children - baseChildren;

            // Add extra charges per night
            const extraChargePerNight = (extraAdults * 300) + (extraChildren * 150);
            totalAmount += (extraChargePerNight * nights);
        }

        // Format and Display
        priceDetails.textContent = `${nights} night${nights > 1 ? 's' : ''} (${weekdays} weekday, ${weekends} weekend) for ${totalGuests} guest${totalGuests > 1 ? 's' : ''}`;
        estimatedTotal.textContent = `₹${totalAmount.toLocaleString('en-IN')}`;
    }

    // Attach listeners
    if (checkInInput && checkOutInput && adultsInput && childrenInput) {
        checkInInput.addEventListener('change', calculateTotal);
        checkOutInput.addEventListener('change', calculateTotal);
        adultsInput.addEventListener('input', calculateTotal);
        childrenInput.addEventListener('input', calculateTotal);
        
        // Prevent selecting past dates
        const today = new Date().toISOString().split('T')[0];
        checkInInput.setAttribute('min', today);
        
        checkInInput.addEventListener('change', function() {
            checkOutInput.setAttribute('min', this.value);
            if (checkOutInput.value && checkOutInput.value <= this.value) {
                checkOutInput.value = '';
                calculateTotal();
            }
        });
    }

    // 6. Booking Form Submission Handling
    const inquiryForm = document.getElementById('inquiryForm');
    const formSuccess = document.getElementById('formSuccess');

    if (inquiryForm) {
        inquiryForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Collect form data (for demonstration purposes or API integration)
            const formData = new FormData(this);
            const bookingDetails = Object.fromEntries(formData.entries());
            
            // Append the calculated total amount to the submission data
            if (estimatedTotal && estimatedTotal.textContent !== '--') {
                bookingDetails.estimatedTotal = estimatedTotal.textContent;
            }
            
            console.log('Booking Inquiry Submitted:', bookingDetails);
            
            // Hide the form and show success message
            this.style.display = 'none';
            formSuccess.classList.remove('hidden');
            
            // Scroll to the success message
            formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    }

    // 7. WhatsApp Booking Inquiry
    const whatsappBtn = document.getElementById('whatsappBtn');
    if (whatsappBtn && inquiryForm) {
        whatsappBtn.addEventListener('click', function() {
            // Validate required fields before proceeding
            const requiredFields = inquiryForm.querySelectorAll('[required]');
            let isValid = true;
            requiredFields.forEach(field => {
                if (!field.value) isValid = false;
            });
            
            if (!isValid) {
                // Trigger HTML5 validation UI
                inquiryForm.reportValidity();
                return;
            }

            const name = document.getElementById('fullName').value;
            const phoneVal = document.getElementById('phone').value;
            const countryCodeInput = document.getElementById('countryCode');
            const countryCode = countryCodeInput ? countryCodeInput.value.trim() : '+91';
            const phone = phoneVal ? `${countryCode} ${phoneVal}` : '';
            const email = document.getElementById('email').value;
            const checkin = document.getElementById('checkIn').value;
            const checkout = document.getElementById('checkOut').value;
            const adults = document.getElementById('adults').value || "0";
            const children = document.getElementById('children').value || "0";
            
            let priceText = "Not calculated";
            if (estimatedTotal && estimatedTotal.textContent !== '--') {
                priceText = estimatedTotal.textContent;
            }

            const message = `Hello, I would like to enquire about booking Soukhya Riverside Homestay.

Name: ${name}
Phone: ${phone}
Email: ${email}

Check-in: ${checkin}
Check-out: ${checkout}

Adults: ${adults}
Children: ${children}

Estimated Price Shown: ${priceText}

Please confirm availability and final price.`;

            const encodedMessage = encodeURIComponent(message);
            // WhatsApp requires the number without the + symbol for the wa.me link
            const whatsappNumber = "918217399823"; 
            window.open(`https://wa.me/${whatsappNumber}?text=${encodedMessage}`, '_blank');
        });
    }
});
