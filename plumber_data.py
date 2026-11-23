"""Service catalogue transcribed from the NoBroker Plumber Figma screen."""


FIGMA = "plumber/figma/"


def _service(name, price, rating, description, photo, starting=False, duration=""):
    return {
        "name": name,
        "price": price,
        "rating": rating,
        "description": description,
        "photo_path": FIGMA + photo + ".png",
        "starting": starting,
        "duration": duration,
    }


def page_data():
    categories = [
        {"id": "toilet", "title": "Toilet", "icon": "🚽", "photo_path": FIGMA + "f0352772-3b4e-4947-83cf-7d14b40cdceb.png", "services": [
            _service("Flush Tank Repair", 190, "4.7 · 12.5K+", "Repair of common flush tank problems and water flow issues.", "61ec20ed-d3fc-4855-a5c3-1b24203e9f9b", True, "1 hr"),
            _service("Jet Spray Replace / Install / Repair", 189, "4.8 · 9.2K+", "Repair, replacement or installation of a jet spray.", "54ee96d1-6043-4c51-a142-cd7c5329a35b", True, "45 mins"),
            _service("Toilet Seat Cover", 142, "4.79 · 2.6K+", "Repair or installation of a toilet seat cover.", "519db5ec-08ab-4947-a4f9-8bbb44eaf885", True, "45 mins"),
            _service("External Flush Tank Replace / Install", 437, "4.77 · 963", "Replacement or installation of an external flush tank.", "08670af1-63a0-4c48-aee1-b89dc247733f", True, "1 hr"),
            _service("Toilet Repair", 585, "4.72 · 350", "Diagnosis and repair of common toilet problems.", "b864bab6-5017-4e3c-8131-38b602040817", True, "1 hr"),
            _service("Toilet Replacement / Installation", 1842, "4.64 · 439", "Replacement and installation of a toilet.", "b864bab6-5017-4e3c-8131-38b602040817", True, "1 hr"),
            _service("Toilet Pot Blockage Removal", 1173, "4.53 · 588", "Removal of blockage from the toilet pot.", "b7b08249-b508-486a-bbe1-bba1212c92d2", True, "45 mins"),
        ]},
        {"id": "tap-mixer", "title": "Tap & Mixer", "icon": "🚰", "photo_path": FIGMA + "78200bac-8244-47b8-a5b7-b7e37f663fd6.png", "services": [
            _service("Tap Repair", 246, "4.79 · 18.4K+", "Repair of leaking, loose or faulty taps.", "868cb5bd-1f31-4a9c-8415-5f9634f09e27", True, "30 mins"),
            _service("Tap Replace / Install", 246, "4.65 · 884", "Replacement or installation of a tap.", "18b2ebe7-329b-4b4f-8861-db34589ec155", True, "45 mins"),
            _service("Tap Accessory Install", 159, "4.81 · 1.3K+", "Installation of common tap accessories.", "810d168f-1388-4d77-a8b9-3bd99437da26", True, "30 mins"),
        ]},
        {"id": "basin-sink", "title": "Basin & Sink", "icon": "🫧", "photo_path": FIGMA + "e4e864de-9edf-455b-aec1-c3b3b766ed40.png", "services": [
            _service("Wash Basin Blockage Removal", 96, "4.76 · 4.5K+", "Clearing clogs or water flow blockages from the wash basin drain or pipe.", "7af9b436-1db9-4748-b736-988716894c98"),
            _service("Wash Basin Leakage Repair", 96, "4.74 · 5.8K+", "Fixing water leakage issues from the wash basin faucet, drain, or pipe connections.", "f148f561-3580-4476-8dd9-6dd19fecea0e"),
            _service("Wash Basin Installation", 455, "4.7 · 1.8K+", "Installation of all kinds of wash basins and sinks.", "b26fe442-0767-4836-b428-d60eb663ede4"),
        ]},
        {"id": "drainage-pipe", "title": "Drainage Pipe", "icon": "🌀", "photo_path": FIGMA + "7386cf79-e447-429d-b4be-86c78c849eef.png", "services": [
            _service("Drainage Pipe Blockage Removal", 145, "4.71 · 4.2K+", "Unclogging and removal of in-pipe blockage.", "9f2fb86b-7003-45de-a721-6f35e44ee6b9"),
            _service("Balcony Drain Blockage Removal", 339, "4.77 · 1.8K+", "Cleaning of drain and floor trap to remove blockage.", "f94d1732-2026-4f45-9aba-a92d61c1dfce"),
            _service("Drain Cover Installation", 193, "4.72 · 758", "Installation of a drain cover.", "397e016a-bce3-47d2-81ed-5fe014bbc5a1"),
        ]},
        {"id": "water-pipe", "title": "Water pipe connection", "icon": "🔩", "photo_path": FIGMA + "d4caa8d7-63c3-4d1d-bf67-757e56397005.png", "services": [
            _service("Washing Machine Inlet", 96, "4.83 · 4.4K+", "Installation or replacement of one inlet pipe.", "b87d2229-fd65-4935-9913-7ea667a8b4d3"),
            _service("Connection Hose Installation", 96, "4.75 · 2K+", "Installation of a connection hose for inlet and outlet linkage.", "1a9d931e-cb2c-4432-8ce3-97b676333a5c"),
            _service("Geyser Connection Pipe Repair", 96, "4.76 · 1.1K+", "Repair or replacement of geyser connecting pipes; geyser installation is not included.", "959a2763-44ce-4e08-a9e6-da8e4518b482"),
            _service("Shut-Off Valve Leakage", 96, "4.7 · 734", "Repair of a leaking shut-off valve.", "c39c242c-ec70-4133-8fac-14fbd9d40d73"),
        ]},
        {"id": "bath-shower", "title": "Bath & Shower", "icon": "🚿", "photo_path": FIGMA + "aff357ef-15ba-4bc6-a080-00c6eeb14691.png", "services": [
            _service("Minor Fittings Installation", 115, "4.73 · 765", "Covers small fittings such as towel hangers, holders, towel shelves, and soap dispensers.", "2af17771-0b2c-4021-a30a-8994ebcf8a5a"),
            _service("Bath Accessory Installation", 96, "4.68 · 239", "Installation of common bath accessories.", "a36c4053-b80f-41ae-8bd2-e444f3cb0ab0"),
            _service("Shower Filter Installation", 96, "4.85 · 513", "Installation of a shower filter.", "a5b8815b-38ae-452a-929b-df47ad69dd1d"),
            _service("Shower Repair", 96, "4.73 · 857", "Repair of shower fittings and water flow issues.", "70c0ca2a-e742-4f59-95a7-94bfa14ef22c"),
            _service("Shower Installation", 135, "4.79 · 1.5K+", "Installation of a wall or ceiling-mounted shower.", "49ff89d7-dce3-444b-9a0e-d5694715e4ba", True),
        ]},
        {"id": "book-plumber", "title": "Book a Plumber", "icon": "🧰", "photo_path": FIGMA + "2f2d65fa-c891-4deb-87a1-d7f3bcc2e14e.png", "services": [
            _service("At Home Consultation", 48, "4.68 · 19.8K+", "An expert plumber assesses the issue on arrival. Inspection amount is adjusted in the final price.", "c3f9d05d-ebc4-4bc8-828b-c5efb426d826", True),
        ]},
        {"id": "water-tank", "title": "Water Tank", "icon": "🛢️", "photo_path": FIGMA + "3817ff3b-b600-4a19-8101-f7e2e5d42592.png", "services": [
            _service("Pipeline Leakage Repair", 96, "4.68 · 1.6K+", "Repair of one faulty galvanized iron or PVC pipe.", "07b0c8df-020f-4795-82cf-96158c837e56"),
            _service("Motor Air Cavity Removal", 96, "4.5 · 479", "Removal of an air cavity from a water motor line.", "a6835722-469a-4795-8411-a64da7dd47ab"),
            _service("Overhead Tank Leakage Repair", 145, "4.45 · 202", "Leakage repair for an overhead tank and water level controller.", "ae0b54f8-e891-4f20-a063-4075e398568d"),
            _service("Overhead Tank Installation", 883, "4.66 · 95", "Installation of one overhead water tank.", "5dce71ee-5152-490f-a5d7-c875d4f36e29", True),
            _service("Motor Installation / Replacement", 436, "4.53 · 272", "Installation or replacement of a water motor.", "7856ec7b-48ed-4f4f-93f9-5f11209577ca", True),
        ]},
        {"id": "grouting", "title": "Grouting", "icon": "🧱", "photo_path": FIGMA + "fb06bb40-c7a0-4409-8a81-d777adf0c7c0.png", "services": [
            _service("Bathroom Grouting", 1800, "4.44 · 1.4K+", "Grouting and tile gap filling for one bathroom; machine work is not included.", "1ea5f740-073c-41b9-b3ae-e6e8bb1ddaa2"),
            _service("Kitchen Grouting", 1800, "4.63 · 434", "Grouting and tile gap filling for one kitchen; machine work is not included.", "3e61a70e-a326-4f7b-963b-c4d265d12d05"),
        ]},
    ]

    for category in categories:
        for service in category["services"]:
            service["duration"] = service["duration"] or "Visit scheduled after booking"

    return {
        "categories": categories,
        "total_services": sum(len(category["services"]) for category in categories),
        "hero_photo": FIGMA + "90fc69de-b7c8-44f7-aa9c-0b3dca563ad6.png",
        "vip_photo": FIGMA + "7296da62-41a7-4bea-baa6-152593c03b14.png",
        "vip_background": FIGMA + "310cb043-b56f-4adb-84ad-47d690bbb0ff.png",
    }
