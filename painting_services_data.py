"""Page content for the regular NoBroker Painting Services catalogue."""


def page_data():
    return {
        "services": [
            {
                "title": "Interior Painting",
                "tag": "MOST POPULAR",
                "photo": "interior-painting.jpg",
                "alt": "NoBroker painting professional in a freshly painted living room",
                "icon": "home",
                "summary": "A fresh, lasting finish for bedrooms, living rooms and every space in between.",
                "points": [
                    "Transparent pricing with no hidden costs; jobs from ₹2,000",
                    "2,200+ shades and 1,000+ texture ideas to choose from",
                    "Skilled painting partners with 300+ hours of training",
                ],
                "more": ["Furniture and electrical outlet masking", "Branded paints and a thorough handover"],
            },
            {
                "title": "Exterior Painting",
                "tag": "WEATHER READY",
                "photo": "exterior-painting.png",
                "alt": "Freshly painted home exterior with a warm protective finish",
                "icon": "shield",
                "summary": "Protect your exterior walls with paint and preparation suited to the weather.",
                "points": [
                    "Weather-proof and anti-algal protection",
                    "Jet washing and crack filling as part of surface preparation",
                    "Accurate quotation with a detailed cost breakdown",
                ],
                "more": ["Options for exterior wall finishes", "Careful masking around windows and fixtures"],
            },
            {
                "title": "Quick Move-in Painting",
                "tag": "MOVE IN READY",
                "photo": "quick-move-in.jpg",
                "alt": "Painter preparing a bright home for move-in",
                "icon": "spark",
                "summary": "Get your new or rental home ready, with cleanup included after painting.",
                "points": [
                    "Quick move-in painting with post-painting cleanup",
                    "A practical choice for rentals and quick refreshes",
                    "Budget-friendly options starting at ₹2,000",
                ],
                "more": ["Room-by-room planning", "Confirm the shade and scope before work begins"],
            },
            {
                "title": "24-hour Painting",
                "tag": "QUICK REFRESH",
                "photo": "express-painting.jpg",
                "alt": "Painter applying a clean white finish to an interior wall",
                "icon": "clock",
                "summary": "A fast refresh for select rooms, touch-ups and rental move-in or move-out needs.",
                "points": [
                    "Painting completed in as little as 24 hours for eligible jobs",
                    "Designed for rental move-ins, move-outs and touch-ups",
                    "Affordable packages starting around ₹4,500",
                ],
                "more": ["Final schedule depends on room size and surface condition", "Ask for an estimate before confirming"],
            },
            {
                "title": "Waterproofing",
                "tag": "WALL HEALTH",
                "photo": "waterproofing.png",
                "alt": "Home service professional applying waterproofing treatment",
                "icon": "droplet",
                "summary": "Identify dampness and protect vulnerable areas with a considered waterproofing plan.",
                "points": [
                    "Leakage detection and dampness solutions",
                    "Terrace, bathroom and external wall options",
                    "Jobs from ₹2,000 onwards, based on an inspection",
                ],
                "more": ["The inspection helps identify the likely source", "Recommended scope and estimate are shared before work"],
            },
        ],
        "process_steps": [
            {"number": "01", "title": "Book a home inspection", "copy": "Tell us when you would like an expert to visit and review your painting needs.", "icon": "calendar"},
            {"number": "02", "title": "Measure and estimate", "copy": "Get a measured scope with an estimate and clear cost breakdown.", "icon": "ruler"},
            {"number": "03", "title": "Paint and hand over", "copy": "The team prepares, paints and completes a post-work quality check.", "icon": "check"},
        ],
        "faqs": [
            {"question": "How much do painting services cost?", "answer": "Pricing depends on the area, surface condition, paint and selected finish. Many listed jobs start at ₹2,000. Request a free estimate to get a measured quote for your home."},
            {"question": "Can I choose the paint colour and finish?", "answer": "Yes. Explore shade and texture options with the painting consultant, then confirm the selected colours before work begins."},
            {"question": "Does the estimate include paint and labour?", "answer": "The estimate explains the recommended scope and its costs. Review the material and labour breakdown with the consultant before you confirm the project."},
            {"question": "Can I book exterior painting or waterproofing?", "answer": "Yes. Choose the service above and request an inspection. The expert can review the surface and suggest the suitable scope."},
        ],
    }
