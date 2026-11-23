"""Electrician catalogue content based on the NoBroker electrician Figma section."""


def _service(name, price, rating, image, duration="", details=(), badge="", price_label="Starts at", old_price=None):
    return {
        "name": name,
        "price": price,
        "rating": rating,
        "image": image,
        "duration": duration,
        "details": list(details),
        "badge": badge,
        "price_label": price_label,
        "old_price": old_price,
    }


def page_data():
    categories = [
        {
            "id": "geyser", "title": "Geyser", "photo_stem": "geyser",
            "icon": "geyser", "items": [
                _service("Geyser Service", 475, "4.76 (4.8K+)", 2, details=["Thorough cleaning and descaling", "Helps improve heating efficiency and machine life", "Minor wiring up to 2m included"]),
                _service("Geyser Installation", 386, "4.8 (4.3K+)", 3, details=["Installation of one geyser", "Material charges additional, if any"]),
                _service("Geyser Check-Up", 141, "4.74 (6.9K+)", 4, badge="43% off", price_label="", old_price=249),
                _service("Geyser Uninstallation", 288, "4.79 (562)", 5, badge="28% off", price_label="", old_price=399),
            ],
        },
        {
            "id": "consultation", "title": "Book an Electrician", "photo_stem": "hero",
            "icon": "consultation", "items": [
                _service("At Home Consultation", 48, "4.74 (16.9K+)", 3, details=["On-site expert evaluation with an instant price quote", "Inspection amount is adjusted in the final price"], badge="13% off", price_label="", old_price=55),
            ],
        },
        {
            "id": "light", "title": "Light", "photo_stem": "light", "icon": "light", "items": [
                _service("Tube Light Install / Replace", 91, "4.88 (6.4K+)", 1, "30 mins"),
                _service("Ceiling Light Install / Replace", 139, "4.84 (1.7K+)", 2, "45 mins"),
                _service("Bulb & Bulb Holder Install / Replace", 71, "4.81 (2.9K+)", 3, "30 mins"),
                _service("CFL to LED Replacement", 91, "4.82 (594)", 4, "30 mins", ["Replacement of CFL bulb or tube light with LED"], price_label=""),
                _service("Wall Mounted Lights Install / Replace", 120, "4.82 (1.6K+)", 5, "30 mins", ["Decorative, bathroom or bedside light installation"]),
                _service("Outdoor Lights Install / Replace", 91, "4.95 (55)", 6, "45 mins"),
                _service("Hanging Lights Install", 187, "4.77 (141)", 7, "1 hr"),
                _service("Chandelier Install / Replace", 683, "4.75 (412)", 8, "1 hr 30 mins", ["Installation of one chandelier with bulbs"]),
            ],
        },
        {
            "id": "festive-lights", "title": "Wedding Lights", "photo_stem": "festive-lights", "icon": "festive", "items": [
                _service("Balcony Lights Installation", 238, "4.58 (373)", 1, "1 hr"),
                _service("Railing Lights Installation", 238, "4.54 (58)", 2, "1 hr"),
                _service("Mandir Lights Installation", 127, "4.48 (39)", 3, "1 hr"),
                _service("Light Uninstallation (per light)", 127, "4.77 (159)", 4, "30 mins", price_label=""),
                _service("Light Installation (per string)", 127, "4.73 (1.6K+)", 5, "30 mins", price_label=""),
                _service("Lantern Installation (per lantern)", 127, "4.59 (65)", 6, "30 mins", price_label=""),
                _service("Outdoor Festive Lights Installation", 1705, "4.66 (9)", 7, "2 hrs", badge="New"),
            ],
        },
        {
            "id": "switch-socket", "title": "Switch & socket", "photo_stem": "switch-socket", "icon": "socket", "items": [
                _service("Switch Replace / Install", 72, "4.86 (7.9K+)", 1, "30 mins"),
                _service("Socket Replace / Install", 72, "4.86 (4K+)", 2, "30 mins"),
                _service("Full Switchboard Installation", 119, "4.78 (3.2K+)", 3, "30 mins"),
                _service("Full Switchboard Repair / Replace", 139, "4.82 (7.9K+)", 4, "30 mins"),
                _service("External Switchbox Installation", 188, "4.77 (124)", 5, "30 mins"),
                _service("Fan Regulator Replace / Install", 82, "4.6 (66)", 6, "30 mins"),
                _service("Plug Replacement", 82, "4.83 (774)", 7, "30 mins"),
            ],
        },
        {
            "id": "fan", "title": "Fan", "photo_stem": "fan", "icon": "fan", "items": [
                _service("Fan Repair", 210, "4.76 (13.9K+)", 1, details=["Inspection and repair for a ceiling, wall or exhaust fan"]),
                _service("Fan Replacement", 222, "4.88 (3.9K+)", 2, details=["Replacement of a ceiling, wall or exhaust fan"]),
                _service("Fan Regulator Replacement", 82, "4.83 (3.2K+)", 3, "30 mins"),
                _service("Fan Uninstallation", 96, "4.89 (2.1K+)", 4),
                _service("Fan Installation", 145, "4.84 (10K+)", 5, details=["Installation of a ceiling, wall or exhaust fan"]),
            ],
        },
        {
            "id": "tv", "title": "TV", "photo_stem": "tv", "icon": "tv", "items": [
                _service("TV Installation", 380, "4.86 (7.4K+)", 1, "45 mins"),
                _service("TV Uninstallation", 331, "4.89 (1.2K+)", 2, "45 mins"),
                _service("TV Socket Installation", 82, "", 3, "30 mins", badge="New"),
                _service("Sound Bar Installation", 188, "4.76 (140)", 4, "45 mins"),
                _service("Home Theatre Installation", 235, "4.73 (203)", 5, "45 mins"),
            ],
        },
        {
            "id": "mcb-fuse", "title": "MCB & Fuse", "photo_stem": "mcb-fuse", "icon": "fuse", "items": [
                _service("MCB Fuse Replacement", 145, "4.77 (1.4K+)", 1),
                _service("Sub Meter Installation", 387, "4.75 (153)", 2, details=["Includes minor wiring work"]),
                _service("3-Phase Changeover Switch Installation", 269, "4.54 (114)", 3),
                _service("MCB Installation", 145, "4.8 (870)", 4, details=["Single, double or four pole MCB installation"]),
            ],
        },
        {
            "id": "inverter", "title": "Inverter & Stabilizer", "photo_stem": "inverter", "icon": "inverter", "items": [
                _service("Inverter Servicing", 242, "4.66 (1.4K+)", 1, details=["Terminal dust removal and distilled water top-up"]),
                _service("Stabilizer Installation", 145, "4.86 (726)", 2),
                _service("Inverter Fuse Replacement", 96, "4.58 (179)", 3),
                _service("Inverter Installation", 470, "4.69 (1.4K+)", 4),
            ],
        },
        {
            "id": "wiring", "title": "Wiring", "photo_stem": "wiring", "icon": "wiring", "items": [
                _service("Wiring Installation", 115, "4.75 (3.2K+)", 1, details=["Concealed conduit internal wiring for a new connection"]),
                _service("Wireless CCTV Installation", 290, "4.65 (633)", 2),
            ],
        },
        {
            "id": "doorbell", "title": "Door bell", "photo_stem": "doorbell", "icon": "doorbell", "items": [
                _service("Doorbell Installation / Replacement", 96, "4.82 (1.8K+)", 1),
            ],
        },
        {
            "id": "ev-charger", "title": "EV Charger", "photo_stem": "ev-charger", "icon": "charger", "items": [
                _service("EV Charger Installation", 878, "4.72 (91)", 1, "1 hr 30 mins", ["Installation of one charging station and switch box"], "Eco"),
            ],
        },
        {
            "id": "air-cooler", "title": "Air Cooler", "photo_stem": "air-cooler", "icon": "cooler", "items": [
                _service("Air Cooler Check Up", 249, "4.67 (74)", 1),
                _service("Air Cooler Full Service", 599, "4.79 (43)", 2),
            ],
        },
    ]

    category_emojis = {
        "geyser": "♨", "consultation": "⚡", "light": "💡", "festive-lights": "✨",
        "switch-socket": "🔌", "fan": "🌀", "tv": "▣", "mcb-fuse": "⚙",
        "inverter": "🔋", "wiring": "〰", "doorbell": "🔔", "ev-charger": "⚡", "air-cooler": "❄",
    }
    for category in categories:
        category["emoji"] = category_emojis[category["id"]]
        category["photo_ext"] = "png" if category["id"] == "inverter" and any(item["image"] == 5 for item in category["items"]) else "jpeg"

    return {
        "categories": categories,
        "quick_categories": [
            {"id": c["id"], "title": c["title"], "icon": c["icon"], "emoji": c["emoji"]}
            for c in categories
        ],
        "hero_photo": "hero-03.jpeg",
        "total_services": sum(len(category["items"]) for category in categories),
    }
