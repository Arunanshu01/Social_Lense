# ─────────────────────────────────────────────────────────────
# Caption Generator
# Logic: Template-based NLG with dynamic slot filling
# Returns 3 ready-to-post captions per request
# ─────────────────────────────────────────────────────────────

import random
from hashtag_recommender import get_hashtags

# ── Template Library ──────────────────────────────────────────
# Each tone has multiple templates
# {topic} is the dynamic slot filled by user input

TEMPLATES = {
    "motivational": [
        "Every big journey starts with one small step. Today, I'm talking about {topic} — and why it matters more than you think. 🚀 Drop a 💪 if you're ready to level up!",
        "The secret to mastering {topic}? Consistency over perfection. Show up every day, even when it's hard. What's your biggest challenge with {topic}? Comment below! 👇",
        "They said it couldn't be done. But here's what I learned about {topic} that changed everything. Save this post — you'll want to come back to it. ⭐",
        "Success with {topic} doesn't happen overnight. But every expert was once a beginner. Start today. Start now. What's stopping you? 🔥",
        "One year ago I knew nothing about {topic}. Today it's changed my life. Here's the truth nobody tells you — it just takes showing up. Are you showing up? 💯"
    ],
    "educational": [
        "3 things you need to know about {topic} that nobody talks about:\n\n1️⃣ It's simpler than you think\n2️⃣ The basics matter most\n3️⃣ Consistency beats talent\n\nSave this for later! 📌",
        "Quick guide to {topic} for beginners:\n\n✅ Start with the fundamentals\n✅ Practice daily for 15 minutes\n✅ Track your progress weekly\n✅ Find a community\n\nWhich step are you on?",
        "Did you know this about {topic}? Most people get this completely wrong. Here's what the research actually says — and how you can use it today. 🧠 Share with someone who needs this!",
        "Everything I wish I knew before starting {topic}:\n\n→ Don't overcomplicate it\n→ Learn from mistakes fast\n→ Find good mentors\n→ Be patient with yourself\n\nWhich one hit different? 👇",
        "The beginner's roadmap to {topic}:\n\nWeek 1: Learn the basics\nWeek 2: Practice daily\nWeek 3: Get feedback\nWeek 4: Level up\n\nSave this and start today! 📚"
    ],
    "casual": [
        "Okay so I've been really into {topic} lately and honestly? Best decision I ever made. Anyone else obsessed? 😄",
        "Hot take: {topic} is underrated and more people need to talk about it. Who agrees? Drop a 🙋 below!",
        "Just spent the whole morning on {topic} and I have zero regrets. This is the life. 😎 What are you up to today?",
        "Not to be dramatic but {topic} literally changed my life. Okay maybe a little dramatic. But seriously though — try it. 😂",
        "Real talk — I was super skeptical about {topic} at first. Now I can't imagine my life without it. Anyone else have that experience? 👀"
    ],
    "professional": [
        "In today's rapidly evolving landscape, understanding {topic} has become essential for professionals across industries. Here are my key insights after working in this space. What's your experience?",
        "After extensive research and hands-on experience with {topic}, I've identified three critical factors that separate successful practitioners from the rest. I'd love to hear your perspective in the comments.",
        "The conversation around {topic} is evolving rapidly. As professionals, staying ahead of these trends isn't optional — it's necessary. Here's what I'm seeing in the field and what it means for our industry.",
        "{topic} presents both significant challenges and extraordinary opportunities for forward-thinking professionals. My analysis of current trends suggests three key areas to focus on. What would you add to this list?",
        "Sharing my framework for approaching {topic} effectively. After years of experience, I've found that the fundamentals matter far more than the latest trends. Agree or disagree?"
    ],
    "humorous": [
        "Me before learning about {topic}: confused 😵 Me after: still confused but make it fancy 😂 Anyone else relate?",
        "Plot twist: {topic} is actually really fun once you stop overthinking it. Past me would never believe this. 😄 Current me is thriving.",
        "Things I thought {topic} was: complicated, boring, not for me. Things {topic} actually is: still complicated but oddly enjoyable? 😂",
        "POV: You finally understand {topic} after the tenth attempt and suddenly feel like a genius 🧠✨ Just me? Okay.",
        "Nobody: \nAbsolutely nobody: \nMe at 2am: let me learn everything about {topic} 😂 No regrets though. Worth it."
    ],
    "inspirational": [
        "Your journey with {topic} is uniquely yours. Don't compare your chapter 1 to someone else's chapter 20. Keep going. 🌟",
        "The best time to start learning {topic} was yesterday. The second best time? Right now. Your future self will thank you. ✨",
        "Every expert at {topic} was once exactly where you are today — confused, unsure, but curious. That curiosity is your superpower. 💫",
        "Progress with {topic} isn't always visible. Sometimes growth happens beneath the surface. Trust the process. 🌱",
        "You don't have to be great to start {topic}. But you have to start to become great. Take that first step today. 🚀"
    ]
}

# ── Platform Character Limits ─────────────────────────────────

PLATFORM_LIMITS = {
    "twitter":   280,
    "instagram": 2200,
    "linkedin":  3000,
    "youtube":   5000
}

# ── Platform Notes ────────────────────────────────────────────

PLATFORM_TIPS = {
    "twitter":   "Keep it under 280 characters. Be punchy and direct.",
    "instagram": "Use line breaks for readability. Hashtags at the end.",
    "linkedin":  "Professional tone works best. Add insights and ask questions.",
    "youtube":   "Use in your video description. Include keywords naturally."
}


def generate_captions(topic, tone, platform, niche, count=3):
    """
    Generates ready-to-post captions for social media.

    Parameters:
        topic    : str — what the post is about (e.g. "morning workout")
        tone     : str — writing style (e.g. "motivational", "casual")
        platform : str — target platform (e.g. "instagram")
        niche    : str — content category (e.g. "fitness")
        count    : int — number of captions to generate (default 3)

    Returns:
        list of dicts, each containing caption text and hashtags
    """

    # Normalize inputs
    topic    = topic.strip()
    tone     = tone.lower().strip()
    platform = platform.lower().strip()
    niche    = niche.lower().strip()

    # Fallback to motivational if tone not found
    if tone not in TEMPLATES:
        tone = "motivational"

    # Get templates for this tone
    available_templates = TEMPLATES[tone]

    # Randomly select 'count' different templates
    # If we don't have enough, use all available
    selected = random.sample(
        available_templates,
        min(count, len(available_templates))
    )

    # Get hashtags for this niche and platform
    hashtags = get_hashtags(niche, platform, count=8)
    hashtag_string = ' '.join(hashtags)

    # Build caption results
    results = []
    for i, template in enumerate(selected):

        # Fill in the topic slot
        caption_text = template.replace('{topic}', topic)

        # For Twitter, trim if too long
        if platform == "twitter":
            # Twitter limit: 280 chars including hashtags
            # Reserve 60 chars for hashtags
            max_caption_length = 200
            if len(caption_text) > max_caption_length:
                caption_text = caption_text[:max_caption_length] + "..."

            # Use fewer hashtags on Twitter
            twitter_hashtags = get_hashtags(niche, platform, count=3)
            final_hashtags = ' '.join(twitter_hashtags)
        else:
            final_hashtags = hashtag_string

        results.append({
            "caption_number" : i + 1,
            "caption"        : caption_text,
            "hashtags"       : final_hashtags,
            "platform"       : platform,
            "tone"           : tone,
            "character_count": len(caption_text),
            "platform_tip"   : PLATFORM_TIPS.get(platform, "")
        })

    return results


def get_available_tones():
    """Returns list of all available tones."""
    return list(TEMPLATES.keys())


# ── Test the module ───────────────────────────────────────────
if __name__ == "__main__":

    print("=" * 60)
    print("CAPTION GENERATOR TEST")
    print("=" * 60)

    # Test 1 — Motivational fitness caption for Instagram
    print("\nTest 1: Fitness | Motivational | Instagram")
    print("-" * 60)
    captions = generate_captions(
        topic    = "morning workout routine",
        tone     = "motivational",
        platform = "instagram",
        niche    = "fitness"
    )
    for c in captions:
        print(f"\nCaption {c['caption_number']}:")
        print(c['caption'])
        print(f"Hashtags: {c['hashtags']}")
        print(f"Characters: {c['character_count']}")

    # Test 2 — Educational tech caption for LinkedIn
    print("\n\nTest 2: Technology | Educational | LinkedIn")
    print("-" * 60)
    captions = generate_captions(
        topic    = "machine learning for beginners",
        tone     = "educational",
        platform = "linkedin",
        niche    = "technology"
    )
    for c in captions:
        print(f"\nCaption {c['caption_number']}:")
        print(c['caption'])
        print(f"Hashtags: {c['hashtags']}")

    # Test 3 — Casual food caption for Twitter
    print("\n\nTest 3: Food | Casual | Twitter")
    print("-" * 60)
    captions = generate_captions(
        topic    = "homemade pasta",
        tone     = "casual",
        platform = "twitter",
        niche    = "food"
    )
    for c in captions:
        print(f"\nCaption {c['caption_number']}:")
        print(c['caption'])
        print(f"Hashtags: {c['hashtags']}")

    print("\nAvailable tones:", get_available_tones())
    