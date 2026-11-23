"""Carpentry catalogue content based on the NoBroker Carpenter Figma screen."""


def _service(name, price, rating, description, photo):
    return {
        "name": name,
        "price": price,
        "rating": rating,
        "description": description,
        "photo": photo,
    }


def page_data():
    categories = [
        {
            "id": "door", "title": "Door", "icon": "🚪", "photo": "door",
            "services": [
                _service("Door Lock Repair & Install", 92, "4.81 · 8.2K+", "Repair, installation, or replacement of a door lock", "door"),
                _service("Wooden Door Repair", 193, "4.78 · 5.7K+", "Alignment fixing, sanding, scraping and door jamb repair", "door"),
                _service("Sliding Door Repair", 290, "4.72 · 1.4K+", "Repair of sliding door channels or bearing replacement", "door"),
                _service("Overhead Door Closure", 174, "4.68 · 500", "Installation of one overhead door closure", "door"),
                _service("Door Dismantling", 243, "4.69 · 487", "Safe dismantling of a wooden door", "door"),
                _service("Wooden Door Installation", 775, "4.38 · 421", "Installation and alignment of a wooden door", "door"),
            ],
        },
        {
            "id": "drill-hang", "title": "Drill & hang", "icon": "🪛", "photo": "assembly",
            "services": [
                _service("Wooden Shelf Installation", 193, "4.83 · 2.9K+", "Secure installation of a wooden wall shelf", "assembly"),
                _service("Bathroom Mirror Installation", 115, "4.83 · 2.4K+", "Wall mounting and alignment for a bathroom mirror", "cabinet"),
                _service("Towel Rod Installation", 96, "4.78 · 1.5K+", "Drilling and installation of a towel rod", "cabinet"),
                _service("Glass Shelf Installation", 135, "4.74 · 787", "Installation of a wall-mounted glass shelf", "cabinet"),
                _service("Bath Fittings Installation", 145, "4.77 · 837", "Fitting and securing bathroom accessories", "cabinet"),
                _service("Drill (Per Hole)", 71, "4.86 · 11.8K+", "Drilling for hooks, shelves and other wall fittings", "assembly"),
            ],
        },
        {
            "id": "cupboard-drawer", "title": "Cupboard and Drawer", "icon": "🗄️", "photo": "cabinet",
            "services": [
                _service("Channel Installation / Replacement", 122, "4.77 · 2.8K+", "Installation or replacement of a drawer channel", "cabinet"),
                _service("Channel Repair", 125, "4.80 · 3K+", "Repair of jammed or misaligned drawer channels", "cabinet"),
                _service("Cupboard Hinge Repair / Replacement", 125, "4.81 · 7.1K+", "Repair or replacement of cupboard hinges", "cabinet"),
                _service("Cupboard Sliding Door Repair", 261, "4.80 · 1.4K+", "Fixing sliding cupboard doors and tracks", "cabinet"),
                _service("Cupboard Handle Installation", 86, "4.80 · 1.3K+", "Installation or replacement of cupboard handles", "cabinet"),
                _service("Cupboard & Drawer Locks", 92, "4.75 · 959", "Repair and installation of cupboard locks", "cabinet"),
            ],
        },
        {
            "id": "windows-curtain", "title": "Windows & curtain", "icon": "🪟", "photo": "door",
            "services": [
                _service("Curtain Rod Installation", 145, "4.82 · 4.9K+", "Mounting and alignment of a curtain rod", "assembly"),
                _service("Window Closing (Post-AC Removal)", 164, "4.71 · 211", "Closing and finishing the window opening after AC removal", "door"),
                _service("Window AC Frame Installation", 339, "4.47 · 77", "Installation of a window air-conditioner frame", "assembly"),
                _service("Shower Curtain Rod Installation", 145, "4.72 · 147", "Mounting and securing of a shower curtain rod", "cabinet"),
                _service("Window Hinge Installation", 145, "4.77 · 178", "Fitting or replacing window hinges", "door"),
                _service("Window Misalignment / Jam Repair", 193, "4.55 · 181", "Adjustment for a stuck or misaligned window", "door"),
            ],
        },
        {
            "id": "bed", "title": "Bed", "icon": "🛏️", "photo": "assembly",
            "services": [
                _service("Cot Assembly", 387, "4.82 · 120", "Assembly and tightening of a cot frame", "assembly"),
                _service("Bed Support Repair", 290, "4.79 · 1.8K+", "Repair of bed support, slats or joints", "assembly"),
                _service("Headboard Repair", 193, "4.76 · 421", "Fixing a loose or damaged headboard", "assembly"),
                _service("Loft Bed / Bunk Bed Assembly", 901, "4.80 · 81", "Assembly and safety check for a bunk or loft bed", "assembly"),
                _service("Single Bed Assembly", 436, "4.89 · 488", "Assembly of a single bed frame", "assembly"),
                _service("Double Bed Assembly", 581, "4.89 · 2.3K+", "Assembly of a double bed frame", "assembly"),
            ],
        },
        {
            "id": "furniture-assembly", "title": "Furniture Assembly", "icon": "🪑", "photo": "assembly",
            "services": [
                _service("Study / Workspace Table Assembly", 436, "4.87 · 1.2K+", "Assembly of a study or workspace table", "assembly"),
                _service("Table / Chair Wheel Fitting", 48, "4.72 · 575", "Fitting or replacement of furniture wheels", "assembly"),
                _service("Plastic Buffer Installation", 48, "4.63 · 231", "Installation of protective furniture buffers", "cabinet"),
                _service("Utensil Rack Assembly", 261, "4.84 · 77", "Assembly and fitting of a kitchen utensil rack", "cabinet"),
                _service("Wall Cabinet Assembly & Installation", 242, "4.69 · 521", "Assembly and installation of wall cabinets", "cabinet"),
                _service("Shoe Cabinet Assembly", 290, "4.80 · 559", "Assembly and placement of a shoe cabinet", "assembly"),
            ],
        },
        {
            "id": "wardrobe", "title": "Wardrobe", "icon": "👔", "photo": "wardrobe",
            "services": [
                _service("Single Door Wardrobe Assembly", 581, "4.68 · 91", "Assembly of a single-door wardrobe", "wardrobe"),
                _service("Double Door Wardrobe Assembly", 824, "4.81 · 197", "Assembly and alignment of a double-door wardrobe", "wardrobe"),
                _service("Three Door Wardrobe Assembly", 921, "4.76 · 323", "Assembly and alignment of a three-door wardrobe", "wardrobe"),
                _service("Four Door Wardrobe Assembly", 1018, "4.72 · 126", "Assembly and alignment of a four-door wardrobe", "wardrobe"),
            ],
        },
    ]

    add_ons = [
        {"name": "At Home Consultation", "price": 48, "description": "Get an expert assessment and an upfront quote."},
        {"name": "IKEA Wardrobe Assembly", "price": 581, "description": "Professional assembly for IKEA wardrobes."},
        {"name": "IKEA Beds Assembly", "price": 484, "description": "Assembly and alignment for IKEA beds."},
        {"name": "IKEA Tables / Drawers Assembly", "price": 193, "description": "Assembly of IKEA tables and drawer units."},
        {"name": "IKEA Sofa Assembly", "price": 436, "description": "Assembly of IKEA sofa furniture."},
        {"name": "TV Installation", "price": 481, "description": "Wall-mounted TV installation service."},
        {"name": "TV Uninstallation", "price": 105, "description": "Careful removal of a wall-mounted TV."},
        {"name": "Ceiling Mounted Hanger Installation", "price": 624, "description": "Installation of a ceiling-mounted hanger."},
        {"name": "Wall / Door Hanger Installation", "price": 115, "description": "Installation of a wall or door hanger."},
    ]

    for category in categories:
        category["photo_path"] = {
            "door": "carpenter/cabinet-repair.jpg",
            "assembly": "carpenter/furniture-assembly.webp",
            "cabinet": "carpenter/cabinet-repair.jpg",
            "wardrobe": "carpenter/wardrobe-assembly.jpg",
        }[category["photo"]]
        for service in category["services"]:
            service["starting"] = service["name"] in {
                "Drill (Per Hole)",
                "Cupboard & Drawer Locks",
                "Single Bed Assembly",
                "Double Bed Assembly",
                "Study / Workspace Table Assembly",
                "Wall Cabinet Assembly & Installation",
                "Shoe Cabinet Assembly",
            }
            service["photo_path"] = {
                "door": "carpenter/cabinet-repair.jpg",
                "assembly": "carpenter/furniture-assembly.webp",
                "cabinet": "carpenter/cabinet-repair.jpg",
                "wardrobe": "carpenter/wardrobe-assembly.jpg",
            }[service["photo"]]

    return {
        "categories": categories,
        "add_ons": add_ons,
        "total_services": sum(len(category["services"]) for category in categories),
    }
