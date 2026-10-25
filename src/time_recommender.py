# ─────────────────────────────────────────────────────────────
# Time Recommender
# Source: Sprout Social 2024 + HubSpot Social Media Benchmarks
# Logic: Returns best posting times by platform and niche
# ─────────────────────────────────────────────────────────────

# ── Engagement Data ───────────────────────────────────────────
# Structure: platform → niche → day → best times
# Based on published research across millions of posts

POSTING_SCHEDULE = {
    "instagram": {
        "general": {
            "Monday"   : ["6:00 AM", "11:00 AM", "7:00 PM"],
            "Tuesday"  : ["8:00 AM", "2:00 PM",  "9:00 PM"],
            "Wednesday": ["9:00 AM", "1:00 PM",  "7:00 PM"],
            "Thursday" : ["7:00 AM", "12:00 PM", "7:00 PM"],
            "Friday"   : ["9:00 AM", "12:00 PM", "6:00 PM"],
            "Saturday" : ["10:00 AM","2:00 PM",  "5:00 PM"],
            "Sunday"   : ["11:00 AM","3:00 PM",  "5:00 PM"]
        },
        "technology": {
            "Monday"   : ["7:00 AM", "12:00 PM", "8:00 PM"],
            "Tuesday"  : ["9:00 AM", "1:00 PM",  "7:00 PM"],
            "Wednesday": ["7:00 AM", "12:00 PM", "7:00 PM"],
            "Thursday" : ["8:00 AM", "1:00 PM",  "8:00 PM"],
            "Friday"   : ["9:00 AM", "12:00 PM", "5:00 PM"],
            "Saturday" : ["10:00 AM","2:00 PM",  "6:00 PM"],
            "Sunday"   : ["11:00 AM","3:00 PM",  "5:00 PM"]
        },
        "fitness": {
            "Monday"   : ["5:00 AM", "12:00 PM", "7:00 PM"],
            "Tuesday"  : ["5:00 AM", "11:00 AM", "7:00 PM"],
            "Wednesday": ["5:00 AM", "12:00 PM", "7:00 PM"],
            "Thursday" : ["5:00 AM", "11:00 AM", "7:00 PM"],
            "Friday"   : ["5:00 AM", "12:00 PM", "6:00 PM"],
            "Saturday" : ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Sunday"   : ["8:00 AM", "11:00 AM", "4:00 PM"]
        },
        "food": {
            "Monday"   : ["11:00 AM","1:00 PM",  "7:00 PM"],
            "Tuesday"  : ["11:00 AM","1:00 PM",  "7:00 PM"],
            "Wednesday": ["11:00 AM","1:00 PM",  "8:00 PM"],
            "Thursday" : ["11:00 AM","1:00 PM",  "7:00 PM"],
            "Friday"   : ["11:00 AM","1:00 PM",  "6:00 PM"],
            "Saturday" : ["10:00 AM","12:00 PM", "5:00 PM"],
            "Sunday"   : ["11:00 AM","1:00 PM",  "5:00 PM"]
        },
        "fashion": {
            "Monday"   : ["9:00 AM", "1:00 PM",  "8:00 PM"],
            "Tuesday"  : ["9:00 AM", "2:00 PM",  "9:00 PM"],
            "Wednesday": ["9:00 AM", "1:00 PM",  "8:00 PM"],
            "Thursday" : ["9:00 AM", "2:00 PM",  "9:00 PM"],
            "Friday"   : ["9:00 AM", "1:00 PM",  "7:00 PM"],
            "Saturday" : ["10:00 AM","2:00 PM",  "6:00 PM"],
            "Sunday"   : ["11:00 AM","3:00 PM",  "5:00 PM"]
        }
    },
    "twitter": {
        "general": {
            "Monday"   : ["8:00 AM", "12:00 PM", "5:00 PM"],
            "Tuesday"  : ["9:00 AM", "1:00 PM",  "5:00 PM"],
            "Wednesday": ["8:00 AM", "12:00 PM", "5:00 PM"],
            "Thursday" : ["9:00 AM", "1:00 PM",  "5:00 PM"],
            "Friday"   : ["9:00 AM", "12:00 PM", "3:00 PM"],
            "Saturday" : ["10:00 AM","1:00 PM",  "4:00 PM"],
            "Sunday"   : ["11:00 AM","2:00 PM",  "4:00 PM"]
        },
        "technology": {
            "Monday"   : ["8:00 AM", "12:00 PM", "6:00 PM"],
            "Tuesday"  : ["9:00 AM", "12:00 PM", "5:00 PM"],
            "Wednesday": ["8:00 AM", "11:00 AM", "5:00 PM"],
            "Thursday" : ["8:00 AM", "12:00 PM", "5:00 PM"],
            "Friday"   : ["9:00 AM", "12:00 PM", "3:00 PM"],
            "Saturday" : ["10:00 AM","1:00 PM",  "4:00 PM"],
            "Sunday"   : ["11:00 AM","2:00 PM",  "4:00 PM"]
        },
        "business": {
            "Monday"   : ["7:00 AM", "12:00 PM", "5:00 PM"],
            "Tuesday"  : ["7:00 AM", "12:00 PM", "5:00 PM"],
            "Wednesday": ["7:00 AM", "12:00 PM", "5:00 PM"],
            "Thursday" : ["7:00 AM", "12:00 PM", "5:00 PM"],
            "Friday"   : ["7:00 AM", "12:00 PM", "3:00 PM"],
            "Saturday" : ["9:00 AM", "12:00 PM", "3:00 PM"],
            "Sunday"   : ["10:00 AM","1:00 PM",  "3:00 PM"]
        }
    },
    "linkedin": {
        "general": {
            "Monday"   : ["7:00 AM", "12:00 PM", "5:00 PM"],
            "Tuesday"  : ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Wednesday": ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Thursday" : ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Friday"   : ["7:00 AM", "10:00 AM", "1:00 PM"],
            "Saturday" : ["10:00 AM","12:00 PM", "2:00 PM"],
            "Sunday"   : ["Skip — low LinkedIn engagement on Sundays"]
        },
        "technology": {
            "Monday"   : ["7:00 AM", "12:00 PM", "6:00 PM"],
            "Tuesday"  : ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Wednesday": ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Thursday" : ["8:00 AM", "12:00 PM", "5:00 PM"],
            "Friday"   : ["7:00 AM", "10:00 AM", "1:00 PM"],
            "Saturday" : ["10:00 AM","12:00 PM", "2:00 PM"],
            "Sunday"   : ["Skip — low LinkedIn engagement on Sundays"]
        },
        "business": {
            "Monday"   : ["6:00 AM", "12:00 PM", "6:00 PM"],
            "Tuesday"  : ["6:00 AM", "10:00 AM", "6:00 PM"],
            "Wednesday": ["6:00 AM", "10:00 AM", "6:00 PM"],
            "Thursday" : ["6:00 AM", "10:00 AM", "6:00 PM"],
            "Friday"   : ["6:00 AM", "10:00 AM", "12:00 PM"],
            "Saturday" : ["9:00 AM", "12:00 PM", "2:00 PM"],
            "Sunday"   : ["Skip — low LinkedIn engagement on Sundays"]
        },
        "education": {
            "Monday"   : ["7:00 AM", "12:00 PM", "5:00 PM"],
            "Tuesday"  : ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Wednesday": ["7:00 AM", "10:00 AM", "5:00 PM"],
            "Thursday" : ["8:00 AM", "12:00 PM", "5:00 PM"],
            "Friday"   : ["7:00 AM", "10:00 AM", "1:00 PM"],
            "Saturday" : ["10:00 AM","12:00 PM", "2:00 PM"],
            "Sunday"   : ["Skip — low LinkedIn engagement on Sundays"]
        }
    },
    "youtube": {
        "general": {
            "Monday"   : ["2:00 PM", "4:00 PM",  "8:00 PM"],
            "Tuesday"  : ["2:00 PM", "4:00 PM",  "8:00 PM"],
            "Wednesday": ["2:00 PM", "4:00 PM",  "9:00 PM"],
            "Thursday" : ["2:00 PM", "4:00 PM",  "9:00 PM"],
            "Friday"   : ["2:00 PM", "4:00 PM",  "8:00 PM"],
            "Saturday" : ["9:00 AM", "11:00 AM", "4:00 PM"],
            "Sunday"   : ["9:00 AM", "11:00 AM", "5:00 PM"]
        },
        "gaming": {
            "Monday"   : ["4:00 PM", "7:00 PM",  "9:00 PM"],
            "Tuesday"  : ["4:00 PM", "7:00 PM",  "9:00 PM"],
            "Wednesday": ["4:00 PM", "7:00 PM",  "10:00 PM"],
            "Thursday" : ["4:00 PM", "7:00 PM",  "10:00 PM"],
            "Friday"   : ["3:00 PM", "6:00 PM",  "10:00 PM"],
            "Saturday" : ["10:00 AM","2:00 PM",  "8:00 PM"],
            "Sunday"   : ["10:00 AM","2:00 PM",  "8:00 PM"]
        },
        "education": {
            "Monday"   : ["2:00 PM", "5:00 PM",  "8:00 PM"],
            "Tuesday"  : ["2:00 PM", "5:00 PM",  "8:00 PM"],
            "Wednesday": ["2:00 PM", "5:00 PM",  "9:00 PM"],
            "Thursday" : ["2:00 PM", "5:00 PM",  "9:00 PM"],
            "Friday"   : ["2:00 PM", "4:00 PM",  "7:00 PM"],
            "Saturday" : ["10:00 AM","12:00 PM", "4:00 PM"],
            "Sunday"   : ["10:00 AM","12:00 PM", "5:00 PM"]
        }
    }
}

# ── Content Type Recommendations ──────────────────────────────

CONTENT_CALENDAR = {
    "Monday"   : {"theme": "Motivational Monday",  "emoji": "🔥",
                  "content_type": "Inspirational quote or personal story"},
    "Tuesday"  : {"theme": "Tutorial Tuesday",     "emoji": "📚",
                  "content_type": "How-to guide or educational post"},
    "Wednesday": {"theme": "Wisdom Wednesday",     "emoji": "🧠",
                  "content_type": "Tips, facts, or industry insights"},
    "Thursday" : {"theme": "Throwback Thursday",   "emoji": "⭐",
                  "content_type": "Behind the scenes or progress update"},
    "Friday"   : {"theme": "Feature Friday",       "emoji": "🎯",
                  "content_type": "Highlight, showcase, or achievement"},
    "Saturday" : {"theme": "Story Saturday",       "emoji": "❤️",
                  "content_type": "Personal story or community engagement"},
    "Sunday"   : {"theme": "Sunday Reflection",    "emoji": "🌟",
                  "content_type": "Weekly recap or upcoming preview"}
}

# ── Posting Frequency by Platform ─────────────────────────────

POSTING_FREQUENCY = {
    "instagram": {"per_week": 4, "note": "3-5 feed posts + daily stories"},
    "twitter"  : {"per_week": 7, "note": "1-3 tweets per day recommended"},
    "linkedin" : {"per_week": 3, "note": "Tue/Wed/Thu perform best"},
    "youtube"  : {"per_week": 1, "note": "1-2 videos per week, consistency matters"}
}


def get_best_times(platform, niche):
    """
    Returns best posting times for a platform and niche.

    Parameters:
        platform : str — e.g. "instagram", "twitter"
        niche    : str — e.g. "technology", "fitness"

    Returns:
        dict with full weekly schedule
    """

    platform = platform.lower().strip()
    niche    = niche.lower().strip()

    # Get platform data
    if platform not in POSTING_SCHEDULE:
        platform = "instagram"

    platform_data = POSTING_SCHEDULE[platform]

    # Get niche-specific schedule, fall back to general
    if niche in platform_data:
        schedule = platform_data[niche]
    else:
        schedule = platform_data["general"]

    # Find the single best time per day (first slot = peak time)
    best_per_day = {}
    for day, times in schedule.items():
        best_per_day[day] = times[0]

    # Get frequency recommendation
    frequency = POSTING_FREQUENCY.get(platform, {"per_week": 3, "note": ""})

    return {
        "platform"        : platform,
        "niche"           : niche,
        "weekly_schedule" : schedule,
        "best_per_day"    : best_per_day,
        "frequency"       : frequency,
        "content_calendar": CONTENT_CALENDAR
    }


def get_weekly_plan(platform, niche):
    """
    Returns a complete 7-day content plan.
    Combines best times + content themes.
    """

    data = get_best_times(platform, niche)
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    plan = []
    for day in days:
        calendar_info = CONTENT_CALENDAR[day]
        best_time     = data["best_per_day"].get(day, "7:00 PM")

        plan.append({
            "day"          : day,
            "theme"        : calendar_info["theme"],
            "emoji"        : calendar_info["emoji"],
            "content_type" : calendar_info["content_type"],
            "best_time"    : best_time,
            "platform"     : platform
        })

    return plan


# ── Test the module ───────────────────────────────────────────
if __name__ == "__main__":

    print("=" * 60)
    print("TIME RECOMMENDER TEST")
    print("=" * 60)

    # Test 1 — Instagram fitness schedule
    print("\nTest 1: Instagram | Fitness")
    print("-" * 60)
    result = get_best_times("instagram", "fitness")
    print(f"Platform : {result['platform']}")
    print(f"Niche    : {result['niche']}")
    print(f"Frequency: {result['frequency']['per_week']}x per week — {result['frequency']['note']}")
    print("\nBest time per day:")
    for day, time in result["best_per_day"].items():
        print(f"  {day:12} → {time}")

    # Test 2 — LinkedIn technology weekly plan
    print("\n\nTest 2: LinkedIn | Technology — Full Weekly Plan")
    print("-" * 60)
    plan = get_weekly_plan("linkedin", "technology")
    for day_plan in plan:
        print(f"{day_plan['emoji']} {day_plan['day']:12} | {day_plan['theme']:22} | Post at: {day_plan['best_time']} | {day_plan['content_type']}")

    # Test 3 — YouTube gaming
    print("\n\nTest 3: YouTube | Gaming")
    print("-" * 60)
    result = get_best_times("youtube", "gaming")
    print(f"Frequency: {result['frequency']['per_week']}x per week — {result['frequency']['note']}")
    print("\nBest time per day:")
    for day, time in result["best_per_day"].items():
        print(f"  {day:12} → {time}")