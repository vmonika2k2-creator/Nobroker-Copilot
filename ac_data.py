"""AC service catalogue transcribed from the NoBroker Pune Figma screen."""

ASSET = "ac/figma/"


def _service(name, rating, reviews, price, description, photo, starting=True, options=2):
    return {
        "name": name,
        "rating": rating,
        "reviews": reviews,
        "price": price,
        "description": description,
        "photo_path": ASSET + photo + ".png",
        "starting": starting,
        "options": options,
    }


def page_data():
    categories = [
        {
            "id": "maintenance",
            "title": "AC Maintenance Service",
            "icon": "🧼",
            "sprite_left": 1203.81,
            "sprite_top": 8.79,
            "banner": ASSET + "ea2f052a-1495-4c5c-8cd4-471c333d0afd.png",
            "services": [
                _service("Foam Blast AC Service", "4.79", "72.4K+", 629, "Ultra Max Cooling · Deep cleaning with foam jet spray for faster and more efficient cooling.", "49135b03-5d71-4a9e-85e8-0792adc4eedd"),
                _service("Premium AC Service", "4.71", "82K+", 539, "High-pressure jet cleaning removes dust and debris to improve airflow.", "8066acaa-3214-4313-81db-446a03a17011"),
                _service("Anti Rust AC Service", "4.79", "4.5K+", 729, "Protects AC coils from corrosion and helps reduce the risk of gas leakage.", "7049cfcd-a986-4ac5-bbac-5d4880288e63"),
            ],
        },
        {
            "id": "repair",
            "title": "AC Repair",
            "icon": "🛠️",
            "sprite_left": 2377.52,
            "sprite_top": 8.79,
            "banner": ASSET + "b11ecf87-9e40-44ab-ba3b-4483c3418ade.png",
            "services": [
                _service("AC Inspection", "4.62", "34.9K+", 289, "Accurate diagnosis and a comprehensive inspection help detect and resolve AC issues efficiently.", "086a1d7a-d903-4011-ae50-f282cce5e290"),
                _service("Noise Reduction Repair", "4.75", "1.3K+", 349, "Indoor and outdoor units are checked to identify the cause of unusual AC noise.", "ad58a2f3-6054-4ea3-8fea-101c0c70067f"),
                _service("Water Leakage Repair", "4.81", "7.2K+", 519, "Inspection of water leakage, slope issues and drain blockages to find the cause.", "c123453d-a9b0-4f6b-bdb8-6b2f64a551c7"),
            ],
        },
        {
            "id": "installation",
            "title": "AC Installation / Uninstallation",
            "icon": "📐",
            "sprite_left": 30.1,
            "sprite_top": 17.59,
            "banner": ASSET + "9e87c7e6-71ac-4110-9c8a-47a538c59a86.png",
            "services": [
                _service("AC Uninstallation", "4.78", "15.4K+", 629, "Safe dismantling of indoor and outdoor AC units.", "4c7583ff-d4fb-4ad9-9a61-60a826251070"),
                _service("AC Installation", "4.56", "17.3K+", 779, "Professional installation of both indoor and outdoor units.", "c58b9f3b-55b8-4fff-9a39-9a69d5429b9e"),
            ],
        },
        {
            "id": "gas-charging",
            "title": "AC Gas Charging",
            "icon": "❄️",
            "sprite_left": 3551.24,
            "sprite_top": 2.93,
            "banner": ASSET + "bc9a52a1-e523-4174-b24a-b26b720732fb.png",
            "services": [
                _service("AC Gas Refill & Check-Up", "4.68", "32.7K+", 2749, "Comprehensive inspection, gas leak detection and repair, plus refrigerant refill for reliable system performance.", "44b4c244-3ae7-49a8-b312-15274bcb9e9a", starting=False),
            ],
        },
    ]
    return {
        "categories": categories,
        "total_services": sum(len(category["services"]) for category in categories),
        "hero_photo": ASSET + "c67dbe71-83d5-4746-bed8-0f1d346342d8.png",
        "hero_promo": ASSET + "5ac6523e-e3ef-4131-85bb-a3967e63f49b.png",
        "hero_sprite": ASSET + "ee3c1a66-9a9e-49f8-8c09-11b9603a8fcd.png",
    }
