from flask import Flask, request, jsonify, render_template, send_from_directory
import os, json
from full_house_data import page_data
from kitchen_data import page_data as kitchen_page_data
from sofa_data import page_data as sofa_page_data
from bathroom_data import page_data as bathroom_page_data
from premium_painting_data import page_data as premium_painting_page_data
from painting_services_data import page_data as painting_services_page_data
from electrician_data import page_data as electrician_page_data
from carpenter_data import page_data as carpenter_page_data
from plumber_data import page_data as plumber_page_data
from appliances_data import page_data as appliances_page_data
from ac_data import page_data as ac_page_data

app = Flask(__name__, template_folder="template")

# ── Per-category: covers / doesn't cover / why ───────────────────────
_SERVICE_COVERAGE = {
    'Full House Cleaning Services': {
        'covers': ['All rooms — floor to ceiling', 'Kitchen slab & bathroom tiles', 'Fans, switches & fixtures', 'Balcony & utility area'],
        'doesnt': ['Inside appliances (oven, fridge)', 'Pest control or fumigation', 'Structural repairs or painting'],
        'why': 'Best value when multiple rooms need attention — one visit, one team, coordinated schedule.',
    },
    'Kitchen Services': {
        'covers': ['Chimney & exhaust degreasing', 'Tile & cabinet surface cleaning', 'Sink, tap & drain area', 'Stove and cooking slab'],
        'doesnt': ['Inside fridge or microwave', 'Plumbing repairs or pipe work', 'Pest or cockroach treatment'],
        'why': 'Kitchen grease needs specialist tools — standard mopping cannot remove built-up oil and grime.',
    },
    'Sofa Cleaning Services': {
        'covers': ['Fabric & leather sofa deep-clean', 'Cushions & armrests', 'Stain treatment & deodorising', 'Recliner & L-shaped sofas'],
        'doesnt': ['Structural frame repairs', 'Replacement fabric or foam', 'Carpet or rug cleaning'],
        'why': 'Sofas harbour allergens and odours that vacuum cleaners miss — professional extraction removes them.',
    },
    'Bathroom Cleaning Services': {
        'covers': ['Toilet, basin & shower fittings', 'Floor & wall tiles + grout', 'Taps, showerhead & drain', 'Mirror & exhaust fan'],
        'doesnt': ['Plumbing repairs or pipe leaks', 'Tile replacement or re-grouting', 'Waterproofing treatment'],
        'why': 'Hard water stains and mould need acid-based cleaners that household products cannot safely match.',
    },
    'Painting Services': {
        'covers': ['Interior walls & ceiling', 'Primer + 2 coats of paint', 'Standard putty & sanding', 'Furniture & floor protection'],
        'doesnt': ['Exterior or terrace surfaces', 'Textured or designer finishes', 'Wood polishing or metal work', 'Seepage repair before painting'],
        'why': 'Fresh paint is the highest-impact visible change — instantly makes a room look brand new.',
    },
    'Premium Painting': {
        'covers': ['Premium brand paints (Asian, Berger)', 'Texture & designer finishes', 'Deep putty + multiple coat process', 'Full protection of furniture'],
        'doesnt': ['Structural crack or seepage repair', 'Exterior painting', 'POP or false ceiling work'],
        'why': 'Premium paint lasts 2–3x longer than standard — saves money by not repainting in 2 years.',
    },
    'Electrician': {
        'covers': ['Switch & socket repair or replace', 'Fan installation & repair', 'Light fixture fitting', 'MCB or fuse box issues', 'Basic wiring check'],
        'doesnt': ['Full home rewiring', 'Generator or inverter install', 'DB board upgrade', 'Solar panel work'],
        'why': 'Electrical faults are fire hazards — a certified electrician spots issues your eye cannot.',
    },
    'Plumber': {
        'covers': ['Tap & flush repair or replace', 'Pipe leak fix', 'Drain unblocking', 'Wash-basin & sink fittings', 'Water pressure issues'],
        'doesnt': ['Underground pipe replacement', 'Water tank cleaning', 'Bathroom tile removal', 'Sewage line work'],
        'why': 'Even a small drip wastes 90 litres per day — fixing it now saves significantly on your water bill.',
    },
    'Carpenter': {
        'covers': ['Door & hinge repair', 'Wardrobe & cabinet fixing', 'Furniture assembly', 'Drawer & lock repair', 'Basic woodwork'],
        'doesnt': ['Custom furniture manufacturing', 'Full kitchen modular work', 'Structural woodwork'],
        'why': 'Loose hinges and stuck drawers worsen over time — an early fix prevents costly replacement.',
    },
    'AC Services': {
        'covers': ['AC servicing & filter cleaning', 'Gas refilling if needed', 'Installation & uninstallation', 'Remote & thermostat check'],
        'doesnt': ['Compressor replacement', 'Major PCB repair', 'Electrical wiring to AC point'],
        'why': 'An unserviced AC uses 25% more electricity — one service visit pays for itself in 2 months.',
    },
    'Appliance Services': {
        'covers': ['Washing machine, fridge, geyser', 'Microwave & oven repair', 'Basic diagnostics included', 'Common part replacement'],
        'doesnt': ['Major motor or compressor overhaul', 'Appliance disposal or shifting', 'Installation of new appliances'],
        'why': 'Repair is 60–80% cheaper than replacement for most common appliance faults.',
    },
}

_DEFAULT_COVERAGE = {
    'covers': ['Professional inspection included', 'Trained and verified technician', 'Standard tools and consumables'],
    'doesnt': ['Structural repairs', 'Replacement of major components', 'Work outside agreed scope'],
    'why': 'NoBroker-verified professionals carry a service warranty — you only pay after the job is done.',
}

def _get_coverage(name: str, category: str) -> dict:
    return (_SERVICE_COVERAGE.get(name)
            or _SERVICE_COVERAGE.get(category)
            or _DEFAULT_COVERAGE)

# ── Feedback storage ──────────────────────────────────────────────────
FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), 'feedback.json')

def _load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return []

def _save_feedback(record: dict):
    data = _load_feedback()
    data.append(record)
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# Temporary in-memory storage for bookings
bookings_list = []


@app.route('/assets/<path:filename>')
def assets(filename):
    """Serve the local catalogue assets referenced by the page data modules."""
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'assets'), filename)

# The four services shown in the Home Cleaning popup
cleaning_services = [
    {"id": "full-house", "name": "Full House Cleaning Services", "icon": "🏠", "desc": "Deep clean of every room, floor to ceiling"},
    {"id": "kitchen", "name": "Kitchen Services", "icon": "🍳", "desc": "Degreasing of tiles, slab, stove, chimney and cabinets"},
    {"id": "sofa", "name": "Sofa Cleaning Services", "icon": "🛋️", "desc": "Vacuuming and shampooing for sofas, cushions and recliners"},
    {"id": "bathroom", "name": "Bathroom Cleaning Services", "icon": "🚿", "desc": "Tiles, fittings, toilet and drain deep cleaning"},
]

# The painting options shown in the Painting popup
painting_services = [
    {"id": "premium-painting", "name": "Premium Painting", "icon": "✨", "desc": "Premium-quality paints and a refined finish for your home"},
    {"id": "painting-services", "name": "Painting Services", "icon": "🖌️", "desc": "Professional painting service for your home"},
]

# The trade options shown in the Electrician & Plumber popup
trade_services = [
    {"id": "electrician", "name": "Electrician", "icon": "⚡", "desc": "Repairs, switches, wiring and electrical installation"},
    {"id": "plumber", "name": "Plumber", "icon": "🔧", "desc": "Tap, pipe, drain and bathroom plumbing repairs"},
    {"id": "carpenter", "name": "Carpenter", "icon": "🪚", "desc": "Furniture assembly, fittings and woodwork repairs"},
]

# The two choices shown in the AC & Appliance Repair popup
appliance_services = [
    {"id": "ac-services", "name": "AC Services", "icon": "❄️", "desc": "AC repair, servicing, installation and uninstallation"},
    {"id": "appliance-services", "name": "Appliance Services", "icon": "🔌", "desc": "Repair and installation for common home appliances"},
]


def _copilot_catalog():
    """Build a small local retrieval index from the existing service catalogues."""
    records = []
    def add_sections(data, detail_url):
        for section in data.get("sections", []):
            for item in section.get("items", []):
                records.append({"name": item["name"], "category": section["title"],
                                "price": item.get("price", 0), "duration": item.get("duration", ""),
                                "rating": item.get("rating"), "details": item.get("includes", []),
                                "detail_url": detail_url, "image": item.get("image") or item.get("photo")})

    def add_categories(data, detail_url):
        for category in data.get("categories", []):
            for item in category.get("items", category.get("services", [])):
                records.append({"name": item["name"], "category": category["title"],
                                "price": item.get("price", 0), "duration": item.get("duration", ""),
                                "rating": item.get("rating"),
                                "details": item.get("details", [item.get("description", "")]),
                                "detail_url": detail_url, "image": item.get("photo_path") or item.get("photo")})

    add_sections(page_data(), "/full-house-cleaning")
    add_sections(kitchen_page_data(), "/kitchen-cleaning")
    add_sections(sofa_page_data(), "/sofa-cleaning")
    add_sections(bathroom_page_data(), "/bathroom-cleaning")
    add_categories(electrician_page_data(), "/electrician")
    add_categories(carpenter_page_data(), "/carpenter")
    add_categories(plumber_page_data(), "/plumber")
    for item in appliances_page_data().get("categories", []):
        for service in item.get("services", []):
            records.append({"name": service["name"], "category": item["title"], "price": service.get("price", 0),
                            "duration": "", "rating": service.get("rating"),
                            "details": [service.get("description", "")], "detail_url": "/appliances",
                            "image": service.get("photo")})
    for service in painting_services_page_data().get("services", []):
        records.append({"name": service["title"], "category": "Painting Services", "price": 2000,
                        "duration": "", "rating": "4.7", "details": service.get("points", []),
                        "detail_url": "/painting-services", "image": service.get("photo")})
    return records


COPILOT_CATALOG = _copilot_catalog()

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NoBroker Home Services Clone</title>
    <!-- Tailwind CSS (preflight off so the existing styles stay the same) -->
    <script>tailwind = { config: { corePlugins: { preflight: false } } };</script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: Inter, Arial, sans-serif; }
        body { background-color: #f4f6f9; color: #333; }
        .navbar { display: flex; justify-content: space-between; align-items: center; background: #fff; padding: 15px 40px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .logo strong { color: #fd3752; font-size: 1.2rem; }
        .nav-right { display: flex; align-items: center; gap: 20px; font-size: 0.9rem; }
        .nav-right span, .nav-right select { cursor: pointer; font-weight: 500; }
        .copilot-nav { border: 0; border-radius: 999px; padding: 9px 15px; background: #111827; color: #fff; font-weight: 700; cursor: pointer; }
        select { border: none; font-size: 0.9rem; outline: none; background: transparent; }
        .search-section { display: flex; justify-content: center; padding: 25px; }
        .search-box { background: #fff; width: 600px; padding: 12px 20px; border-radius: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); display: flex; gap: 10px; }
        .search-box input { border: none; outline: none; width: 100%; font-size: 1rem; }
        .container { max-width: 1100px; margin: 0 auto; padding: 10px 20px; }
        .hero-grid { display: grid; grid-template-columns: 1.2fr 1fr; gap: 30px; align-items: center; }
        .services-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center; }
        .service-item { cursor: pointer; transition: transform 0.2s; padding: 8px; border-radius: 10px; }
        .service-item:hover { transform: translateY(-4px); background: #eef1f6; }
        .badge { background: #fde8b9; color: #8a5a00; font-size: 0.7rem; font-weight: bold; padding: 2px 8px; border-radius: 10px; display: inline-block; margin-bottom: 5px; }
        .icon-circle { width: 60px; height: 60px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; margin: 0 auto 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
        .promo-banner { height: 240px; border-radius: 12px; background: linear-gradient(135deg, #2c5e50, #4a7c6d); display: flex; align-items: flex-end; overflow: hidden; }
        .promo-overlay { width: 100%; background: rgba(0,0,0,0.7); color: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
        .btn-teal { background: #009587; color: #fff; border: none; padding: 8px 20px; border-radius: 5px; font-weight: bold; cursor: pointer; }
        .offers-section { background: #fff; margin-top: 30px; padding: 25px; border-radius: 12px; }
        .offers-section h2 { text-align: center; margin-bottom: 20px; }
        .offers-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .offer-card { padding: 20px; border-radius: 12px; min-height: 150px; display: flex; flex-direction: column; justify-content: space-between; }
        .dark { background: #1a1a1a; color: #fff; }
        .light-green { background: #e6f7f2; color: #0b4f3e; }
        .light-blue { background: #eaf4fc; color: #164366; }
        button { align-self: flex-start; padding: 8px 16px; border-radius: 20px; border: 1px solid #ccc; background: #fff; font-weight: bold; cursor: pointer; }
        button:hover { opacity: 0.9; }

        /* Floating home-services badge */
        .help-badge {
            position: fixed;
            right: clamp(18px, 3vw, 42px);
            bottom: clamp(18px, 3vw, 36px);
            width: 154px;
            aspect-ratio: 1;
            z-index: 30;
            display: grid;
            place-items: center;
            border-radius: 50%;
            background: #0f5d42;
            box-shadow: 0 14px 30px rgba(14, 64, 46, .28);
            isolation: isolate;
            text-decoration: none;
            border: 0;
            padding: 0;
            cursor: pointer;
            transition: transform .2s ease, box-shadow .2s ease;
        }
        .help-badge:hover, .help-badge:focus-visible {
            transform: translateY(-4px) scale(1.03);
            box-shadow: 0 18px 35px rgba(14, 64, 46, .36);
            outline: none;
        }
        .help-badge::before {
            content: "";
            position: absolute;
            inset: 23px;
            border-radius: 50%;
            background: linear-gradient(145deg, #4d9a69, #347f5b);
            z-index: -1;
        }
        .help-badge__ring {
            position: absolute;
            inset: -2px;
            width: calc(100% + 4px);
            height: calc(100% + 4px);
            animation: help-badge-spin 14s linear infinite;
            transform-origin: center;
            pointer-events: none;
        }
        .help-badge__ring text {
            fill: #dce8d7;
            font: 700 13px Arial, sans-serif;
            letter-spacing: 1.4px;
        }
        .help-badge__icon {
            width: 64px;
            height: 64px;
            color: #f1ccd9;
        }
        @keyframes help-badge-spin {
            to { transform: rotate(360deg); }
        }
        @media (prefers-reduced-motion: reduce) {
            .help-badge__ring { animation-duration: 30s; }
        }
        @media (max-width: 600px) {
            .help-badge { width: 126px; right: 14px; bottom: 14px; }
            .help-badge__icon { width: 54px; height: 54px; }
            .help-badge__ring text { font-size: 12px; letter-spacing: 1px; }
        }

        /* Screen 2: role selection */
        .role-modal {
            display: none;
            position: fixed;
            inset: 0;
            z-index: 1100;
            place-items: center;
            padding: 24px;
            background: rgba(26, 26, 26, .18);
        }
        .role-modal.is-open { display: grid; }
        .role-modal__panel {
            position: relative;
            display: grid;
            grid-template-columns: 1fr 1fr;
            width: min(920px, 100%);
            min-height: 560px;
            overflow: hidden;
            border-radius: 24px;
            background: #fff;
            box-shadow: 0 24px 70px rgba(35, 27, 38, .22);
        }
        .role-option {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 34px;
            padding: 54px 56px;
            text-align: center;
        }
        .role-option--owner { background: #fff3ea; color: #d4511b; }
        .role-option--tenant { background: #faeaff; color: #980cc2; }
        .role-option__image {
            width: min(300px, 75%);
            aspect-ratio: 1;
            border-radius: 28px;
            background: rgba(255,255,255,.48);
            display: grid;
            place-items: center;
            font-size: clamp(76px, 10vw, 132px);
            box-shadow: inset 0 0 0 1px rgba(255,255,255,.55);
        }
        .role-option h2 {
            max-width: 350px;
            font-family: 'Trebuchet MS', Arial, sans-serif;
            font-size: clamp(24px, 3vw, 36px);
            line-height: 1.08;
            font-weight: 500;
        }
        .role-option button {
            color: #fff;
            border: 0;
            padding: 13px 25px;
            border-radius: 26px;
            font-size: 16px;
        }
        .role-option--owner button { background: #c2410c; }
        .role-option--tenant button { background: #980cc2; }
        .role-modal__close {
            position: absolute;
            top: 14px;
            right: 16px;
            z-index: 1;
            width: 38px;
            height: 38px;
            padding: 0;
            border: 0;
            border-radius: 50%;
            background: rgba(255,255,255,.82);
            color: #444;
            font-size: 24px;
            line-height: 1;
        }
        .role-toast {
            position: fixed;
            left: 50%;
            bottom: 28px;
            z-index: 1200;
            transform: translate(-50%, 20px);
            padding: 12px 18px;
            border-radius: 24px;
            background: #1a1a1a;
            color: #fff;
            font-size: 14px;
            opacity: 0;
            pointer-events: none;
            transition: opacity .2s ease, transform .2s ease;
        }
        .role-toast.is-visible { opacity: 1; transform: translate(-50%, 0); }
        @media (max-width: 680px) {
            .role-modal__panel { grid-template-columns: 1fr; }
            .role-option { min-height: 390px; padding: 36px 24px; gap: 14px; }
            .role-option__image { width: 150px; font-size: 72px; }
            .role-option h2 { font-size: 25px; }
        }

        /* Owner inspection workspace, matching the reference screen */
        .owner-screen { display:none; position:fixed; inset:0; z-index:1150; overflow:auto; background:#fff5e5; color:#4b2415; }
        .owner-screen.is-open { display:block; }
        .owner-shell { width:min(1260px, 100%); margin:0 auto; padding:12px 34px 44px; }
        .owner-topbar { height:70px; display:flex; justify-content:space-between; align-items:center; gap:18px; border-bottom:1px solid #edd9bd; }
        .owner-brand { display:flex; align-items:center; gap:10px; font-size:17px; font-weight:900; color:#b94512; }
        .owner-brand small { display:block; color:#866c5b; font-size:8px; font-weight:500; }
        .owner-brand-mark { width:28px; height:28px; display:grid; place-items:center; border-radius:50%; background:#b94512; color:#fff; }
        .owner-nav { display:flex; align-items:center; gap:8px; }
        .owner-nav button, .owner-close { border:1px solid #e8b58c; background:#fffaf2; color:#5e301e; padding:9px 14px; border-radius:999px; font-size:11px; }
        .owner-close { cursor:pointer; }
        .owner-main { padding-top:22px; }
        .owner-kicker { display:inline-block; padding:7px 11px; border-radius:999px; background:#d8f2ea; color:#268273; font-size:10px; font-weight:800; }
        .owner-main h1 { margin:14px 0 8px; font-size:clamp(30px,4vw,46px); line-height:1.06; letter-spacing:-1px; color:#4b2415; }
        .owner-intro { font-size:12px; color:#765e50; margin-bottom:22px; }
        .owner-layout { display:grid; grid-template-columns:minmax(0,1fr) 300px; gap:18px; align-items:start; }
        .owner-board, .owner-summary { border:1px solid #efcda5; border-radius:18px; background:#fffdf9; box-shadow:0 8px 20px rgba(118,70,25,.07); }
        .owner-board { padding:18px; }
        .owner-step-title { display:flex; gap:10px; align-items:flex-start; margin-bottom:12px; }
        .owner-step-number { flex:0 0 24px; width:24px; height:24px; display:grid; place-items:center; border-radius:50%; background:#bd420e; color:#fff; font-size:12px; font-weight:900; }
        .owner-step-title h2 { margin:0; font-size:16px; color:#4b2415; }
        .owner-step-title p { margin:3px 0 0; color:#927866; font-size:10px; }
        .owner-services { display:flex; flex-wrap:wrap; gap:10px; padding:0 8px 14px; }
        .owner-service { width:62px; border:0; background:transparent; cursor:pointer; color:#6b4938; font-size:9px; text-align:center; }
        .owner-service-icon { width:44px; height:44px; display:grid; place-items:center; margin:0 auto 5px; border-radius:10px; background:#f7e8d0; font-size:23px; border:2px solid transparent; }
        .owner-service.is-selected .owner-service-icon { border-color:#c54310; background:#ffe1bd; }
        .owner-prompt { display:flex; gap:8px; border:1px solid #dfcdb7; border-radius:999px; padding:5px 8px 5px 14px; background:#fff; }
        .owner-prompt input { flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:11px; }
        .owner-prompt button { width:29px; height:29px; border:0; border-radius:50%; background:#bd420e; color:#fff; cursor:pointer; }
        .owner-damage { display:flex; flex-wrap:wrap; gap:7px; margin:12px 0 14px; padding-left:34px; }
        .owner-damage button { border:0; border-radius:999px; background:#ffd88c; color:#6b3b19; font-size:9px; padding:6px 10px; cursor:pointer; }
        .owner-damage button.is-selected { background:#bd420e; color:#fff; }
        .owner-photo-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; padding-left:34px; }
        .owner-photo { min-height:135px; position:relative; overflow:hidden; border:1px solid #e6c697; border-radius:12px; background:#f9eddc; }
        .owner-photo img { width:100%; height:100px; object-fit:cover; display:block; background:#f0d4aa; }
        .owner-photo strong, .owner-photo small { display:block; padding:4px 9px 0; font-size:10px; }
        .owner-photo small { padding-top:2px; color:#8c6f5b; font-size:8px; }
        .owner-photo.is-picked { outline:2px solid #bd420e; }
        .owner-photo input { display:none; }
        .owner-add { min-height:135px; display:grid; place-items:center; text-align:center; border:1px dashed #bd420e; border-radius:12px; background:#fff8ee; color:#bd420e; cursor:pointer; font-size:10px; }
        .owner-add span { display:block; font-size:23px; margin-bottom:8px; }
        .owner-photo-actions { display:flex; gap:10px; padding:14px 0 0 34px; }
        .owner-photo-actions button { border:1px solid #bd420e; background:#fff; color:#bd420e; padding:9px 14px; border-radius:999px; font-size:10px; cursor:pointer; }
        .owner-photo-actions button:first-child { background:#bd420e; color:#fff; }
        .owner-summary { padding:18px; position:sticky; top:15px; }
        .owner-summary h2 { margin:0 0 14px; font-size:16px; }
        .owner-summary-count { color:#bd420e; font-size:28px; font-weight:900; }
        .owner-summary-count small { color:#6f4d3c; font-size:10px; font-weight:500; }
        .owner-selection { display:grid; gap:7px; margin:12px 0 15px; }
        .owner-selection div { padding:11px; border-radius:10px; background:#fff0df; font-size:10px; }
        .owner-selection small { display:block; color:#9c7e69; margin-top:3px; }
        .owner-summary ul { padding:0 0 0 16px; color:#7b5c4a; font-size:10px; line-height:1.8; }
        .owner-estimate-button { width:100%; border:0; border-radius:999px; background:#148c84; color:#fff; padding:12px; font-weight:800; font-size:11px; cursor:pointer; }
        .owner-result { display:none; margin:14px 0 0 34px; padding:13px; border-radius:12px; background:#fff1d9; border:1px solid #e8c48f; color:#5e301e; font-size:11px; }
        .owner-result.is-visible { display:block; }
        .owner-price { font-size:25px; font-weight:900; color:#bd420e; margin:3px 0 6px; }
        .owner-note { font-size:10px; color:#876e5c; line-height:1.45; }
        .owner-shell { display:none; }
        .copilot-flow { min-height:100vh; padding:22px 34px 50px; color:#241c19; background:linear-gradient(135deg,#fff8ee 0%,#fffaf6 48%,#edf8f3 100%); }
        .copilot-flow__bar { width:min(1160px,100%); margin:auto; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #eadfd3; padding-bottom:18px; }
        .copilot-flow__brand { color:#bd420e; font-weight:900; font-size:18px; }
        .copilot-flow__brand small { display:block; color:#927866; font-size:9px; font-weight:500; margin-top:3px; }
        .copilot-flow__close { border:1px solid #e2cbb8; color:#6b4938; background:#fff; border-radius:999px; padding:9px 14px; cursor:pointer; }
        .copilot-flow__content { width:min(1160px,100%); margin:0 auto; padding-top:42px; }
        .copilot-flow__eyebrow { color:#238276; font-weight:800; font-size:12px; letter-spacing:.04em; }
        .copilot-flow h1 { max-width:750px; margin:10px 0 12px; color:#321e15; font-size:clamp(34px,5vw,58px); letter-spacing:-2px; line-height:1.02; }
        .copilot-flow__lead { max-width:620px; color:#745c4b; line-height:1.6; font-size:15px; }
        .room-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:15px; margin:30px 0 22px; }
        .room-card { position:relative; min-height:145px; border:1px solid #ead7c5; border-radius:20px; padding:18px; text-align:left; background:rgba(255,255,255,.78); cursor:pointer; transition:.2s; }
        .room-card:hover,.room-card.is-selected { border-color:#bd420e; transform:translateY(-2px); box-shadow:0 10px 24px rgba(141,76,28,.12); }
        .room-card.is-selected { background:#fff0df; box-shadow:inset 0 0 0 2px #bd420e; }
        .room-card__icon { font-size:30px; display:block; margin-bottom:16px; }
        .room-card strong { display:block; font-size:16px; color:#42261a; }
        .room-card small { display:block; color:#927866; margin-top:5px; font-size:11px; }
        .room-card__check { position:absolute; right:14px; top:14px; display:none; width:22px; height:22px; border-radius:50%; background:#bd420e; color:#fff; text-align:center; line-height:22px; }
        .room-card.is-selected .room-card__check { display:block; }
        .copilot-flow__actions { display:flex; gap:10px; align-items:center; flex-wrap:wrap; }
        .copilot-primary,.copilot-secondary { border-radius:999px; padding:13px 20px; cursor:pointer; font-weight:800; }
        .copilot-primary { border:0; background:#148c84; color:#fff; }
        .copilot-secondary { border:1px solid #d9c1ab; background:#fff; color:#6b4938; }
        .copilot-primary:disabled { cursor:not-allowed; opacity:.45; }
        .copilot-hint { color:#927866; font-size:11px; }
        .copilot-results { display:none; }
        .copilot-results.is-visible { display:block; }
        .copilot-back { border:0; background:transparent; color:#bd420e; padding:0; cursor:pointer; font-weight:800; }
        .copilot-results__head { display:flex; justify-content:space-between; gap:20px; align-items:end; flex-wrap:wrap; margin:20px 0; }
        .copilot-results__head h2 { margin:0; font-size:32px; color:#321e15; }
        .copilot-room-tabs { display:flex; gap:8px; flex-wrap:wrap; margin:18px 0; }
        .copilot-room-tab { border:1px solid #e1cdbb; background:#fff; color:#6b4938; border-radius:999px; padding:9px 14px; cursor:pointer; }
        .copilot-room-tab.is-active { background:#321e15; color:#fff; border-color:#321e15; }
        .copilot-context { display:grid; grid-template-columns:1.15fr 1fr; gap:16px; margin-bottom:18px; }
        .copilot-panel { border:1px solid #ead7c5; border-radius:18px; padding:18px; background:rgba(255,255,255,.84); }
        .copilot-panel h3 { margin:0 0 9px; color:#42261a; font-size:17px; }
        .copilot-panel p { color:#745c4b; font-size:13px; line-height:1.5; margin:0; }
        .copilot-checklist { display:grid; gap:9px; margin:0; padding:0; list-style:none; }
        .copilot-checklist li { color:#5d4639; font-size:12px; padding-left:22px; position:relative; }
        .copilot-checklist li:before { content:'✓'; position:absolute; left:0; color:#148c84; font-weight:900; }
        .service-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }
        .service-card { border:1px solid #ead7c5; border-radius:18px; overflow:hidden; background:#fff; box-shadow:0 8px 18px rgba(118,70,25,.06); }
        .service-card img { width:100%; height:120px; object-fit:cover; background:#f4e5d3; }
        .service-card__body { padding:14px; }
        .service-card h3 { margin:0 0 7px; color:#321e15; font-size:15px; line-height:1.25; }
        .service-card__meta { display:flex; justify-content:space-between; color:#6d5141; font-size:12px; margin-bottom:10px; }
        .service-card__why { padding:10px; margin:10px 0; border-radius:10px; background:#f2faf7; color:#397468; font-size:11px; line-height:1.45; }
        .service-card__footer { display:flex; justify-content:space-between; align-items:center; gap:8px; }
        .service-card__footer a,.service-card__footer button { color:#bd420e; font-size:11px; font-weight:800; border:0; background:transparent; padding:0; cursor:pointer; text-decoration:none; }
        .copilot-questions { display:none; margin-top:16px; }
        .copilot-questions.is-visible { display:block; }
        .copilot-question { display:flex; gap:10px; align-items:center; margin:9px 0; color:#5d4639; font-size:12px; }
        .copilot-question input { accent-color:#148c84; }
        .handover { display:none; margin-top:18px; padding:18px; border-radius:16px; border:1px solid #efb6a8; background:#fff0ed; color:#7d3022; }
        .handover.is-visible { display:flex; justify-content:space-between; align-items:center; gap:16px; flex-wrap:wrap; }
        .handover strong { display:block; margin-bottom:4px; }
        .chat-layout { display:grid; grid-template-columns:230px minmax(0,1fr); gap:22px; min-height:700px; }
        .room-sidebar { border-right:1px solid #eadfd3; padding:16px 18px 16px 0; }
        .room-sidebar__title { color:#927866; font-size:11px; font-weight:900; letter-spacing:.08em; text-transform:uppercase; margin:10px 0 14px; }
        .room-sidebar__rooms { display:grid; gap:7px; }
        .room-sidebar__room { display:flex; justify-content:space-between; align-items:center; width:100%; text-align:left; border:0; border-radius:12px; padding:12px 13px; background:transparent; color:#6d5141; cursor:pointer; font-weight:700; }
        .room-sidebar__room:hover,.room-sidebar__room.is-active { background:#fff0df; color:#bd420e; }
        .room-sidebar__room small { font-weight:500; color:#aa907f; }
        .room-sidebar__add { width:100%; margin-top:16px; border:1px dashed #d36b38; color:#bd420e; background:transparent; border-radius:12px; padding:10px; cursor:pointer; }
        .chat-main { min-width:0; display:flex; flex-direction:column; }
        .chat-main__header { display:flex; align-items:center; justify-content:space-between; gap:14px; padding:12px 0 22px; border-bottom:1px solid #eadfd3; }
        .chat-main__header h2 { margin:0; color:#4b2415; font-size:22px; }
        .chat-main__header small { display:block; color:#927866; font-size:11px; margin-top:4px; }
        .chat-canvas { flex:1; padding:24px 0 14px; }
        .chat-message { max-width:700px; border-radius:18px; padding:15px 18px; font-size:14px; line-height:1.55; }
        .chat-message--assistant { background:#fff; border:1px solid #ead7c5; color:#574237; box-shadow:0 6px 18px rgba(118,70,25,.04); }
        .chat-message--user { margin:12px 0 0 auto; background:#bd420e; color:#fff; }
        .chat-checklist { max-width:700px; margin:16px 0; border:1px solid #ead7c5; background:#fff; border-radius:18px; padding:16px; }
        .chat-checklist__title { display:flex; align-items:center; justify-content:space-between; gap:12px; margin-bottom:12px; color:#4b2415; font-weight:900; }
        .chat-checklist__rows { display:grid; gap:8px; }
        .chat-checklist__row { display:flex; align-items:center; gap:10px; padding:10px; background:#fffaf4; border-radius:10px; color:#5e4639; font-size:12px; }
        .chat-checklist__row input { accent-color:#bd420e; }
        .chat-checklist__row button { margin-left:auto; border:0; background:transparent; color:#b66c53; cursor:pointer; padding:3px 6px; }
        .chat-checklist__empty { color:#927866; font-size:12px; padding:6px; }
        .chat-composer { display:flex; align-items:center; gap:10px; border:1px solid #c9cdd2; border-radius:36px; padding:7px 10px 7px 18px; background:#fff; box-shadow:0 5px 18px rgba(70,50,35,.05); }
        .chat-composer textarea { flex:1; min-height:44px; max-height:100px; resize:vertical; border:0; outline:0; color:#514743; font:inherit; font-size:14px; padding-top:11px; }
        .chat-composer__send { flex:0 0 46px; width:46px; height:46px; border:0; border-radius:50%; background:#bd420e; color:#fff; cursor:pointer; font-size:20px; }
        .chat-actions { display:flex; gap:10px; flex-wrap:wrap; margin:14px 0 0; }
        .chat-action { border:1px solid #bd420e; border-radius:999px; padding:11px 16px; background:#fff; color:#bd420e; cursor:pointer; font-weight:800; font-size:12px; }
        .chat-action--primary { background:#bd420e; color:#fff; }
        .chat-deals { margin-top:28px; border-top:1px solid #eadfd3; padding-top:20px; }
        .chat-deals h3 { margin:0 0 12px; color:#4b2415; font-size:18px; }
        .plan-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:18px; }
        .plan-card { padding:15px; border:1px solid #ead7c5; border-radius:16px; background:#fff; }
        .plan-card.is-recommended { border:2px solid #bd420e; box-shadow:0 8px 20px rgba(189,66,14,.1); }
        .plan-card h4 { margin:0 0 5px; color:#4b2415; }
        .plan-card strong { color:#bd420e; }
        .plan-card p,.plan-card li { color:#765e50; font-size:11px; line-height:1.5; }
        .plan-card ul { margin:10px 0 0; padding-left:16px; }
        .package-row { display:flex; justify-content:space-between; gap:14px; align-items:center; padding:14px 16px; border:1px solid #d8ebe5; border-radius:14px; background:#f3fbf8; color:#397468; }
        .package-row strong { color:#246a5e; }
        @media (max-width:850px) { .chat-layout { grid-template-columns:1fr; gap:12px; } .room-sidebar { border-right:0; border-bottom:1px solid #eadfd3; padding:0 0 12px; } .room-sidebar__rooms { display:flex; overflow:auto; } .room-sidebar__room { min-width:max-content; } .room-sidebar__add { width:auto; margin:10px 0 0; } .plan-grid { grid-template-columns:1fr; } }
        @media (max-width:850px) { .copilot-flow { padding:16px 14px 35px; } .room-grid { grid-template-columns:repeat(2,1fr); } .service-grid,.copilot-context { grid-template-columns:1fr; } }
        @media (max-width:520px) { .room-grid { grid-template-columns:1fr 1fr; gap:9px; } .room-card { min-height:120px; padding:13px; } .room-card__icon { font-size:24px; margin-bottom:10px; } .room-card strong { font-size:13px; } }
        @media (max-width:800px) { .owner-shell { padding:8px 14px 35px; } .owner-layout { grid-template-columns:1fr; } .owner-summary { position:static; } .owner-photo-grid { grid-template-columns:repeat(2,1fr); } .owner-nav button:nth-child(-n+2) { display:none; } }

        /* Popup Modal Styles */
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); justify-content: center; align-items: center; z-index: 1000; }
        .modal-content { background: #fff; padding: 25px; border-radius: 12px; width: 400px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
        .modal-content h3 { margin-bottom: 15px; color: #fd3752; }
        .modal-content input { width: 100%; padding: 10px; margin: 8px 0 15px; border: 1px solid #ccc; border-radius: 6px; }
        .modal-actions { display: flex; justify-content: flex-end; gap: 10px; }
        .booking-card { background: #f4f6f9; padding: 10px; border-radius: 6px; margin-bottom: 10px; font-size: 0.9rem; border-left: 4px solid #009587; }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="logo">🚫 <strong>NOBROKER</strong> Home Services</div>
        <div class="nav-right">
            <select id="citySelect">
                <option value="Pune">Pune ▼</option>
                <option value="Hyderabad">Hyderabad ▼</option>
                <option value="Bangalore">Bangalore ▼</option>
                <option value="Mumbai">Mumbai ▼</option>
            </select>
            <span onclick="openBookingsModal()">📋 My Bookings (<span id="bookingCount">0</span>)</span>
            <button class="copilot-nav" type="button" onclick="window.location.href='/copilot'">✦ Copilot</button>
            <span onclick="openAuthModal('Sign Up')">Sign Up</span>
            <span onclick="openAuthModal('Log In')">Log In</span>
        </div>
    </div>

    <div class="search-section">
        <div class="search-box">
            🔍 <input type="text" id="searchInput" onkeyup="filterServices()" placeholder="Type to search services (e.g., Cleaning, Painting, AC)...">
        </div>
    </div>

    <div class="container">
        <div class="hero-grid">
            <div class="services-grid" id="servicesGrid">
                <div class="service-item" onclick="openCleaningPopup()"><span class="badge">Upto 60% Off*</span><div class="icon-circle">🧹</div><p>Home Cleaning</p></div>
                <div class="service-item" onclick="openBookingModal('Packers & Movers')"><span class="badge">Lowest Quote*</span><div class="icon-circle">🚚</div><p>Packers & Movers</p></div>
                <div class="service-item" onclick="openPaintingPopup()"><span class="badge">Flat 15% Off</span><div class="icon-circle">🖌️</div><p>Painting</p></div>
                <div class="service-item" onclick="openBookingModal('Sales Agreement')"><br><div class="icon-circle">📄</div><p>Sales Agreement</p></div>
                <div class="service-item" onclick="openBookingModal('Rental Agreement')"><span class="badge">Flat 30% Off*</span><div class="icon-circle">📝</div><p>Rental Agreement</p></div>
                <div class="service-item" onclick="openTradesPopup()"><br><div class="icon-circle">🔧</div><p>Electrician & Plumber</p></div>
                <div class="service-item" onclick="openBookingModal('Interior & Renovation')"><br><div class="icon-circle">🛋️</div><p>Interior & Renovation</p></div>
                <div class="service-item" onclick="openAppliancePopup()"><span class="badge">Upto 30% Off*</span><div class="icon-circle">❄️</div><p>AC & Appliance Repair</p></div>
            </div>
            <div class="promo-banner">
                <div class="promo-overlay">
                    <span>Cleaning Services</span>
                    <button class="btn-teal" onclick="openBookingModal('Deep Cleaning Service')">Book</button>
                </div>
            </div>
        </div>

        <div class="offers-section">
            <h2>Offers for you</h2>
            <div class="offers-grid">
                <div class="offer-card dark"><small>VIP MEMBERSHIP</small><h3>Save upto 15% off on Home Services</h3><button onclick="openBookingModal('VIP Membership Plan')">Buy Now</button></div>
                <div class="offer-card light-green"><small>Free Tenant Verification</small><h3>Upto 30% off on Rental agreement</h3><button onclick="openBookingModal('Rental Agreement (30% Off)')">Create Agreement</button></div>
                <div class="offer-card light-blue"><small>Festive Sale</small><h3>Flat 15% off on Home Painting</h3><button onclick="openBookingModal('Home Painting (15% Off)')">Explore Now</button></div>
            </div>
        </div>
    </div>

    <!-- Home Cleaning Popup (4 services) -->
    <div id="cleaningModal" class="modal">
        <div class="bg-white rounded-2xl p-6 w-[480px] max-w-[92vw] shadow-2xl">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-xl font-bold text-gray-900" style="margin:0;color:#111">Home Cleaning Services</h3>
                <button class="text-2xl leading-none border-0 bg-transparent" onclick="closeModals()">✕</button>
            </div>
            <p class="text-sm text-gray-500 mb-4">Choose a service to book</p>
            <div id="cleaningList" class="grid grid-cols-2 gap-3"></div>
        </div>
    </div>

    <!-- Painting Popup (2 services) -->
    <div id="paintingModal" class="modal">
        <div class="bg-white rounded-2xl p-6 w-[480px] max-w-[92vw] shadow-2xl">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-xl font-bold text-gray-900" style="margin:0;color:#111">Painting Services</h3>
                <button class="text-2xl leading-none border-0 bg-transparent" onclick="closeModals()">✕</button>
            </div>
            <p class="text-sm text-gray-500 mb-4">Choose a painting service</p>
            <div id="paintingList" class="grid grid-cols-2 gap-3"></div>
        </div>
    </div>

    <!-- Electrician & Plumber popup (three services) -->
    <div id="tradesModal" class="modal">
        <div class="bg-white rounded-2xl p-6 w-[480px] max-w-[92vw] shadow-2xl">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-xl font-bold text-gray-900" style="margin:0;color:#111">Electrician, Plumber &amp; Carpenter</h3>
                <button class="text-2xl leading-none border-0 bg-transparent" onclick="closeModals()" aria-label="Close">×</button>
            </div>
            <p class="text-sm text-gray-500 mb-4">Choose a home repair service</p>
            <div id="tradesList" class="grid grid-cols-2 gap-3"></div>
        </div>
    </div>

    <!-- AC & Appliance Repair popup (two service groups) -->
    <div id="applianceModal" class="modal">
        <div class="bg-white rounded-2xl p-6 w-[480px] max-w-[92vw] shadow-2xl">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-xl font-bold text-gray-900" style="margin:0;color:#111">AC &amp; Appliance Repair</h3>
                <button class="text-2xl leading-none border-0 bg-transparent" onclick="closeModals()" aria-label="Close">×</button>
            </div>
            <p class="text-sm text-gray-500 mb-4">Choose the type of service you need</p>
            <div id="applianceList" class="grid grid-cols-2 gap-3"></div>
        </div>
    </div>

    <!-- Booking Modal -->
    <div id="bookingModal" class="modal">
        <div class="modal-content">
            <h3 id="modalServiceTitle">Book Service</h3>
            <label>Your Name:</label>
            <input type="text" id="custName" placeholder="Enter your full name">
            <label>Phone Number:</label>
            <input type="text" id="custPhone" placeholder="Enter 10-digit mobile number">
            <label>Preferred Date:</label>
            <input type="date" id="custDate">
            <div class="modal-actions">
                <button onclick="closeModals()">Cancel</button>
                <button class="btn-teal" onclick="submitBooking()">Confirm Booking</button>
            </div>
        </div>
    </div>

    <!-- My Bookings Modal -->
    <div id="myBookingsModal" class="modal">
        <div class="modal-content">
            <h3>My Bookings</h3>
            <div id="bookingsContainer">No bookings yet.</div>
            <div class="modal-actions" style="margin-top:15px;">
                <button class="btn-teal" onclick="closeModals()">Close</button>
            </div>
        </div>
    </div>

    <!-- Screen 2 role selection -->
    <div id="roleModal" class="role-modal" role="dialog" aria-modal="true" aria-labelledby="roleModalTitle">
        <div class="role-modal__panel">
            <button class="role-modal__close" type="button" onclick="closeModals()" aria-label="Close role selection">×</button>
            <section class="role-option role-option--owner">
                <div class="role-option__image" aria-hidden="true">🏠</div>
                <h2 id="roleModalTitle">Need help with your home? Let us take care of it</h2>
                <button type="button" onclick="chooseRole('Owner')">I am the Owner</button>
            </section>
            <section class="role-option role-option--tenant">
                <div class="role-option__image" aria-hidden="true">🛠️</div>
                <h2>Need assistance with anything? Let us know how we can help.</h2>
                <button type="button" onclick="chooseRole('Tenant')">I am the Tenant</button>
            </section>
        </div>
    </div>

    <!-- Owner Screen / NoBroker Copilot inspection workflow -->
    <section id="ownerScreen" class="owner-screen" aria-label="Owner Copilot inspection workspace">
        <div class="copilot-flow" id="copilotFlow">
            <div class="copilot-flow__bar"><div class="copilot-flow__brand">NoBroker <small>Ghar Seva · Smart home help</small></div><button class="copilot-flow__close" type="button" onclick="closeOwnerScreen()">Close</button></div>
            <div class="copilot-flow__content">
                <section id="roomStep">
                    <div class="copilot-flow__eyebrow">✦ Copilot starts with what you know</div>
                    <h1>Which rooms need attention?</h1>
                    <p class="copilot-flow__lead">Choose one or more rooms. We’ll look up the services available for each room and ask only the questions that help narrow it down.</p>
                    <div class="room-grid" id="roomGrid">
                        <button class="room-card" data-room="Living room" onclick="toggleCopilotRoom(this)"><span class="room-card__icon">🛋️</span><strong>Living room</strong><small>Walls, sofa, fixtures</small><span class="room-card__check">✓</span></button>
                        <button class="room-card" data-room="Kitchen" onclick="toggleCopilotRoom(this)"><span class="room-card__icon">🍽️</span><strong>Kitchen</strong><small>Tiles, cabinets, plumbing</small><span class="room-card__check">✓</span></button>
                        <button class="room-card" data-room="Bathroom" onclick="toggleCopilotRoom(this)"><span class="room-card__icon">🚿</span><strong>Bathroom</strong><small>Fittings, tiles, seepage</small><span class="room-card__check">✓</span></button>
                        <button class="room-card" data-room="Bedroom" onclick="toggleCopilotRoom(this)"><span class="room-card__icon">🛏️</span><strong>Bedroom</strong><small>Paint, carpentry, AC</small><span class="room-card__check">✓</span></button>
                        <button class="room-card" data-room="Balcony" onclick="toggleCopilotRoom(this)"><span class="room-card__icon">🌿</span><strong>Balcony</strong><small>Flooring, paint, cleaning</small><span class="room-card__check">✓</span></button>
                        <button class="room-card" data-room="Pooja room" onclick="toggleCopilotRoom(this)"><span class="room-card__icon">🪔</span><strong>Pooja room</strong><small>Cleaning and paint</small><span class="room-card__check">✓</span></button>
                    </div>
                    <div class="owner-prompt" style="max-width:680px;margin-bottom:18px"><input id="copilotNote" placeholder="Anything you’ve noticed? e.g. tap leaking, damp wall, sofa stain"><span class="copilot-hint">Optional</span></div>
                    <div class="copilot-flow__actions"><button class="copilot-primary" id="continueRooms" onclick="continueCopilotRooms()" disabled>Continue with selected rooms →</button><span class="copilot-hint">You can add or switch rooms later</span></div>
                </section>
                <section id="resultsStep" class="copilot-results">
                    <div class="chat-layout">
                        <aside class="room-sidebar"><button class="copilot-back" onclick="backToRoomStep()">← Change rooms</button><div class="room-sidebar__title">Rooms in this visit</div><div class="room-sidebar__rooms" id="copilotRoomTabs"></div><button class="room-sidebar__add" onclick="backToRoomStep()">＋ Add another room</button></aside>
                        <main class="chat-main">
                            <div class="chat-main__header"><div><h2 id="copilotRoomTitle">Living room</h2><small>Copilot is here to help you figure this out.</small></div><div class="copilot-flow__actions"><button class="copilot-secondary" style="padding:9px 12px" onclick="renameActiveRoom()">Rename room</button><button class="copilot-secondary" style="padding:9px 12px" onclick="openHandover()">I disagree</button></div></div>
                            <div class="chat-canvas" id="chatCanvas"><div class="chat-message chat-message--assistant" id="chatIntro">I understand that something in this room needs attention. We’ll go step by step — you can describe the issue in your own words, skip photos, and remove any service that doesn’t feel right.</div><div class="chat-checklist"><div class="chat-checklist__title"><span>Services to check for this room</span><span class="copilot-hint">You control this list</span></div><div class="chat-checklist__rows" id="copilotChecklist"></div></div><div class="copilot-questions" id="copilotQuestions"><div class="chat-message chat-message--assistant"><h3 style="margin:0 0 5px;color:#4b2415">Can you tell me a little more?</h3><div id="copilotQuestionList"></div></div></div></div>
                            <div class="chat-composer"><textarea id="copilotIssueText" placeholder="What needs repair? For example: bathroom tap is leaking"></textarea><button class="chat-composer__send" onclick="submitCopilotDescription()" aria-label="Send description">➤</button></div>
                            <div class="chat-actions"><button class="chat-action chat-action--primary" onclick="document.getElementById('copilotPhotoInput').click()">▣ Take live photo</button><button class="chat-action" onclick="document.getElementById('copilotPhotoInput').click()">▧ Upload from gallery</button><button class="chat-action" onclick="skipCopilotPhotos()">I don’t want to upload photos</button><input id="copilotPhotoInput" type="file" accept="image/*" multiple hidden onchange="handleCopilotPhotos(event)"></div><div id="photoStatus" class="copilot-hint" style="margin-top:10px"></div>
                        </main>
                    </div>
                    <div class="chat-deals" id="suggestionsSection" style="display:none"><h3>Suggested individual services</h3><div class="service-grid" id="copilotServiceGrid"></div><div id="groupServicesSection" style="display:none"><h3 style="margin-top:24px">Grouped plans</h3><div class="plan-grid" id="copilotPlanGrid"></div><div class="package-row" id="copilotPackageRow"></div></div></div>
                    <div class="handover" id="handoverPanel"><div><strong>We’ll bring in a human helper</strong><span>Tell us what feels off and a specialist can call you.</span></div><a class="copilot-primary" href="tel:+918000123456">Call +91 8000 123 456</a></div>
                </section>
            </div>
        </div>
        <div class="owner-shell">
            <header class="owner-topbar">
                <div class="owner-brand"><span class="owner-brand-mark">⌂</span><span>NoBroker<small>Ghar Seva · Owner Desk</small></span></div>
                <div class="owner-nav"><button type="button">◷ History</button><button type="button">▣ Estimate</button><button type="button">▣ My Bookings (0)</button><button type="button" onclick="closeOwnerScreen()">⇥ Log out</button></div>
            </header>
            <main class="owner-main">
                <span class="owner-kicker">✦ Owner damage inspection</span>
                <h1>Hey Boss, What is going with your House,<br>Let me Help You</h1>
                <p class="owner-intro">Pick a room, describe what needs attention and add photos. We will prepare a fair service estimate from the selected items.</p>
                <div class="owner-layout">
                    <section class="owner-board">
                        <div class="owner-step-title"><span class="owner-step-number">1</span><div><h2>Which room needs attention?</h2><p>Tap a room to filter services. You can select more than one.</p></div></div>
                        <div class="owner-services" id="ownerServices">
                            <button class="owner-service" onclick="selectOwnerService(this,'Furnished Apartment')"><span class="owner-service-icon">🏢</span>Furnished<br>Apartment</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Unfurnished Apartment')"><span class="owner-service-icon">🏢</span>Unfurnished<br>Apartment</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Furnished Villa')"><span class="owner-service-icon">🏡</span>Furnished Villa</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Unfurnished Villa')"><span class="owner-service-icon">🏡</span>Unfurnished Villa</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Empty Kitchen Cleaning')"><span class="owner-service-icon">🍽️</span>Empty Kitchen<br>Cleaning</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Occupied Kitchen Cleaning')"><span class="owner-service-icon">🧰</span>Occupied Kitchen<br>Cleaning</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Sofa Cleaning')"><span class="owner-service-icon">🛋️</span>Sofa cleaning</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Electrician')"><span class="owner-service-icon">🛠️</span>Electrician</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Bathroom Cleaning')"><span class="owner-service-icon">🪣</span>Bathroom<br>Cleaning</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Painting')"><span class="owner-service-icon">🎨</span>Painting</button>
                            <button class="owner-service" onclick="selectOwnerService(this,'Plumbing')"><span class="owner-service-icon">🔧</span>Plumbing</button>
                        </div>
                        <div class="owner-prompt"><input id="ownerPrompt" placeholder="What needs repair? For example: bathroom tap is leaking"><button type="button" onclick="addOwnerPrompt()">➤</button></div>
                        <div class="owner-step-title" style="margin-top:16px"><span class="owner-step-number">2</span><div><h2>What kind of damage or work is it?</h2></div></div>
                        <div class="owner-damage" id="ownerDamage"><button onclick="toggleDamage(this,'Wall stain')">⚠ Wall stain</button><button onclick="toggleDamage(this,'Paint peeling')">⚠ Paint peeling</button><button onclick="toggleDamage(this,'Cracked tile')">⚠ Cracked tile</button><button onclick="toggleDamage(this,'Seepage / damp')">⚠ Seepage / damp</button><button onclick="toggleDamage(this,'Broken door')">⚠ Broken door</button><button onclick="toggleDamage(this,'Missing fixture')">⚠ Missing fixture</button><button onclick="toggleDamage(this,'Burn mark')">⚠ Burn mark</button><button onclick="toggleDamage(this,'Other')">⚠ Other</button></div>
                        <div class="owner-step-title"><span class="owner-step-number">3</span><div><h2>Select the photos to be sent</h2><p><span id="ownerPhotoCount">0</span> of 7 selected · only genuine damage, not normal wear &amp; tear</p></div></div>
                        <div class="owner-photo-grid" id="ownerPhotoGrid">
                            <label class="owner-add"><input id="ownerFileInput" type="file" accept="image/*" multiple onchange="handleOwnerFiles(event)"><span>▣</span>Add live photo<small>Open camera or pick from gallery</small></label>
                            <div class="owner-photo is-picked" data-room="Hall" onclick="togglePhoto(this)"><img alt="Hall photo" src="/assets/ac/figma/086a1d7a-d903-4011-ae50-f282cce5e290.png"><strong>Hall</strong><small>⚠ Wall stain · Live · 22 Nov, 2:20 pm</small></div>
                            <div class="owner-photo is-picked" data-room="Hall" onclick="togglePhoto(this)"><img alt="Hall photo" src="/assets/ac/figma/44b4c244-3ae7-49a8-b312-15274bcb9e9a.png"><strong>Hall</strong><small>⚠ Paint peeling · Live · 22 Nov, 2:20 pm</small></div>
                            <div class="owner-photo is-picked" data-room="Kitchen" onclick="togglePhoto(this)"><img alt="Kitchen photo" src="/assets/ac/figma/49135b03-5d71-4a9e-85e8-0792adc4eedd.png"><strong>Kitchen</strong><small>⚠ Cracked tile · Live · 22 Nov, 2:20 pm</small></div>
                            <div class="owner-photo" data-room="Bathroom" onclick="togglePhoto(this)"><img alt="Bathroom photo" src="/assets/ac/figma/4c7583ff-d4fb-4ad9-9a61-60a826251070.png"><strong>Bathroom</strong><small>⚠ Seepage / damp</small></div>
                            <div class="owner-photo" data-room="Bedroom" onclick="togglePhoto(this)"><img alt="Bedroom photo" src="/assets/ac/figma/5ac6523e-e3ef-4131-85bb-a3967e63f49b.png"><strong>Bedroom</strong><small>⚠ Broken door</small></div>
                            <div class="owner-photo" data-room="Balcony" onclick="togglePhoto(this)"><img alt="Balcony photo" src="/assets/ac/figma/8066acaa-3214-4313-81db-446a03a17011.png"><strong>Balcony</strong><small>⚠ Cracked tile</small></div>
                            <div class="owner-photo" data-room="Pooja room" onclick="togglePhoto(this)"><img alt="Pooja room photo" src="/assets/ac/figma/9e87c7e6-71ac-4110-9c8a-47a538c59a86.png"><strong>Pooja room</strong><small>⚠ Burn mark</small></div>
                        </div>
                        <div class="owner-photo-actions"><button type="button" onclick="document.getElementById('ownerFileInput').click()">▣ Take live photo</button><button type="button" onclick="document.getElementById('ownerFileInput').click()">▧ Upload from gallery</button></div>
                        <div id="ownerResult" class="owner-result" aria-live="polite"></div>
                    </section>
                    <aside class="owner-summary"><h2>Your selection</h2><div class="owner-summary-count"><span id="ownerPhotoCountSummary">3</span> <small>of 7 photos</small></div><div style="height:5px;border-radius:9px;background:#f8e8ca;margin:10px 0 14px"><div id="ownerProgress" style="height:100%;width:43%;border-radius:9px;background:#bd420e"></div></div><div class="owner-selection" id="ownerSelection"><div>🛋 Hall<small>Wall stain</small></div><div>▣ Hall<small>Paint peeling</small></div><div>⌂ Kitchen<small>Cracked tile</small></div></div><ul><li>Live photos only — each one is time-stamped and tagged to the room.</li><li>Fair estimate: normal wear &amp; tear is never deducted.</li><li>Result in under 2 minutes.</li></ul><button class="owner-estimate-button" type="button" onclick="requestOwnerEstimate()">↗ &nbsp; Check damage estimate</button></aside>
                </div>
            </main>
        </div>
    </section>
    <div id="roleToast" class="role-toast" role="status" aria-live="polite"></div>

    <!-- Floating help badge -->
    <button class="help-badge" type="button" onclick="openRoleModal()" aria-label="Need help with home services? Choose your role">
        <svg class="help-badge__ring" viewBox="0 0 160 160" aria-hidden="true">
            <defs>
                <path id="help-badge-circle" d="M 80,80 m -61,0 a 61,61 0 1,1 122,0 a 61,61 0 1,1 -122,0" />
            </defs>
            <text>
                <textPath href="#help-badge-circle" startOffset="0%">NEED HELP WITH HOME SERVICES · WE ARE HERE FOR YOU · </textPath>
            </text>
        </svg>
        <svg class="help-badge__icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M10 29 32 10l22 19" />
            <path d="M16 27v25h32V27" />
            <path d="M27 52h10" />
            <path d="M32 26c-5 0-9 4-9 9 0 3 1 6 4 8v7h10v-7c3-2 4-5 4-8 0-5-4-9-9-9z" />
            <path d="M27 43h10" />
        </svg>
    </button>

    <script>
        let selectedService = "";
        let selectedRole = localStorage.getItem('homeServicesRole') || '';

        function openRoleModal() {
            document.getElementById('roleModal').classList.add('is-open');
        }

        function chooseRole(role) {
            selectedRole = role;
            localStorage.setItem('homeServicesRole', role);
            closeModals();
            if (role === 'Owner') {
                openOwnerScreen();
                return;
            }
            const toast = document.getElementById('roleToast');
            toast.textContent = role + ' mode selected. Choose a service to continue.';
            toast.classList.add('is-visible');
            window.setTimeout(() => toast.classList.remove('is-visible'), 3200);
            document.getElementById('servicesGrid').scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        function openOwnerScreen() {
            document.getElementById('ownerScreen').classList.add('is-open');
            document.body.style.overflow = 'hidden';
            resetCopilotFlow();
        }

        function closeOwnerScreen() {
            document.getElementById('ownerScreen').classList.remove('is-open');
            document.body.style.overflow = '';
        }

        const ownerState = { rooms: [], damage: [], photos: 3 };

        const copilotState = { rooms: [], activeRoom: '', photos: [], recommendations: {}, labels: {}, excluded: {}, described: {} };
        const roomImages = {
            'Living room': '/assets/ac/figma/086a1d7a-d903-4011-ae50-f282cce5e290.png',
            'Kitchen': '/assets/ac/figma/49135b03-5d71-4a9e-85e8-0792adc4eedd.png',
            'Bathroom': '/assets/ac/figma/4c7583ff-d4fb-4ad9-9a61-60a826251070.png',
            'Bedroom': '/assets/ac/figma/5ac6523e-e3ef-4131-85bb-a3967e63f49b.png',
            'Balcony': '/assets/ac/figma/8066acaa-3214-4313-81db-446a03a17011.png',
            'Pooja room': '/assets/ac/figma/9e87c7e6-71ac-4110-9c8a-47a538c59a86.png'
        };

        function resetCopilotFlow() {
            copilotState.rooms = []; copilotState.activeRoom = ''; copilotState.photos = []; copilotState.recommendations = {}; copilotState.labels = {}; copilotState.excluded = {}; copilotState.described = {};
            document.querySelectorAll('.room-card.is-selected').forEach(card => card.classList.remove('is-selected'));
            document.getElementById('continueRooms').disabled = true;
            document.getElementById('roomStep').style.display = 'block';
            document.getElementById('resultsStep').classList.remove('is-visible');
            document.getElementById('handoverPanel').classList.remove('is-visible');
        }

        function toggleCopilotRoom(card) {
            card.classList.toggle('is-selected');
            copilotState.rooms = [...document.querySelectorAll('.room-card.is-selected')].map(item => item.dataset.room);
            document.getElementById('continueRooms').disabled = copilotState.rooms.length === 0;
        }

        async function continueCopilotRooms() {
            copilotState.activeRoom = copilotState.rooms[0];
            document.getElementById('roomStep').style.display = 'none';
            document.getElementById('resultsStep').classList.add('is-visible');
            document.getElementById('copilotServiceGrid').innerHTML = '<div class="copilot-panel">Finding relevant services for your rooms…</div>';
            const response = await fetch('/api/copilot/recommend', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({ rooms: copilotState.rooms, note: document.getElementById('copilotNote').value, photos: false }) });
            const data = await response.json();
            copilotState.recommendations = data.rooms || {};
            renderCopilotRoomTabs();
            renderCopilotRoom(copilotState.activeRoom);
        }

        function renderCopilotRoomTabs() {
            document.getElementById('copilotRoomTabs').innerHTML = copilotState.rooms.map(room => `<button class="room-sidebar__room ${room === copilotState.activeRoom ? 'is-active' : ''}" onclick="renderCopilotRoom('${room.replace(/'/g, "\\'")}')"><span>${copilotState.labels[room] || room}</span><small>${(copilotState.recommendations[room]?.matches || []).length}</small></button>`).join('');
        }

        function renderCopilotRoom(room) {
            copilotState.activeRoom = room;
            renderCopilotRoomTabs();
            const data = copilotState.recommendations[room] || {};
            const roomHasDescription = Boolean(copilotState.described[room]);
            document.getElementById('copilotRoomTitle').textContent = `${copilotState.labels[room] || room} checklist`;
            const excluded = copilotState.excluded[room] || [];
            const visibleMatches = (data.matches || []).filter(match => !excluded.includes(match.name));
            document.getElementById('copilotChecklist').innerHTML = roomHasDescription ? (visibleMatches.map((match, index) => `<label class="chat-checklist__row"><input type="checkbox" checked onchange="toggleChecklistService('${match.name.replace(/'/g, "\\'")}')"><span><b>${match.name}</b><br><small>${(data.checklist || [])[index % Math.max(1, (data.checklist || []).length)] || 'Inspect this service area based on the issue you described.'}</small></span><button type="button" onclick="toggleChecklistService('${match.name.replace(/'/g, "\\'")}')" aria-label="Remove ${match.name}">Delete</button></label>`).join('') || '<div class="chat-checklist__empty">No services selected. Describe another part of the issue to get a new suggestion.</div>') : '<div class="chat-checklist__empty">I’ll show the service checklist after I understand what is wrong.</div>';
            document.getElementById('copilotQuestionList').innerHTML = `<p>${(data.questions || ["What would you like me to understand about this room?"])[0]}</p>`;
            document.getElementById('copilotQuestions').classList.toggle('is-visible', !roomHasDescription);
            document.getElementById('chatIntro').textContent = roomHasDescription
                ? `Thanks — I understood the issue you described in the ${copilotState.labels[room] || room}. I checked the NoBroker services available for this room and selected the most relevant ones below.`
                : 'I understand that something in this room needs attention. Tell me what you noticed and I’ll check the NoBroker services available for this room.';
            document.getElementById('suggestionsSection').style.display = roomHasDescription && visibleMatches.length ? 'block' : 'none';
            document.getElementById('copilotServiceGrid').innerHTML = visibleMatches.map(match => `<article class="service-card"><img src="${serviceImageUrl(match, room)}" alt="${match.name}"><div class="service-card__body"><h3>${match.name}</h3><div class="service-card__meta"><span>₹${Number(match.price).toLocaleString('en-IN')}</span><span>★ ${match.rating || '4.7'}</span></div><div class="service-card__why"><b>Why this is suggested:</b> ${data.why || 'This service matches the room and the issue you described.'}</div><div class="service-card__footer"><a href="${match.detail_url || serviceDetailUrl(match.name)}">View details →</a><button onclick="openBookingModal('${match.name.replace(/'/g, "\\'")}')">Add service</button></div></div></article>`).join('');
            const showGrouped = roomHasDescription && visibleMatches.length > 1;
            document.getElementById('groupServicesSection').style.display = showGrouped ? 'block' : 'none';
            document.getElementById('copilotPlanGrid').innerHTML = showGrouped ? (data.plans || []).map(plan => `<article class="plan-card ${plan.recommended ? 'is-recommended' : ''}"><h4>${plan.name} ${plan.recommended ? '· Recommended' : ''}</h4><strong>₹${Number(plan.price).toLocaleString('en-IN')}</strong><p>${plan.summary}</p><ul><li><b>What it covers:</b> ${plan.covers}</li><li><b>What it doesn’t:</b> ${plan.excludes}</li></ul></article>`).join('') : '';
            document.getElementById('copilotPackageRow').innerHTML = showGrouped ? `<div><strong>${data.package?.name || 'Home care package'}</strong><br><span>${data.package?.description || 'Bundle related services for this room.'}</span></div><strong>₹${Number(data.package?.price || 0).toLocaleString('en-IN')}</strong>` : '';
        }

        function serviceImageUrl(match, room) { const image = match.image || ''; return image.startsWith('/') ? image : (image ? `/assets/${image}` : (roomImages[room] || roomImages['Living room'])); }
        function serviceDetailUrl(name) {
            const value = name.toLowerCase();
            if (value.includes('bathroom')) return '/bathroom-cleaning';
            if (value.includes('kitchen')) return '/kitchen-cleaning';
            if (value.includes('sofa')) return '/sofa-cleaning';
            if (value.includes('electric')) return '/electrician';
            if (value.includes('plumb')) return '/plumber';
            if (value.includes('paint')) return '/painting-services';
            if (value.includes('ac')) return '/ac-services';
            return '/';
        }

        function backToRoomStep() { document.getElementById('resultsStep').classList.remove('is-visible'); document.getElementById('roomStep').style.display = 'block'; }
        async function submitCopilotDescription() { const input = document.getElementById('copilotIssueText'); const description = input.value.trim(); if (!description) return; const bubble = document.createElement('div'); bubble.className = 'chat-message chat-message--user'; bubble.textContent = description; document.getElementById('chatCanvas').appendChild(bubble); copilotState.described[copilotState.activeRoom] = true; const response = await fetch('/api/copilot/recommend', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({ rooms:[copilotState.activeRoom], note:description, photos:copilotState.photos.length > 0 }) }); const data = await response.json(); copilotState.recommendations[copilotState.activeRoom] = data.rooms[copilotState.activeRoom]; renderCopilotRoom(copilotState.activeRoom); document.getElementById('photoStatus').textContent = 'I updated the service checklist from your description.'; input.value = ''; }
        function toggleChecklistService(name) { const excluded = copilotState.excluded[copilotState.activeRoom] || []; copilotState.excluded[copilotState.activeRoom] = excluded.includes(name) ? excluded.filter(item => item !== name) : [...excluded, name]; renderCopilotRoom(copilotState.activeRoom); }
        function renameActiveRoom() { const label = window.prompt('What would you like to call this room?', copilotState.labels[copilotState.activeRoom] || copilotState.activeRoom); if (label && label.trim()) { copilotState.labels[copilotState.activeRoom] = label.trim(); renderCopilotRoom(copilotState.activeRoom); } }
        function skipCopilotPhotos() { copilotState.photos = []; document.getElementById('photoStatus').textContent = 'That’s okay — we’ll use a few focused questions instead.'; document.getElementById('copilotQuestions').classList.add('is-visible'); }
        function handleCopilotPhotos(event) { copilotState.photos = [...event.target.files]; document.getElementById('photoStatus').textContent = `${copilotState.photos.length} photo${copilotState.photos.length === 1 ? '' : 's'} added. Recommendations can be refined after inspection.`; document.getElementById('copilotQuestions').classList.remove('is-visible'); }
        function openHandover() { document.getElementById('handoverPanel').classList.add('is-visible'); document.getElementById('handoverPanel').scrollIntoView({behavior:'smooth', block:'nearest'}); }

        function selectOwnerService(button, room) {
            button.classList.toggle('is-selected');
            ownerState.rooms = [...document.querySelectorAll('.owner-service.is-selected')].map(item => item.innerText.replace(/\\s+/g, ' ').trim());
        }

        function toggleDamage(button, damage) {
            button.classList.toggle('is-selected');
            ownerState.damage = [...document.querySelectorAll('#ownerDamage button.is-selected')].map(item => item.innerText.replace('⚠ ', ''));
            updateOwnerSelection();
        }

        function addOwnerPrompt() {
            const input = document.getElementById('ownerPrompt');
            if (input.value.trim()) { ownerState.damage.push(input.value.trim()); input.value = ''; updateOwnerSelection(); }
        }

        function togglePhoto(card) {
            card.classList.toggle('is-picked');
            ownerState.photos = document.querySelectorAll('.owner-photo.is-picked').length;
            updateOwnerSelection();
        }

        function handleOwnerFiles(event) {
            const files = [...event.target.files].slice(0, 7);
            const grid = document.getElementById('ownerPhotoGrid');
            files.forEach(file => {
                const card = document.createElement('div');
                card.className = 'owner-photo is-picked';
                card.innerHTML = `<img alt="Uploaded inspection photo" src="${URL.createObjectURL(file)}"><strong>New photo</strong><small>Live · just now</small>`;
                card.onclick = () => togglePhoto(card);
                grid.appendChild(card);
            });
            ownerState.photos = Math.min(7, document.querySelectorAll('.owner-photo.is-picked').length);
            updateOwnerSelection();
        }

        function updateOwnerSelection() {
            const count = Math.min(7, ownerState.photos);
            document.getElementById('ownerPhotoCount').textContent = count;
            document.getElementById('ownerPhotoCountSummary').textContent = count;
            document.getElementById('ownerProgress').style.width = `${Math.round(count / 7 * 100)}%`;
            const selected = [...document.querySelectorAll('.owner-photo.is-picked')].slice(0, 3);
            document.getElementById('ownerSelection').innerHTML = selected.map(card => `<div>▣ ${card.dataset.room || 'New photo'}<small>${ownerState.damage[0] || 'Inspection photo'}</small></div>`).join('') || '<div>No photos selected yet</div>';
        }

        async function requestOwnerEstimate() {
            addOwnerPrompt();
            const prompt = [ownerState.rooms.join(' '), ownerState.damage.join(' ')].filter(Boolean).join(' ') || 'home damage inspection';
            const result = document.getElementById('ownerResult');
            result.innerHTML = '<b>Checking your damage estimate…</b>';
            result.classList.add('is-visible');
            const response = await fetch('/api/copilot/estimate', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({ prompt, quantity:1 }) });
            const data = await response.json();
            const money = value => '₹' + Number(value).toLocaleString('en-IN');
            result.innerHTML = `<b>Recommended damage estimate</b><div class="owner-price">${money(data.estimate.low)} – ${money(data.estimate.high)}</div><div>${data.matches.slice(0, 2).map(match => `${match.name} · ${money(match.price)}`).join('<br>')}</div><p class="owner-note">${data.note}</p>`;
        }

        // 1. Live Search Filter
        function filterServices() {
            let input = document.getElementById('searchInput').value.toLowerCase();
            let items = document.getElementsByClassName('service-item');
            for (let item of items) {
                let text = item.innerText.toLowerCase();
                item.style.display = text.includes(input) ? "block" : "none";
            }
        }

        // 2. Open Booking Popup
        function openBookingModal(serviceName) {
            selectedService = serviceName;
            document.getElementById('modalServiceTitle').innerText = "Book: " + serviceName;
            document.getElementById('bookingModal').style.display = 'flex';
        }

        // Home Cleaning popup: loads the 4 services from Python
        async function openCleaningPopup() {
            const list = document.getElementById('cleaningList');
            const res = await fetch('/api/cleaning-services');
            const services = await res.json();
            list.innerHTML = services.map(s =>
                `<div class="cursor-pointer rounded-xl border border-gray-200 p-4 text-center hover:border-teal-600 hover:bg-teal-50 transition"
                      onclick="pickCleaningService('${s.name}')">
                    <div class="text-3xl mb-2">${s.icon}</div>
                    <div class="font-semibold text-gray-900 text-sm">${s.name}</div>
                    <div class="text-xs text-gray-500 mt-1">${s.desc}</div>
                </div>`
            ).join('');
            document.getElementById('cleaningModal').style.display = 'flex';
        }

        // Painting popup: loads the two painting options from Python
        async function openPaintingPopup() {
            const list = document.getElementById('paintingList');
            const res = await fetch('/api/painting-services');
            const services = await res.json();
            list.innerHTML = services.map(s =>
                `<div class="cursor-pointer rounded-xl border border-gray-200 p-4 text-center hover:border-teal-600 hover:bg-teal-50 transition"
                      onclick="pickPaintingService('${s.name}')">
                    <div class="text-3xl mb-2">${s.icon}</div>
                    <div class="font-semibold text-gray-900 text-sm">${s.name}</div>
                    <div class="text-xs text-gray-500 mt-1">${s.desc}</div>
                </div>`
            ).join('');
            document.getElementById('paintingModal').style.display = 'flex';
        }

        // Open the available electrician, plumber and carpenter choices.
        async function openTradesPopup() {
            const list = document.getElementById('tradesList');
            const response = await fetch('/api/trade-services');
            const services = await response.json();
            list.innerHTML = services.map(service =>
                `<button type="button" class="cursor-pointer rounded-xl border border-gray-200 p-4 text-center hover:border-teal-600 hover:bg-teal-50 transition"
                         onclick="pickTradeService('${service.name}')">
                    <span class="text-3xl mb-2 block" aria-hidden="true">${service.icon}</span>
                    <span class="font-semibold text-gray-900 text-sm block">${service.name}</span>
                    <span class="text-xs text-gray-500 mt-1 block">${service.desc}</span>
                </button>`
            ).join('');
            document.getElementById('tradesModal').style.display = 'flex';
        }

        // Show the two service groups for AC and home appliance repair.
        async function openAppliancePopup() {
            const list = document.getElementById('applianceList');
            const response = await fetch('/api/appliance-services');
            const services = await response.json();
            list.innerHTML = services.map(service =>
                `<button type="button" class="cursor-pointer rounded-xl border border-gray-200 p-4 text-center hover:border-teal-600 hover:bg-teal-50 transition"
                         onclick="pickApplianceService('${service.name}')">
                    <span class="text-3xl mb-2 block" aria-hidden="true">${service.icon}</span>
                    <span class="font-semibold text-gray-900 text-sm block">${service.name}</span>
                    <span class="text-xs text-gray-500 mt-1 block">${service.desc}</span>
                </button>`
            ).join('');
            document.getElementById('applianceModal').style.display = 'flex';
        }

        function pickApplianceService(name) {
            closeModals();
            if (name === 'AC Services') {
                window.location.href = '/ac';
                return;
            }
            if (name === 'Appliance Services') {
                window.location.href = '/appliances';
                return;
            }
            openBookingModal(name);
        }

        function pickTradeService(name) {
            closeModals();
            if (name === 'Electrician') {
                window.location.href = '/electrician';
                return;
            }
            if (name === 'Carpenter') {
                window.location.href = '/carpenter';
                return;
            }
            if (name === 'Plumber') {
                window.location.href = '/plumber';
                return;
            }
            openBookingModal(name);
        }

        function pickPaintingService(name) {
            closeModals();
            if (name === 'Premium Painting') {
                window.location.href = '/premium-painting';
                return;
            }
            if (name === 'Painting Services') {
                window.location.href = '/painting-services';
                return;
            }
            openBookingModal(name);
        }

        function pickCleaningService(name) {
            closeModals();
            if (name.startsWith('Full House')) {
                window.location.href = '/full-house-cleaning';
                return;
            }
            if (name.startsWith('Bathroom')) {
                window.location.href = '/bathroom-cleaning';
                return;
            }
            if (name.startsWith('Sofa')) {
                window.location.href = '/sofa-cleaning';
                return;
            }
            if (name.startsWith('Kitchen')) {
                window.location.href = '/kitchen-cleaning';
                return;
            }
            openBookingModal(name);
        }

        function openAuthModal(type) {
            alert(type + " feature triggered! Enter details during booking.");
        }

        function closeModals() {
            document.getElementById('cleaningModal').style.display = 'none';
            document.getElementById('paintingModal').style.display = 'none';
            document.getElementById('tradesModal').style.display = 'none';
            document.getElementById('applianceModal').style.display = 'none';
            document.getElementById('bookingModal').style.display = 'none';
            document.getElementById('myBookingsModal').style.display = 'none';
            document.getElementById('roleModal').classList.remove('is-open');
        }

        updateOwnerSelection();

        // 3. Send Booking Data to Python Backend
        async function submitBooking() {
            const name = document.getElementById('custName').value;
            const phone = document.getElementById('custPhone').value;
            const date = document.getElementById('custDate').value;
            const city = document.getElementById('citySelect').value;

            if (!name || !phone || !date) {
                alert("Please fill in all details!");
                return;
            }

            const response = await fetch('/book', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ service: selectedService, name, phone, date, city, role: selectedRole })
            });

            const data = await response.json();
            document.getElementById('bookingCount').innerText = data.total;
            alert("Success! Your booking for " + selectedService + " is confirmed.");
            closeModals();
        }

        // 4. Fetch & Display Saved Bookings from Python
        async function openBookingsModal() {
            const response = await fetch('/bookings');
            const bookings = await response.json();
            const container = document.getElementById('bookingsContainer');
            
            if (bookings.length === 0) {
                container.innerHTML = "<p>No bookings yet. Click any service to book!</p>";
            } else {
                container.innerHTML = bookings.map(b => 
                    `<div class="booking-card">
                        <strong>${b.service}</strong> (${b.city})<br>
                        Name: ${b.name} | Date: ${b.date}
                    </div>`
                ).join('');
            }
            document.getElementById('myBookingsModal').style.display = 'flex';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    services = [
        {"name": "Home Cleaning", "tag": "Upto 60% Off*", "icon": "🧹"},
        {"name": "Packers & Movers", "tag": "Lowest Quote*", "icon": "🚚"},
        {"name": "Painting", "tag": "Flat 15% Off", "icon": "🖌️"},
        {"name": "Sales Agreement", "tag": "", "icon": "📄"},
        {"name": "Rental Agreement", "tag": "Flat 30% Off*", "icon": "📝"},
        {"name": "Electrician, Plumber & Carpenter", "tag": "", "icon": "🔧"},
        {"name": "Interior and Renovation", "tag": "", "icon": "🛋️"},
        {"name": "AC & Appliance Repair", "tag": "Upto 30% Off*", "icon": "❄️"}
    ]
    
    offers = [
        {
            "badge": "VIP MEMBERSHIP",
            "title": "Save upto 15% off on Home Services",
            "btn": "Buy Now",
            "theme": "dark"
        },
        {
            "badge": "Free Tenant Verification",
            "title": "Upto 30% off on Rental agreement",
            "btn": "Create Agreement",
            "theme": "light-green"
        },
        {
            "badge": "Festive Sale",
            "title": "Flat 15% off on Home Painting",
            "btn": "Explore Now",
            "theme": "light-blue"
        }
    ]
    
    service_links = {
        'Home Cleaning': '/full-house-cleaning',
        'Painting': '/painting-services',
        'Electrician, Plumber & Carpenter': '/electrician',
        'Interior and Renovation': '/premium-painting',
        'AC & Appliance Repair': '/ac-services',
    }
    for service in services:
        service['href'] = service_links.get(service['name'], '/')
    return render_template('index.html', services=services, offers=offers)


# ─────────────────────────────────────────────────────────────────────
# Catalogue pages and APIs
def _json_page(data):
    return jsonify(data)


def _render_catalog(template_name, data):
    return render_template(template_name, **data)


@app.route('/full-house-cleaning')
def full_house_cleaning():
    return _render_catalog('full_house_cleaning.html', page_data())


@app.route('/kitchen-cleaning')
def kitchen_cleaning():
    return _render_catalog('kitchen_cleaning.html', kitchen_page_data())


@app.route('/sofa-cleaning')
def sofa_cleaning():
    return _render_catalog('sofa_cleaning.html', sofa_page_data())


@app.route('/bathroom-cleaning')
def bathroom_cleaning():
    return _render_catalog('bathroom_cleaning.html', bathroom_page_data())


@app.route('/electrician')
def electrician():
    return _render_catalog('electrician.html', electrician_page_data())


@app.route('/carpenter')
def carpenter():
    return _render_catalog('carpenter.html', carpenter_page_data())


@app.route('/plumber')
def plumber():
    return _render_catalog('plumber.html', plumber_page_data())


@app.route('/ac-services')
def ac_services():
    return _render_catalog('ac.html', ac_page_data())


@app.route('/appliances')
def appliances():
    return _render_catalog('appliances.html', appliances_page_data())


@app.route('/painting-services')
def painting_services_page():
    return _render_catalog('painting_services.html', painting_services_page_data())


@app.route('/premium-painting')
def premium_painting():
    return _render_catalog('premium_painting.html', premium_painting_page_data())


@app.route('/api/full-house-cleaning')
def api_full_house_cleaning():
    return _json_page(page_data())


@app.route('/api/kitchen-cleaning')
def api_kitchen_cleaning():
    return _json_page(kitchen_page_data())


@app.route('/api/sofa-cleaning')
def api_sofa_cleaning():
    return _json_page(sofa_page_data())


@app.route('/api/bathroom-cleaning')
def api_bathroom_cleaning():
    return _json_page(bathroom_page_data())


@app.route('/api/cleaning-services')
def api_cleaning_services():
    return _json_page(cleaning_services)


@app.route('/api/painting-services')
def api_painting_services():
    return _json_page(painting_services)


@app.route('/api/trade-services')
def api_trade_services():
    return _json_page(trade_services)


@app.route('/api/appliance-services')
def api_appliance_services():
    return _json_page(appliance_services)


@app.route('/book', methods=['POST'])
def book():
    payload = request.get_json(silent=True) or {}
    record = {key: payload.get(key, '') for key in ('service', 'name', 'phone', 'date', 'city', 'role')}
    record['city'] = record['city'] or 'Pune'
    record['role'] = record['role'] or 'Customer'
    bookings_list.append(record)
    return jsonify({'status': 'success', 'message': 'Booking confirmed', 'total': len(bookings_list), 'booking': record})


@app.route('/bookings')
def bookings():
    return jsonify(bookings_list)


#  Copilot Page
# ─────────────────────────────────────────────────────────────────────
@app.route('/copilot')
def copilot_page():
    return render_template('copilot.html')


# ─────────────────────────────────────────────────────────────────────
#  Room-aware service recommendations
#  POST /api/copilot/room-services
#  Body: { room: str, has_photos: bool, photo_count: int }
# ─────────────────────────────────────────────────────────────────────

# Per-room rules: which catalogue terms are relevant + "why" text + icon
_ROOM_RULES = {
    'Living Room': {
        'terms': ['sofa', 'painting', 'electrician', 'full house', 'cleaning'],
        'icon': '🛋️',
        'whys': {
            'sofa':        'Sofas and upholstery in living rooms collect dust, stains and allergens over time.',
            'painting':    'Wall scuffs, faded patches and peeling paint are most visible in living areas.',
            'electrician': 'Switches, fans and lighting fixtures see the heaviest use in the living room.',
            'full house':  'A full-house clean covers your living room plus all connected spaces in one visit.',
            'cleaning':    'General deep-cleaning removes dust, stains and allergens from all surfaces.',
        },
        'groups': ['Full House Cleaning Services', 'Premium Painting'],
    },
    'Kitchen': {
        'terms': ['kitchen', 'plumb', 'painting', 'cleaning'],
        'icon': '🍽️',
        'whys': {
            'kitchen': 'Kitchen cleaning targets grease on tiles, chimney, cabinets and the cooking slab.',
            'plumb':   'Under-sink leaks and drain blockages are the most common kitchen plumbing issues.',
            'painting': 'Steam and grease discolour kitchen walls faster than any other room.',
            'cleaning': 'Deep cleaning removes built-up grease and sanitises the full cooking area.',
        },
        'groups': ['Kitchen Services'],
    },
    'Bathroom': {
        'terms': ['bathroom', 'plumb', 'painting'],
        'icon': '🚿',
        'whys': {
            'bathroom': 'Bathroom cleaning covers tiles, fittings, toilet, basin and drain deep-cleaning.',
            'plumb':    'Tap drips, flush issues and slow drains are common bathroom plumbing repairs.',
            'painting': 'Moisture causes paint to peel or mould faster in bathrooms than elsewhere.',
        },
        'groups': ['Bathroom Cleaning Services'],
    },
    'Bedroom': {
        'terms': ['painting', 'carpenter', 'ac', 'electrician', 'cleaning'],
        'icon': '🛏️',
        'whys': {
            'painting':    'Bedrooms benefit most from a fresh wall finish — especially near the headboard.',
            'carpenter':   'Wardrobe hinges, door handles and bed frames are common bedroom repair items.',
            'ac':          'Bedroom ACs need periodic servicing to maintain cooling efficiency.',
            'electrician': 'Fan speed issues, light flickering and switch problems are common in bedrooms.',
            'cleaning':    'Dust accumulates in bedroom corners, under beds and inside wardrobes.',
        },
        'groups': ['Premium Painting'],
    },
    'Balcony': {
        'terms': ['painting', 'full house', 'bathroom', 'cleaning'],
        'icon': '🌿',
        'whys': {
            'painting': 'Balcony walls face weather and UV exposure, requiring more frequent repainting.',
            'full house': 'A full-house service can include the balcony in a single coordinated visit.',
            'bathroom': 'Balcony drains can be cleaned alongside bathroom drain work in one visit.',
            'cleaning': 'Balconies collect rain grime, bird debris and outdoor dust that need deep cleaning.',
        },
        'groups': [],
    },
    'Pooja Room': {
        'terms': ['full house', 'painting', 'kitchen', 'cleaning'],
        'icon': '🪔',
        'whys': {
            'full house': 'Pooja rooms are included in full-house deep-cleaning packages.',
            'painting':   'Smoke and incense marks on walls benefit from a touch-up or full repaint.',
            'kitchen':    'Pooja rooms with vessel prep areas share cleaning needs with the kitchen.',
            'cleaning':   'Incense residue, ash and dust from lamps need specialist gentle cleaning.',
        },
        'groups': [],
    },
    'Study / Office': {
        'terms': ['electrician', 'carpenter', 'painting', 'cleaning'],
        'icon': '💻',
        'whys': {
            'electrician': 'Work desks require multiple power points and proper lighting — common upgrade requests.',
            'carpenter':   'Shelves, study tables and cable management are typical carpentry jobs.',
            'painting':    'A fresh neutral wall colour improves focus in a study or home office.',
            'cleaning':    'Dust on bookshelves and electronic equipment builds up faster in enclosed studies.',
        },
        'groups': [],
    },
    'Full House': {
        'terms': ['full house', 'painting', 'sofa', 'bathroom', 'kitchen', 'electrician'],
        'icon': '🏠',
        'whys': {
            'full house': 'A full-house clean covers every room — the most cost-effective option for a whole-home refresh.',
            'painting':   'Full-home repainting bundles all rooms into one visit, cutting cost and downtime.',
            'sofa':       'Sofa cleaning is included or discounted in full-home service packages.',
            'bathroom':   'Bathroom deep-cleaning is part of a full-house service run.',
            'kitchen':    'Kitchen degreasing is covered in full-house cleaning packages.',
            'electrician':'A full-home electrical check spots issues across all rooms in a single inspection.',
        },
        'groups': ['Full House Cleaning Services', 'Premium Painting'],
    },
}


def _build_room_services(room: str, has_photos: bool, photo_count: int):
    """
    Return a list of service dicts for the given room.
    Each dict: id, name, price, rating, duration, category, image, icon,
               why, is_group, detail_url, covers, doesnt
    """
    rule = _ROOM_RULES.get(room, _ROOM_RULES['Living Room'])
    terms = rule['terms']
    whys  = rule.get('whys', {})
    group_names = set(rule.get('groups', []))

    def score(record):
        text = ' '.join([record['name'], record['category'], *record.get('details', [])]).lower()
        return sum(1 for term in terms if term in text)

    matches = sorted(COPILOT_CATALOG, key=score, reverse=True)
    matches = [r for r in matches if score(r) > 0][:8] or COPILOT_CATALOG[:5]

    # Deduplicate by name
    seen = set()
    result = []
    for item in matches:
        key = item['name'].lower()
        if key in seen:
            continue
        seen.add(key)
        # find best why (from room rules first)
        why = ''
        for term, reason in whys.items():
            if term in item['name'].lower() or term in item['category'].lower():
                why = reason
                break
        # photo boost: if photos shared, enrich the why text
        if has_photos and photo_count > 0 and not why:
            why = f'Identified as likely needed based on your {photo_count} photo(s) of this room.'

        # get covers / doesn't cover for this service
        cov = _get_coverage(item['name'], item.get('category', ''))
        # if coverage has its own why, prefer it over the vague default
        if not why and cov.get('why'):
            why = cov['why']

        result.append({
            'id':         item['name'].lower().replace(' ', '_').replace('/', '_'),
            'name':       item['name'],
            'price':      item.get('price', 0),
            'rating':     item.get('rating') or '4.5',
            'duration':   item.get('duration', ''),
            'category':   item.get('category', ''),
            'image':      item.get('image', ''),
            'icon':       rule['icon'],
            'why':        why,
            'is_group':   item['name'] in group_names or item['category'] in group_names,
            'detail_url': item.get('detail_url', '/'),
            'covers':     cov['covers'],
            'doesnt':     cov['doesnt'],
        })
    return result


@app.route('/api/copilot/room-services', methods=['POST'])
def copilot_room_services():
    payload    = request.get_json(silent=True) or {}
    room       = str(payload.get('room', 'Living Room'))
    has_photos = bool(payload.get('has_photos', False))
    photo_count = int(payload.get('photo_count', 0))
    services   = _build_room_services(room, has_photos, photo_count)
    return jsonify({'room': room, 'services': services, 'count': len(services)})


# ─────────────────────────────────────────────────────────────────────
#  Estimate from selected checklist items
#  POST /api/copilot/estimate-checklist
#  Body: { services: [{id, name, price, room}] }
# ─────────────────────────────────────────────────────────────────────
@app.route('/api/copilot/estimate-checklist', methods=['POST'])
def copilot_estimate_checklist():
    payload  = request.get_json(silent=True) or {}
    services = payload.get('services', [])
    line_items = []
    total = 0
    for svc in services:
        price = int(svc.get('price', 0) or 0)
        name = svc.get('name', '—')
        category = svc.get('category', '')
        cov = _get_coverage(name, category)
        why = svc.get('why') or cov.get('why', '')
        line_items.append({
            'room':    svc.get('room', '—'),
            'name':    name,
            'price':   price,
            'why':     why,
            'covers':  cov.get('covers', []),
            'doesnt':  cov.get('doesnt', []),
            'detail_url': svc.get('detail_url', '/')
        })
        total += price
    # Add a ±10% range
    low  = int(total * 0.90)
    high = int(total * 1.10)
    return jsonify({
        'total_low':  low,
        'total_high': high,
        'line_items': line_items,
        'note': 'Estimate uses current catalogue prices. Final cost confirmed after professional inspection. Parts, materials and applicable taxes may vary.',
        'service_count': len(line_items),
    })


# ─────────────────────────────────────────────────────────────────────
#  Semi-supervised Feedback API
#  POST /api/copilot/feedback
#  Body: { room: str, service_id: str, service_name: str, vote: 'up'|'down', comment: str }
# ─────────────────────────────────────────────────────────────────────
@app.route('/api/copilot/feedback', methods=['POST'])
def copilot_feedback():
    payload = request.get_json(silent=True) or {}
    record = {
        'timestamp': os.environ.get('CURRENT_TIME', ''),
        'room': payload.get('room', ''),
        'service_id': payload.get('service_id', ''),
        'service_name': payload.get('service_name', ''),
        'vote': payload.get('vote', 'up'),
        'comment': payload.get('comment', '')
    }
    _save_feedback(record)
    return jsonify({'status': 'success', 'message': 'Feedback recorded for model learning'})


if __name__ == '__main__':
    app.run(debug=True)
