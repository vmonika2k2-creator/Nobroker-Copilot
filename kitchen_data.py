"""Data for the Kitchen Cleaning page (from the 'NO broker Screens' Figma section).

Image files are expected in static/img/kitchen/ (see IMAGES below). The page hides
any image that is missing, so it still works before the files are added.
"""

IMG = "/static/img/kitchen/"


def _item(id_, name, rating, duration, price, includes, image=None, starts_at=False, options=None, badge=None):
    return {"id": id_, "name": name, "rating": rating, "duration": duration, "price": price,
            "includes": includes, "image": (IMG + image) if image else None,
            "startsAt": starts_at, "options": options, "badge": badge}


SECTIONS = [
    {"id": "occupied", "title": "Occupied Kitchen Cleaning", "tabImage": IMG + "tab-occupied.png",
     "items": [
        _item("occ-eco", "Eco-Smart", "4.72 (4.5K+)", "2 hrs 30 mins", 2009, [
            "Odourless eco-smart deep cleaning",
            "High-pressure steam + active foam degreases tiles, slabs & gas stove/hob without fumes",
            "Includes all of Power Steam cleaning (sink, cabinets, utensils, exhaust & more)",
            "Non-corrosive and safe for family"], "eco-smart.png", options="2 options", badge="🌿"),
        _item("occ-steam", "Power Steam", "4.77 (7.4K+)", "3 hrs", 1959, [
            "High-pressure steam degreasing of kitchen tiles, slabs & gas stove / hob",
            "Sink & under the sink, exhaust & fan dusting",
            "Kitchen floors, windows & switchboard fixtures cleaning",
            "Utensil removal / rearrangement included",
            "Cabinet cleaning - exterior & interior"], options="2 options"),
        _item("occ-essential", "Essential", "4.74 (5.8K+)", "3 hrs", 1459, [
            "Degreasing of kitchen tiles, floor & slab, gas stove / hob",
            "Sink & under-the-sink, exhaust & fan dusting",
            "Kitchen floors, windows & switchboard fixtures cleaning",
            "Utensil removal / rearrangement not included",
            "Cabinet cleaning - exterior only"], options="2 options", badge="⭐"),
    ]},
    {"id": "empty", "title": "Empty Kitchen Cleaning", "tabImage": IMG + "tab-empty.png",
     "items": [
        _item("emp-essential", "Essential", "4.75 (4.5K+)", "2 hrs 30 mins", 849, [
            "Degreasing of kitchen tiles, slabs & gas stove / hob",
            "Sink & under-the-sink, exhaust & fan dusting",
            "Kitchen floors, windows & switchboard fixtures cleaning",
            "Utensil removal / rearrangement not included",
            "Cabinet cleaning - exterior only"], options="2 options", badge="⭐"),
        _item("emp-steam", "Power Steam", "4.73 (3.9K+)", "2 hrs 30 mins", 949, [
            "High-pressure steam degreasing of kitchen tiles, slabs & gas stove / hob",
            "Sink & under-the-sink, exhaust & fan dusting",
            "Kitchen floors, windows & switchboard fixtures cleaning",
            "Utensil removal / rearrangement not included",
            "Cabinet cleaning - exterior only"], options="2 options"),
    ]},
    {"id": "dedicated", "title": "Appliances & Dedicated Cleaning", "tabImage": None,
     "items": [
        _item("ded-fridge", "Fridge Cleaning", "4.75 (24.8K+)", "30 mins", 379, [
            "Removing and placing back all food items", "Cleaning of shelves and trays",
            "Wiping interior & exterior surfaces", "Removal of food stains, crumbs, and odors"],
            "fridge.png", starts_at=True, options="3 options"),
        _item("ded-chimney", "Chimney Cleaning", "4.81 (30.3K+)", "30 mins", 379, [
            "Degreasing and stain removal of one chimney", "Mesh and filter deep cleaning",
            "Digital chimney cleaning is carried out only on the exterior"]),
        _item("ded-utility", "Utility Area Cleaning", "4.74 (1.6K+)", "1 hr", 499, [
            "End-to-end cleaning of utility windows, appliances, and floor for a hygienic area"]),
        _item("ded-microwave", "Microwave Cleaning", "4.72 (9.3K+)", "30 mins", 189, [
            "Deep cleaning of microwave exterior",
            "Wet wiping of interior to remove stains and remove odour",
            "Removing oil stain, Food stain"]),
        _item("ded-stove", "Gas Stove Cleaning", "4.78 (3.9K+)", "30 mins", 89, [
            "Removes grease, stains, and grime from stove, burners, and knobs"]),
        _item("ded-tiles", "Kitchen Tiles and Slabs Cleaning", "4.76 (2.5K+)", "30 mins", 279, [
            "Degreases tiles & slabs and deep cleans grout for a fresh kitchen"]),
        _item("ded-cabinet", "Cabinet & Trolley Cleaning", "4.76 (3K+)", "1 hr", 1139, [
            "Cleaning inside of cabinets. Includes removal & placing back of items",
            "Removal of oil & grease stains from cabinets exterior"]),
        _item("ded-oven", "Oven, Toaster & Grill Cleaning", "4.72 (608)", "15 mins", 379, [
            "Deep cleaning the interiors for food crumbs & spills",
            "Cleaning of exterior & back panel for grease stains"]),
    ]},
    {"id": "mini", "title": "Mini Services", "tabImage": IMG + "tab-mini.png",
     "items": [
        _item(f"mini-{i}", n, None, d, p, [f"{n} by a trained, background-verified partner"])
        for i, (n, d, p) in enumerate([
            ("Fan Cleaning", "15 mins", 89),
            ("Utensils Removal & Replacement", "30 mins", 409),
            ("Sink & Under Sink Cleaning", "20 mins", 79),
            ("Kitchen Window Cleaning", "30 mins", 269),
            ("Dining Table & Chairs (6) Cleaning", "20 mins", 549),
            ("Dining Table & Chairs (4) Cleaning", "15 mins", 449),
            ("Balcony Cleaning: Upto 4 ft Width", "1 hr", 399),
            ("Balcony Cleaning: Above 4 ft Width", "1 hr 20 mins", 549),
            ("Window Cleaning (Upto 4 Ft X 4 Ft)", "30 mins", 399),
            ("Window Cleaning (Above 4 Ft X 4 Ft)", "1 hr", 449),
        ])
    ]},
]

# Tabs shown under the page title, in the same order as the Figma design
TABS = [
    {"label": "Occupied Kitchen Cleaning", "target": "occupied", "image": IMG + "tab-occupied.png", "fallback": "🍳"},
    {"label": "Empty Kitchen Cleaning", "target": "empty", "image": IMG + "tab-empty.png", "fallback": "🧽"},
    {"label": "Mini Services", "target": "mini", "image": IMG + "tab-mini.png", "fallback": "🪟"},
]

HERO = {"image": IMG + "hero.png", "title": "Kitchen Cleaning Service in Pune",
        "rating": "4.77 (219.5K+ ratings)",
        "vip": "Save upto 15% off on cleaning, plumbing and ac services"}

RATINGS = [
    {"stars": 5, "count": 201434}, {"stars": 4, "count": 5835}, {"stars": 3, "count": 3060},
    {"stars": 2, "count": 2329}, {"stars": 1, "count": 6866},
]

REVIEWS = [
    {"name": "Saimah Khan", "stars": 5, "date": "21 Nov 2026", "service": "Furnished Apartment - Essential (2 BHK), Single Door Fridge Cleaning",
     "text": "Very professional and sincere team. Timely start and a seamless process."},
    {"name": "Chirag", "stars": 5, "date": "21 Nov 2026", "service": "Furnished Apartment - Elite (2 BHK), Single Door Fridge Cleaning",
     "text": "Service was too good and appreciable, everything was properly cleaned."},
    {"name": "Aishwarya", "stars": 5, "date": "21 Nov 2026", "service": "Balcony Cleaning, Eco-Smart Bathroom Cleaning",
     "text": "Very nice service, I booked bathroom and balcony cleaning."},
    {"name": "Ajith", "stars": 5, "date": "21 Nov 2026", "service": "Kitchen Cleaning - Power Steam",
     "text": "Very good cleaning. Well deserved 5 stars."},
]

INCLUDED = [
    "Degreasing of kitchen tiles, slab, gas stove / hob, sink and exhaust",
    "Cleaning of kitchen floor, windows and switchboard fixtures",
    "Cabinet cleaning (exterior; interior in Power Steam and Eco-Smart)",
]
NOT_INCLUDED = [
    "Repair, servicing or dismantling of appliances and fixtures",
    "Plumbing, electrical or maintenance work",
    "Digital chimney interior cleaning",
]

FAQS = [
    {"q": "What is the difference between occupied and empty kitchen cleaning?",
     "a": "Occupied kitchens have utensils and items in place, so the partner works around them or removes and rearranges them in the higher plans. Empty kitchens are cleaned with nothing inside."},
    {"q": "Do I need to be present during the cleaning?",
     "a": "No, you don't have to be home. Secure key management options are available."},
    {"q": "Are the cleaning products safe for my family?",
     "a": "Eco-Smart uses an odourless, non-corrosive, family-safe foam with high-pressure steam."},
    {"q": "Can I reschedule or cancel my service?",
     "a": "Yes, you can reschedule or cancel anytime before the scheduled service."},
    {"q": "How can I book kitchen cleaning?",
     "a": "Pick a package on this page, add it to your cart, enter your details and confirm the booking."},
]


def page_data():
    return {"hero": HERO, "tabs": TABS, "sections": SECTIONS, "ratings": RATINGS, "reviews": REVIEWS,
            "included": INCLUDED, "not_included": NOT_INCLUDED, "faqs": FAQS}
