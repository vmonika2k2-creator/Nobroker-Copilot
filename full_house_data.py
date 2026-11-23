"""Data for the Full Home Cleaning page (taken from the 'NO broker Screens' Figma section)."""


def _pkg(id_, name, rating, duration, price, includes, starts_at=False):
    return {"id": id_, "name": name, "rating": rating, "duration": duration,
            "price": price, "includes": includes, "startsAt": starts_at}


_ESSENTIAL_APT = [
    "Bathroom & kitchen deep cleaning",
    "Machine cleaning of floors, doors & windows",
    "Cobweb removal, ceiling & fan dusting",
]
_PREMIUM_APT = [
    "Includes everything in Essential Plan",
    "Cupboard cleaning (interior + exterior, if empty)",
    "Cabinets interior with utensil removal",
]
_VILLA_ESSENTIAL = [
    "Bathroom and kitchen deep cleaning",
    "Wiping and mopping of complete floor area",
    "Cobweb removal and wall dry dusting",
    "Balcony and utility area cleaning",
]
_VILLA_PREMIUM = [
    "Bathroom and kitchen deep cleaning",
    "Cobweb removal and wall dry dusting",
    "Dry vacuuming of sofa, carpet and chair",
    "Machine cleaning of floors, doors and windows",
    "Furniture and appliances dusting and wet wiping",
]

SECTIONS = [
    {"id": "furnished-apartment", "title": "Furnished Apartment", "items": [
        _pkg("fa-essential", "Essential", "4.75 (11.4K+)", "3 hrs 45 mins", 3609,
             ["Bathroom & kitchen deep cleaning", "Machine cleaning of floors, doors & windows",
              "Cobweb removal, ceiling & fan dusting", "Balcony & utility area cleaning",
              "Cabinet & furniture exterior dusting & wet wiping"]),
        _pkg("fa-premium", "Premium", "4.7 (24.7K+)", "4 hrs 15 mins", 4099,
             ["Includes everything in Essential Plan", "Cupboard cleaning (interior + exterior, if empty)",
              "Cabinets interior with utensil removal"]),
        _pkg("fa-elite", "Elite", "4.7 (16.1K+)", "4 hrs 45 mins", 4539,
             ["Includes everything in Premium plan", "Sofa, carpet & mattress shampooing"]),
    ]},
    {"id": "unfurnished-apartment", "title": "Unfurnished Apartment", "items": [
        _pkg("ua-essential", "Essential", "4.72 (22.5K+)", "3 hrs", 3319, _ESSENTIAL_APT),
        _pkg("ua-premium", "Premium", "4.63 (27.9K+)", "3 hrs 40 mins", 3949, _PREMIUM_APT),
        _pkg("ua-post", "Post Interior Work", "4.63 (390)", "6 hrs", 4699,
             ["Includes everything in Premium Plan", "Includes sticker, gum and garbage removal",
              "Paint and stain removal with the best possible efficiency (100% removal not guaranteed)"]),
    ]},
    {"id": "furnished-villa", "title": "Furnished Villa", "items": [
        _pkg("fv-essential", "Essential", "4.73 (784)", "5 hrs 20 mins", 4439, _VILLA_ESSENTIAL),
        _pkg("fv-premium", "Premium", "4.65 (982)", "5 hrs 50 mins", 6729, _VILLA_PREMIUM),
    ]},
    {"id": "unfurnished-villa", "title": "Unfurnished Villa", "items": [
        _pkg("uv-essential", "Essential", "4.66 (821)", "5 hrs 20 mins", 4419, _VILLA_ESSENTIAL),
        _pkg("uv-premium", "Premium", "4.64 (1.4K+)", "5 hrs 50 mins", 5819,
             ["Bathroom and kitchen deep cleaning", "Cobweb removal and wall dry dusting",
              "Wiping and mopping of complete floor area", "Machine cleaning of floors, doors and windows"]),
    ]},
    {"id": "book-by-room", "title": "Book by Room", "items": [
        _pkg("room-bedroom", "Bedroom Cleaning", "4.76 (4.8K+)", "1 hr", 649,
             ["Dusting and mopping of all bedroom surfaces", "Ideal for both empty and furnished rooms"], True),
        _pkg("room-living", "Living Room Cleaning", "4.72 (2.5K+)", "1 hr 30 mins", 899,
             ["Deep cleaning of floors, furniture, and fixtures to refresh your living space"], True),
        _pkg("room-floor", "Floor Cleaning", "4.78 (2.4K+)", "1 hr", 399,
             ["Thorough cleaning of tiles, grouts, and corners"]),
    ]},
    {"id": "mini-services", "title": "Mini Services", "items": [
        _pkg(f"mini-{i}", n, None, d, p, [f"{n} by a trained, background-verified partner"])
        for i, (n, d, p) in enumerate([
            ("Balcony Cleaning: Upto 4 ft Width", "1 hr", 399),
            ("Balcony Cleaning: Above 4 ft Width", "1 hr 20 mins", 549),
            ("Utensils Removal & Replacement", "30 mins", 409),
            ("Fan Cleaning", "15 mins", 89),
            ("Ceiling Dusting & Cobweb Cleaning", "20 mins", 179),
            ("Single Door Fridge Cleaning", "30 mins", 379),
            ("Double Door Fridge Cleaning", "1 hr", 499),
            ("Window Cleaning (Upto 4 Ft X 4 Ft)", "30 mins", 399),
            ("Window Cleaning (Above 4 Ft X 4 Ft)", "1 hr", 449),
            ("Cushion Cleaning", "30 mins", 169),
            ("Microwave Cleaning", "30 mins", 189),
            ("Dining Table & Chairs (6) Cleaning", "20 mins", 549),
            ("Dining Table & Chairs (4) Cleaning", "15 mins", 449),
        ])
    ]},
]

RATINGS = [
    {"stars": 5, "count": 278498}, {"stars": 4, "count": 8952}, {"stars": 3, "count": 4917},
    {"stars": 2, "count": 4000}, {"stars": 1, "count": 10955},
]

REVIEWS = [
    {"name": "Neha", "stars": 5, "date": "21 Nov 2026", "service": "Furnished Apartment - Premium (3 BHK)",
     "text": "Very satisfied with cleaning"},
    {"name": "Saimah Khan", "stars": 5, "date": "21 Nov 2026",
     "service": "Furnished Apartment - Essential (2 BHK), Single Door Fridge Cleaning",
     "text": "Very professional and sincere team. Timely start and a seamless process."},
    {"name": "Ajith", "stars": 5, "date": "21 Nov 2026", "service": "Unfurnished Apartment - Essential (2 BHK)",
     "text": "Very good cleaning. Well deserved 5 stars."},
    {"name": "Manasa", "stars": 5, "date": "21 Nov 2026", "service": "Unfurnished Apartment - Essential (1 BHK)",
     "text": "It was very good service"},
    {"name": "Ashutosh Soni", "stars": 5, "date": "21 Nov 2026", "service": "Post Interior Work (1 BHK)",
     "text": "Very good service. Nice behaviour and good work done by the team."},
    {"name": "Chirag", "stars": 5, "date": "21 Nov 2026", "service": "Furnished Apartment - Elite (2 BHK)",
     "text": "Service was too good and appreciable, everything was properly cleaned."},
    {"name": "Aishwarya", "stars": 5, "date": "21 Nov 2026", "service": "Balcony Cleaning (Upto 4 ft Width)",
     "text": "Very nice service, I booked bathroom and balcony cleaning."},
    {"name": "Sai Krishnan", "stars": 5, "date": "21 Nov 2026", "service": "Furnished Apartment - Premium (3 BHK)",
     "text": "Excellent work. We are fully satisfied with the output."},
]

INCLUDED = [
    "Deep cleaning of living rooms, bedrooms, kitchens, bathrooms and utility areas",
    "Machine-assisted floor scrubbing and mopping",
]
NOT_INCLUDED = [
    "Repair, servicing or dismantling of appliances and fixtures",
    "Plumbing, electrical or maintenance work",
]

FAQS = [
    {"q": "How often should I schedule professional home cleaning services?",
     "a": "Professional home cleaning is recommended at least once every six months."},
    {"q": "Do I need to be present during the cleaning?",
     "a": "No, you don't have to be home. Secure key management options are available."},
    {"q": "Will the cleaners move furniture while cleaning?",
     "a": "The team can move light furniture to clean thoroughly. Heavier pieces are cleaned around."},
    {"q": "What happens if I am not satisfied with the cleaning?",
     "a": "Customer satisfaction is the priority. If you are unhappy with any part of the service, let us know and we will make it right."},
    {"q": "Can I reschedule or cancel my cleaning service?",
     "a": "Yes, you can reschedule or cancel anytime before the scheduled service."},
    {"q": "How can I book a home cleaning session?",
     "a": "Pick a package on this page, add it to your cart, enter your details and confirm the booking."},
]


def page_data():
    return {"sections": SECTIONS, "ratings": RATINGS, "reviews": REVIEWS,
            "included": INCLUDED, "not_included": NOT_INCLUDED, "faqs": FAQS}
