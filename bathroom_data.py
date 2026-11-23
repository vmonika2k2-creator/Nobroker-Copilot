"""Data for the Bathroom Cleaning page (from the 'NO broker Screens' Figma section).

Icons and photos live in assets/bathroom cleaning/ (served at /assets/...). For every
`photo` name the page tries <name>.jpg first and falls back to <name>.svg.
"""

BASE = "/assets/bathroom%20cleaning/"


def _item(id_, name, rating, duration, price, includes, icon, photo=None, starts_at=False, options=None):
    return {"id": id_, "name": name, "rating": rating, "duration": duration, "price": price,
            "includes": includes, "icon": BASE + "icons/" + icon + ".svg",
            "photo": (BASE + "photos/" + photo) if photo else None,
            "startsAt": starts_at, "options": options}


SECTIONS = [
    {"id": "bathroom", "title": "Bathroom Cleaning", "items": [
        _item("bath-eco", "Eco-Smart", "4.81 (47.3K+)", None, 509, [
            "Deep bathroom cleaning using eco-friendly active foam technology",
            "Removes tough stains, soap scum, and grime without bleach, fumes, or residue",
            "Odourless, non-corrosive, and family-safe",
            "Includes machine-assisted scrubbing"], "leaf", "eco-smart", options="5 options"),
        _item("bath-machine", "Machine", "4.74 (234.1K+)", None, 479, [
            "Machine scrubbing of floor and tiles", "Removal of dirt & black spots",
            "Ideal for tough stain removal and deep cleaning"], "machine", options="5 options"),
        _item("bath-hands", "Hands On", "4.75 (312.6K+)", "50 mins", 439, [
            "Manual scrubbing for regular cleaning", "Removal of dirt & black spots",
            "Takes 50 mins per bathroom"], "hand", options="5 options"),
    ]},
    {"id": "balcony", "title": "Balcony Cleaning", "items": [
        _item("balcony-1", "Balcony Cleaning", "4.78 (19.3K+)", "1 hr", 399, [
            "Sweeping & mopping of balcony floor",
            "Dusting & wiping of railings, grills, and accessible walls",
            "Removal of cobwebs and loose dirt",
            "Cleaning of sliding door glass (inside & outside, where it's reachable)"],
            "balcony", "balcony", True, "2 options"),
    ]},
    {"id": "mini", "title": "Mini Services", "items": [
        _item(f"mini-{i}", n, None, d, p, [f"{n} by a trained, background-verified partner"], ic)
        for i, (n, d, p, ic) in enumerate([
            ("Fan Cleaning", "15 mins", 89, "fan"),
            ("Washbasin Cleaning", "10 mins", 79, "washbasin"),
            ("Chimney Cleaning", "30 mins", 379, "chimney"),
            ("Exhaust Fan Cleaning", "20 mins", 79, "exhaust-fan"),
            ("Single Door Fridge Cleaning", "30 mins", 379, "fridge"),
            ("Mirror Cleaning", "10 mins", 49, "mirror"),
            ("Double Door Fridge Cleaning", "1 hr", 499, "fridge"),
            ("Window Cleaning (Upto 4 Ft X 4 Ft)", "30 mins", 399, "window"),
            ("Window Cleaning (Above 4 Ft X 4 Ft)", "1 hr", 449, "window"),
            ("Microwave Cleaning", "30 mins", 189, "microwave"),
            ("Dining Table & Chairs (6) Cleaning", "20 mins", 549, "dining"),
            ("Dining Table & Chairs (4) Cleaning", "15 mins", 449, "dining"),
            ("Utensils Removal & Replacement", "30 mins", 409, "utensils"),
        ])
    ]},
]

TABS = [
    {"label": "Bathroom Cleaning", "target": "bathroom", "icon": BASE + "icons/bath.svg"},
    {"label": "Balcony Cleaning", "target": "balcony", "icon": BASE + "icons/balcony.svg"},
    {"label": "Mini Services", "target": "mini", "icon": BASE + "icons/sparkles.svg"},
]

HERO = {"photo": BASE + "photos/hero", "title": "Bathroom Cleaning Services in Pune",
        "rating": "4.76 (779K+ ratings)",
        "vip": "Save upto 15% off on cleaning, plumbing and ac services"}

RATINGS = [
    {"stars": 5, "count": 703055}, {"stars": 4, "count": 28962}, {"stars": 3, "count": 12629},
    {"stars": 2, "count": 8855}, {"stars": 1, "count": 25511},
]

REVIEWS = [
    {"name": "Reema", "stars": 5, "date": "21 Nov 2026", "service": "Eco-Smart Bathroom Cleaning (2 Bathrooms)",
     "text": "Cleaning was good, though a little odour was left behind in the bathroom."},
    {"name": "Kavitha", "stars": 5, "date": "21 Nov 2026", "service": "Bathroom Hands On Cleaning (2 Bathrooms), Washbasin Cleaning",
     "text": "He is a good cleaning person."},
    {"name": "Aishwarya", "stars": 5, "date": "21 Nov 2026", "service": "Balcony Cleaning, Eco-Smart Bathroom Cleaning (1 Bathroom)",
     "text": "Very nice service, I booked bathroom and balcony cleaning."},
    {"name": "Ramakrishnan", "stars": 5, "date": "21 Nov 2026", "service": "Bathroom Hands On Cleaning (2 Bathrooms), Window Cleaning (x4)",
     "text": "Excellent service & very neat and clean. Thanks."},
]

INCLUDED = [
    "Scrubbing of floor, tiles and fittings; removal of dirt, soap scum and black spots",
    "Cleaning of washbasin, toilet seat, taps, mirror and accessible surfaces",
    "Machine-assisted scrubbing in Machine and Eco-Smart plans",
]
NOT_INCLUDED = [
    "Plumbing, leakage or fitting repairs",
    "Permanent stains or damaged tiles",
    "Cleaning of ceiling tiles or false ceilings",
]

FAQS = [
    {"q": "What is the difference between Eco-Smart, Machine and Hands On?",
     "a": "Eco-Smart uses odourless, family-safe active foam with machine scrubbing. Machine uses machine scrubbing for tough stains. Hands On is manual scrubbing for regular cleaning."},
    {"q": "How long does bathroom cleaning take?",
     "a": "Hands On takes about 50 minutes per bathroom."},
    {"q": "Do I need to be present during the cleaning?",
     "a": "No, you don't have to be home. Secure key management options are available."},
    {"q": "Are the products safe for my family?",
     "a": "Eco-Smart is odourless, non-corrosive and free of bleach and fumes."},
    {"q": "Can I reschedule or cancel my service?",
     "a": "Yes, you can reschedule or cancel anytime before the scheduled service."},
]


def page_data():
    return {"hero": HERO, "tabs": TABS, "sections": SECTIONS, "ratings": RATINGS, "reviews": REVIEWS,
            "included": INCLUDED, "not_included": NOT_INCLUDED, "faqs": FAQS}
