# ─────────────────────────────────────────────────────────────
# Hashtag Recommender
# Source: Curated from Sprout Social 2024 + HubSpot Benchmarks
# Logic: Returns top hashtags by niche and platform
# ─────────────────────────────────────────────────────────────

# Hashtag database — organised by niche, then platform
HASHTAG_DATABASE = {
    "technology": {
        "instagram": ["#Tech", "#Technology", "#AI", "#MachineLearning",
                      "#Python", "#DataScience", "#Coding", "#Developer",
                      "#Innovation", "#TechTrends", "#Programming", "#ML"],
        "twitter":   ["#AI", "#MachineLearning", "#Python", "#DataScience",
                      "#TechTwitter", "#OpenSource", "#DeepLearning",
                      "#Tech", "#Coding", "#Innovation"],
        "linkedin":  ["#Technology", "#Innovation", "#AI", "#DigitalTransformation",
                      "#MachineLearning", "#DataScience", "#Leadership",
                      "#FutureOfWork", "#Tech", "#Automation"],
        "youtube":   ["#Tech", "#Technology", "#AI", "#Programming",
                      "#TechReview", "#Coding", "#Developer", "#MachineLearning",
                      "#Python", "#TechTips"]
    },
    "fitness": {
        "instagram": ["#Fitness", "#FitnessMotivation", "#Workout", "#Gym",
                      "#HealthyLifestyle", "#FitLife", "#Training", "#Exercise",
                      "#Health", "#WellnessJourney", "#FitFam", "#GymLife"],
        "twitter":   ["#Fitness", "#Workout", "#Health", "#FitnessMotivation",
                      "#Exercise", "#Gym", "#HealthyLiving", "#FitLife",
                      "#Training", "#Wellness"],
        "linkedin":  ["#Health", "#Wellness", "#Fitness", "#WorkLifeBalance",
                      "#MentalHealth", "#Productivity", "#HealthyHabits",
                      "#Mindfulness", "#Leadership", "#PersonalDevelopment"],
        "youtube":   ["#Fitness", "#Workout", "#GymMotivation", "#Exercise",
                      "#Health", "#FitnessJourney", "#Training", "#Gym",
                      "#HealthyLifestyle", "#FitLife"]
    },
    "food": {
        "instagram": ["#Food", "#FoodPhotography", "#Foodie", "#FoodLovers",
                      "#Recipe", "#Cooking", "#Homemade", "#FoodBlogger",
                      "#Delicious", "#FoodPorn", "#InstaFood", "#Yummy"],
        "twitter":   ["#Food", "#Recipe", "#Cooking", "#Foodie",
                      "#FoodTwitter", "#Homemade", "#FoodLovers",
                      "#Delicious", "#Chef", "#FoodBlog"],
        "linkedin":  ["#FoodIndustry", "#Hospitality", "#FoodBusiness",
                      "#Restaurant", "#FoodTech", "#Sustainability",
                      "#FoodInnovation", "#Entrepreneurship"],
        "youtube":   ["#Food", "#Recipe", "#Cooking", "#Foodie",
                      "#CookingChannel", "#HomeCooking", "#FoodReview",
                      "#EasyRecipes", "#Chef", "#FoodVlog"]
    },
    "travel": {
        "instagram": ["#Travel", "#Wanderlust", "#TravelPhotography",
                      "#TravelBlogger", "#Adventure", "#Explore",
                      "#TravelGram", "#Vacation", "#TravelLife", "#WorldTravel",
                      "#InstaTravel", "#TravelInspiration"],
        "twitter":   ["#Travel", "#Wanderlust", "#Adventure", "#TravelTips",
                      "#Explore", "#TravelBlogger", "#Vacation",
                      "#TravelPhotography", "#Backpacking", "#Tourism"],
        "linkedin":  ["#Travel", "#BusinessTravel", "#WorkFromAnywhere",
                      "#TravelIndustry", "#Tourism", "#DigitalNomad",
                      "#RemoteWork", "#Hospitality", "#Adventure"],
        "youtube":   ["#Travel", "#TravelVlog", "#Adventure", "#Explore",
                      "#TravelGuide", "#Wanderlust", "#Backpacking",
                      "#TravelTips", "#Vacation", "#TravelChannel"]
    },
    "finance": {
        "instagram": ["#Finance", "#Money", "#Investing", "#PersonalFinance",
                      "#Wealth", "#FinancialFreedom", "#Investment",
                      "#MoneyTips", "#FinanceTips", "#StockMarket",
                      "#Crypto", "#FinancialLiteracy"],
        "twitter":   ["#Finance", "#Investing", "#StockMarket", "#Crypto",
                      "#PersonalFinance", "#FinTwit", "#Money",
                      "#Wealth", "#Trading", "#FinancialFreedom"],
        "linkedin":  ["#Finance", "#Investment", "#Fintech", "#Banking",
                      "#WealthManagement", "#Economy", "#FinancialServices",
                      "#Investing", "#Leadership", "#Business"],
        "youtube":   ["#Finance", "#Investing", "#PersonalFinance", "#Money",
                      "#StockMarket", "#Crypto", "#FinanceTips",
                      "#Wealth", "#FinancialFreedom", "#Investment"]
    },
    "education": {
        "instagram": ["#Education", "#Learning", "#Study", "#Students",
                      "#Knowledge", "#Teaching", "#EdTech", "#School",
                      "#College", "#OnlineLearning", "#StudyGram", "#Academia"],
        "twitter":   ["#Education", "#EdTech", "#Learning", "#Teaching",
                      "#HigherEd", "#EduTwitter", "#Students", "#Study",
                      "#OnlineLearning", "#Academia"],
        "linkedin":  ["#Education", "#Learning", "#EdTech", "#Leadership",
                      "#ProfessionalDevelopment", "#HigherEducation",
                      "#Elearning", "#Skills", "#Teaching", "#Career"],
        "youtube":   ["#Education", "#Learning", "#Tutorial", "#HowTo",
                      "#Study", "#OnlineLearning", "#EdTech", "#Teaching",
                      "#Knowledge", "#Skills"]
    },
    "fashion": {
        "instagram": ["#Fashion", "#Style", "#OOTD", "#FashionBlogger",
                      "#Outfit", "#Fashionista", "#FashionPhotography",
                      "#Streetstyle", "#Trending", "#FashionDesign",
                      "#Lookbook", "#FashionInspiration"],
        "twitter":   ["#Fashion", "#Style", "#OOTD", "#FashionTwitter",
                      "#Trending", "#FashionBlogger", "#Outfit",
                      "#Fashionista", "#StyleInspo", "#FashionWeek"],
        "linkedin":  ["#Fashion", "#FashionIndustry", "#Sustainability",
                      "#FashionBusiness", "#Retail", "#Entrepreneurship",
                      "#FashionTech", "#Innovation", "#Design"],
        "youtube":   ["#Fashion", "#Style", "#OOTD", "#FashionHaul",
                      "#Lookbook", "#FashionVlog", "#Outfit",
                      "#FashionTips", "#Trending", "#StyleGuide"]
    },
    "gaming": {
        "instagram": ["#Gaming", "#Gamer", "#VideoGames", "#GamersOfInstagram",
                      "#GamingCommunity", "#Esports", "#PCGaming",
                      "#PlayStation", "#Xbox", "#NintendoSwitch",
                      "#GamingSetup", "#GamingLife"],
        "twitter":   ["#Gaming", "#Gamer", "#VideoGames", "#GamingTwitter",
                      "#Esports", "#PCGaming", "#Xbox", "#PlayStation",
                      "#NintendoSwitch", "#GameDev"],
        "linkedin":  ["#Gaming", "#Esports", "#GameDevelopment", "#GamingIndustry",
                      "#Tech", "#Innovation", "#VirtualReality",
                      "#Metaverse", "#GameDesign"],
        "youtube":   ["#Gaming", "#Gamer", "#VideoGames", "#GamingChannel",
                      "#Gameplay", "#Esports", "#PCGaming",
                      "#GamingSetup", "#GameReview", "#LetsPlay"]
    },
    "business": {
        "instagram": ["#Business", "#Entrepreneur", "#Startup", "#Success",
                      "#Motivation", "#BusinessTips", "#Marketing",
                      "#Entrepreneurship", "#SmallBusiness", "#CEO",
                      "#BusinessMindset", "#GrowthHacking"],
        "twitter":   ["#Business", "#Entrepreneur", "#Startup", "#Marketing",
                      "#Success", "#SmallBusiness", "#CEO", "#Leadership",
                      "#Entrepreneurship", "#BusinessTips"],
        "linkedin":  ["#Business", "#Leadership", "#Entrepreneurship",
                      "#Innovation", "#Strategy", "#Marketing",
                      "#Management", "#Startup", "#Growth", "#B2B"],
        "youtube":   ["#Business", "#Entrepreneur", "#Startup", "#Success",
                      "#BusinessTips", "#Marketing", "#Entrepreneurship",
                      "#SmallBusiness", "#HowToBusiness", "#CEO"]
    },
    "lifestyle": {
        "instagram": ["#Lifestyle", "#LifestyleBlogger", "#DailyLife",
                      "#LiveYourBestLife", "#Inspiration", "#Motivation",
                      "#Mindset", "#SelfCare", "#Wellness", "#Happiness",
                      "#GoodVibes", "#PositiveVibes"],
        "twitter":   ["#Lifestyle", "#Motivation", "#Inspiration", "#SelfCare",
                      "#Wellness", "#Mindset", "#Happiness", "#GoodVibes",
                      "#PositiveVibes", "#DailyLife"],
        "linkedin":  ["#Lifestyle", "#WorkLifeBalance", "#Mindfulness",
                      "#PersonalDevelopment", "#Leadership", "#Wellness",
                      "#Productivity", "#Motivation", "#Success"],
        "youtube":   ["#Lifestyle", "#DailyVlog", "#LifestyleVlog",
                      "#SelfCare", "#Wellness", "#Motivation",
                      "#DayInMyLife", "#Inspiration", "#Mindset", "#Happiness"]
    }
}

def get_hashtags(niche, platform, count=10):
    """
    Returns top hashtags for a given niche and platform.

    Parameters:
        niche    : str — content category (e.g. "technology", "fitness")
        platform : str — social media platform (e.g. "instagram", "twitter")
        count    : int — number of hashtags to return (default 10)

    Returns:
        list of hashtag strings
    """

    # Normalize input to lowercase
    niche    = niche.lower().strip()
    platform = platform.lower().strip()

    # Check if niche exists in our database
    if niche not in HASHTAG_DATABASE:
        # Return general hashtags if niche not found
        return ["#Content", "#Creator", "#SocialMedia", "#Trending",
                "#Viral", "#Follow", "#Like", "#Share",
                "#ContentCreator", "#Digital"]

    # Check if platform exists for this niche
    if platform not in HASHTAG_DATABASE[niche]:
        # Default to instagram if platform not found
        platform = "instagram"

    hashtags = HASHTAG_DATABASE[niche][platform]

    # Return requested count
    return hashtags[:count]


def get_all_niches():
    """Returns list of all available niches."""
    return list(HASHTAG_DATABASE.keys())


def get_all_platforms():
    """Returns list of all supported platforms."""
    return ["instagram", "twitter", "linkedin", "youtube"]


# ── Test the module ───────────────────────────────────────────
if __name__ == "__main__":

    print("=" * 50)
    print("HASHTAG RECOMMENDER TEST")
    print("=" * 50)

    test_cases = [
        ("technology", "instagram"),
        ("fitness",    "twitter"),
        ("food",       "youtube"),
        ("finance",    "linkedin"),
        ("gaming",     "instagram"),
    ]

    for niche, platform in test_cases:
        hashtags = get_hashtags(niche, platform, count=5)
        print(f"\nNiche: {niche} | Platform: {platform}")
        print(f"Top 5 Hashtags: {' '.join(hashtags)}")

    print("\nAvailable niches:", get_all_niches())