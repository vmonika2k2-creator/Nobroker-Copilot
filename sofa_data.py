"""Data for the Sofa Cleaning page (from the 'NO broker Screens' Figma section).

Icons and photos live in assets/sofa cleaning/ (served at /assets/...). For every
`photo` name the page tries <name>.jpg first and falls back to <name>.svg.
"""

BASE = "/assets/sofa%20cleaning/"


def _item(id_, name, rating, duration, price, includes, icon, photo=None, starts_at=False, options=None):
    return {"id": id_, "name": name, "rating": rating, "duration": duration, "price": price,
            "includes": includes, "icon": BASE + "icons/" + icon + ".svg",
            "photo": (BASE + "photos/" + photo) if photo else None,
            "startsAt": starts_at, "options": options}


SECTIONS = [
    {"id": "sofa", "title": "Sofa cleaning", "items": [
        _item("sofa-1", "Sofa Cleaning", "4.79 (36.2K+)", "45 mins", 329, [
            "Shampooing and freshen the sofa's plush seats",
            "Thorough dry and wet vacuuming for deep cleaning",
            "Not inclusive of cushion shampooing and vacuuming"], "sofa", "sofa", options="11 options"),
        _item("sofa-2", "Sofa with Cushion Cleaning", "4.84 (10.6K+)", "1 hr 15 mins", 599, [
            "Shampooing and freshen the sofa's plush seats",
            "Thorough dry and wet vacuuming for deep cleaning",
            "Same number of cushions are included as per seats of sofa selected"],
            "sofa-cushion", "sofa-cushion", options="11 options"),
        _item("sofa-3", "Mattress Cleaning", "4.82 (5.9K+)", "30 mins", 389, [
            "Dry and wet vacuuming, shampooing and stain removal of mattress",
            "Mattress shampooing & removing hard stains."], "mattress", "mattress", True, "2 options"),
        _item("sofa-4", "Cushion Cleaning", "4.84 (905)", "30 mins", 169, [
            "Wet & dry vacuuming with shampooing", "Up to 5 cushions per booking",
            "Removes dust, stains & odour"], "cushion", "cushion"),
        _item("sofa-5", "Dining Table & Chairs Cleaning", "4.8 (2.7K+)", "15 mins", 449, [
            "Dry vacuuming of cushioned chairs and wet wiping of dining table",
            "Shampooing the dining chair", "Cleaning under dining tables & chair",
            "Removing touch stain, oil stain, food stain"], "dining", "dining", True, "7 options"),
        _item("sofa-6", "Window Cleaning", "4.74 (9.5K+)", "30 mins", 399, [
            "Thorough cleaning of your window"], "window", "window", True, "2 options"),
        _item("sofa-7", "Recliner Cleaning", "4.83 (491)", "20 mins", 219, [
            "Removes stains and spillage through dry and wet vacuuming"], "recliner", "recliner", True, "3 options"),
        _item("sofa-8", "Sofa Cum Bed Cleaning", "4.92 (281)", "40 mins", 379, [
            "Vacuuming and foam cleaning to remove dust, dirt and common stains",
            "Wood surface cleaning"], "sofa-bed", "sofa-bed", True, "4 options"),
    ]},
    {"id": "carpet", "title": "Carpet cleaning", "items": [
        _item("carpet-1", "Carpet Cleaning", "4.77 (6.6K+)", "1 hr", 369, [
            "Removal of accumulated dust particles, dirt, debris",
            "Foam based shampooing on the carpet using a sponge",
            "Vacuuming & wiping shampoo using microfibre cloth"], "carpet", "carpet", True, "5 options"),
    ]},
    {"id": "mini", "title": "Mini Services", "items": [
        _item(f"mini-{i}", n, None, d, p, [f"{n} by a trained, background-verified partner"], ic)
        for i, (n, d, p, ic) in enumerate([
            ("Sofa Center Table Cleaning", "30 mins", 179, "table"),
            ("Study Table and Chair Cleaning", "30 mins", 229, "study"),
            ("Fan Cleaning", "15 mins", 89, "fan"),
            ("Single Door Fridge Cleaning", "30 mins", 379, "fridge"),
            ("Ottoman Cleaning", "15 mins", 99, "ottoman"),
            ("Showcase Cleaning", "20 mins", 199, "showcase"),
            ("Door Cleaning", "10 mins", 89, "door"),
            ("Double Door Fridge Cleaning", "1 hr", 499, "fridge"),
            ("Balcony Cleaning: Upto 4 ft Width", "1 hr", 399, "balcony"),
            ("Balcony Cleaning: Above 4 ft Width", "1 hr 20 mins", 549, "balcony"),
            ("Microwave Cleaning", "30 mins", 189, "microwave"),
            ("Utensils Removal & Replacement", "30 mins", 409, "utensils"),
        ])
    ]},
]

TABS = [
    {"label": "Sofa cleaning", "target": "sofa", "icon": BASE + "icons/sofa.svg"},
    {"label": "Carpet cleaning", "target": "carpet", "icon": BASE + "icons/carpet.svg"},
    {"label": "Mini Services", "target": "mini", "icon": BASE + "icons/sparkles.svg"},
]

HERO = {"photo": BASE + "photos/hero", "title": "Best Sofa Cleaning Service in Pune",
        "rating": "4.78 (249.1K+ ratings)",
        "vip": "Save upto 15% off on cleaning, plumbing and ac services"}

RATINGS = [
    {"stars": 5, "count": 229509}, {"stars": 4, "count": 6559}, {"stars": 3, "count": 3177},
    {"stars": 2, "count": 2451}, {"stars": 1, "count": 7411},
]

REVIEWS = [
    {"name": "Mahi Jagga", "stars": 5, "date": "21 Nov 2026", "service": "Sofa Cleaning (5 Sofa Seats)",
     "text": "Very polite and respectful service partner. Knows his job well."},
    {"name": "Saimah Khan", "stars": 5, "date": "21 Nov 2026", "service": "Furnished Apartment - Essential (2 BHK), Single Door Fridge Cleaning",
     "text": "Very professional and sincere team. Timely start and a seamless process."},
    {"name": "Chirag", "stars": 5, "date": "21 Nov 2026", "service": "Furnished Apartment - Elite (2 BHK)",
     "text": "Service was too good and appreciable, everything was properly cleaned."},
    {"name": "Ramakrishnan", "stars": 5, "date": "21 Nov 2026", "service": "Window Cleaning (x4)",
     "text": "Excellent service & very neat and clean. Thanks."},
]

INCLUDED = [
    "Dry and wet vacuuming of sofa, cushions, carpets and mattresses",
    "Foam / shampoo cleaning with removal of common stains and odour",
    "Cleaning of dining chairs, recliners and sofa-cum-beds",
]
NOT_INCLUDED = [
    "Permanent or old stains that cannot be removed",
    "Repair or stitching of upholstery",
    "Moving of heavy furniture",
]

FAQS = [
    {"q": "How long does sofa cleaning take?",
     "a": "A standard sofa takes about 45 minutes. Sofa with cushions takes about 1 hr 15 mins."},
    {"q": "Are cushions included in sofa cleaning?",
     "a": "No. Choose 'Sofa with Cushion Cleaning' to include the same number of cushions as sofa seats."},
    {"q": "Do I need to be present during the cleaning?",
     "a": "No, you don't have to be home. Secure key management options are available."},
    {"q": "Will all stains be removed?",
     "a": "Common stains are removed. Old or permanent stains may not come out fully."},
    {"q": "Can I reschedule or cancel my service?",
     "a": "Yes, you can reschedule or cancel anytime before the scheduled service."},
]


def page_data():
    return {"hero": HERO, "tabs": TABS, "sections": SECTIONS, "ratings": RATINGS, "reviews": REVIEWS,
            "included": INCLUDED, "not_included": NOT_INCLUDED, "faqs": FAQS}
