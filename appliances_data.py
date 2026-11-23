"""Home appliance service catalogue based on the linked NoBroker page."""

ASSET = "appliences/"


def _service(name, rating, reviews, price, description, photo, options=1):
    return {
        "name": name,
        "rating": rating,
        "reviews": reviews,
        "price": price,
        "description": description,
        "photo_path": ASSET + photo,
        "options": options,
    }


def page_data():
    categories = [
        {
            "id": "washing-machine", "title": "Washing Machine", "icon": "🧺",
            "banner": ASSET + "washing-machine-banner.webp",
            "services": [
                _service("Washing Machine Checkup", "4.80", "13.1K+", 199, "Complete diagnosis of the washing machine. Spare parts are charged separately; service warranty of 180 days.", "washing-machine-checkup.webp", 3),
                _service("Washing Machine Installation", "4.84", "2.3K+", 359, "Professional installation and setup for your washing machine.", "washing-machine-installation.webp"),
                _service("Washing Machine Uninstallation", "4.83", "100+", 359, "Safe disconnection and removal of your washing machine.", "washing-machine-banner.webp"),
                _service("Washing Machine Descaling Service", "4.75", "30+", 799, "Remove limescale and hard-water buildup from internal components.", "washing-machine-checkup.webp", 2),
                _service("Washing Machine Deep-Clean Service", "4.72", "163+", 958, "Deep cleaning of the drum, filters, and internal parts with a jet spray.", "washing-machine-installation.webp", 2),
            ],
        },
        {
            "id": "refrigerator", "title": "Refrigerator", "icon": "🧊",
            "banner": ASSET + "refrigerator-banner.webp",
            "services": [
                _service("Double Door Check-Up", "4.74", "3.9K+", 193, "Complete diagnosis of your refrigerator to identify repair needs. Spare parts are charged separately; 180-day service warranty.", "refrigerator-checkup.webp", 2),
                _service("Single Door Fridge Check-Up", "4.82", "3.6K+", 193, "Inspection and diagnosis for single-door refrigerators.", "refrigerator-banner.webp"),
                _service("Side By Side Door Check-Up", "4.66", "401+", 193, "Complete diagnosis for side-by-side refrigerators, with a 180-day service warranty.", "refrigerator-checkup.webp", 2),
            ],
        },
        {
            "id": "water-purifier", "title": "Water Purifier", "icon": "💧",
            "banner": ASSET + "water-purifier-banner.webp",
            "services": [
                _service("Water Purifier Check-Up", "4.75", "4K+", 299, "Inspection and diagnosis of your water purifier.", "water-purifier-service.webp"),
                _service("Water Purifier Filter Check-Up", "4.76", "2.5K+", 299, "Check filter condition and purifier performance.", "water-purifier-checkup.webp"),
                _service("Water Purifier Regular Service", "4.84", "416+", 1259, "Cleaning of the filter, sediment, and carbon filters.", "water-purifier-service.webp"),
                _service("Water Purifier Full Service", "4.70", "500+", 2499, "Complete purifier service with filter, membrane, and TDS testing.", "water-purifier-checkup.webp"),
                _service("Water Purifier Installation", "4.80", "5.5K+", 419, "Professional water purifier installation and setup.", "water-purifier-service.webp"),
                _service("Water Purifier Uninstallation", "4.87", "527+", 359, "Safe disconnection and removal of your water purifier.", "water-purifier-checkup.webp"),
            ],
        },
        {
            "id": "microwave", "title": "Microwave", "icon": "♨️",
            "banner": ASSET + "microwave-banner.webp",
            "services": [
                _service("Microwave Check-Up", "4.80", "2.4K+", 199, "A technician checks your microwave and diagnoses the issue. Parts are charged separately.", "microwave-banner.webp"),
            ],
        },
    ]
    return {
        "categories": categories,
        "total_services": sum(len(category["services"]) for category in categories),
        "hero_photo": ASSET + "appliance-banner.webp",
    }
