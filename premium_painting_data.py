"""Content for the Premium Painting page based on the matching Figma section."""

ASSET_BASE = "/assets/painting/premium/"
PHOTO_BASE = ASSET_BASE + "photos/"
ICON_BASE = ASSET_BASE + "icons/"

PROCESS_STEPS = [
    {"title": "Book an Inspection", "tag": "TODAY", "description": "The measurements and notes are yours to keep either way.", "photo": "process-inspection.png"},
    {"title": "Design Consultation and Scoping", "tag": "45 MIN (SET A TIME)", "description": "Surfaces, shades and finishes are discussed to define the scope.", "photo": "process-consultation.png"},
    {"title": "Get an Itemised Quote", "tag": "IN 24 HOURS", "description": "Get a full cost breakdown for paint, primer, putty and labour.", "photo": "process-quote.png"},
    {"title": "Preparation and Precautions", "tag": "DAY 1", "description": "Furniture is wrapped, floors are sheeted and surfaces prepared.", "photo": "process-preparation.png"},
    {"title": "Painting", "tag": "DAY 2 ONWARDS", "description": "Experienced painters apply the selected finish with care.", "photo": "process-painting.png"},
    {"title": "Final Handover", "tag": "QUALITY CHECK", "description": "Review the completed work with your project supervisor.", "photo": "process-handover.png"},
]

PAINT_GRADES = [
    {"name": "Premium Emulsion", "brand": "Asian Paints", "description": "A smooth, durable finish for everyday living spaces.", "photo": "grade-basic.png"},
    {"name": "Royale Luxury Emulsion", "brand": "Asian Paints", "description": "A rich finish with a refined look and easy maintenance.", "photo": "grade-premium.png"},
    {"name": "Royale Glitz Shyne Matt", "brand": "Asian Paints", "description": "A soft sheen that brings depth to your walls.", "photo": "grade-luxury.png"},
    {"name": "Royale Aspira", "brand": "Asian Paints", "description": "A premium paint grade for a polished home makeover.", "photo": "grade-exterior.png"},
]

PROJECTS = [
    {"before": "project-1.jpg", "after": "project-3.jpg", "title": "Dining room transformation", "location": "Pune", "note": "A rich, warm shade brings character to the dining space."},
    {"before": "project-4.jpg", "after": "project-5.jpg", "title": "Bedroom transformation", "location": "Pune", "note": "A soft rose finish gives this bedroom a fresh feel."},
    {"before": "project-6.jpg", "after": "project-2.jpg", "title": "Living room transformation", "location": "Pune", "note": "A deep green wall creates a calm focal point."},
]

FAQS = [
    {"question": "What does the ₹49 inspection get me?", "answer": "A painting expert visits to assess the surfaces, take measurements and note the preparation required. You can keep the measurements and itemised quote whether or not you proceed."},
    {"question": "Is the ₹49 refunded if I book?", "answer": "The visit charge is adjusted against your painting booking when you proceed with the quoted work."},
    {"question": "How is the painting quote calculated?", "answer": "The quote is based on measured area, surface condition, selected paint grade and the preparation work required. It lists paint, primer, putty and labour separately."},
    {"question": "Can I choose the paint colour and brand?", "answer": "Yes. Discuss colour, brand and finish with the painting consultant during the site visit before confirming the scope."},
    {"question": "How long does a home painting project take?", "answer": "The schedule depends on the home size and preparation needed. Your consultant will share the estimated timeline with the itemised quote."},
    {"question": "Is the painting work insured?", "answer": "Eligible claims for completed painting bookings can be raised in the app and are reviewed under the applicable service conditions."},
]


def page_data():
    """Return template data using local Figma-exported assets."""
    return {
        "asset_base": ASSET_BASE,
        "photo_base": PHOTO_BASE,
        "icon_base": ICON_BASE,
        "process_steps": PROCESS_STEPS,
        "paint_grades": PAINT_GRADES,
        "projects": PROJECTS,
        "faqs": FAQS,
    }
