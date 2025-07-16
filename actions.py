from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

# Sample data — in real life, connect to DB or API
STRAIN_DB = {
    "indica": ["Granddaddy Purple", "Northern Lights", "Purple Kush"],
    "sativa": ["Sour Diesel", "Jack Herer", "Durban Poison"],
    "hybrid": ["Gelato", "Wedding Cake", "Blue Dream"]
}

SLANG_DEFINITIONS = {
    "zaza": "High-quality exotic cannabis, known for its potent effects and unique flavor.",
    "boof": "Low-quality or fake weed that’s not worth your time.",
    "rig": "A device used to vaporize cannabis concentrates, usually for dabbing."
}

MUNCHIE_SNACKS = [
    "Gummy bears",
    "Hot Cheetos",
    "Frozen grapes",
    "Nutella waffles",
    "Popcorn with extra butter"
]

# Action to greet user
class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        greetings = [
            "What’s up, my leafy friend? 🌱",
            "Peace and potency! How can I elevate your day?",
            "Yo yo yo! Ready to get lifted?",
            "Greetings from the ganja galaxy. How can I help?"
        ]
        dispatcher.utter_message(text=random.choice(greetings))
        return []

# Action to say goodbye
class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        farewells = [
            "Catch you on the next cloud ☁️",
            "Stay grounded, stay high 🌿",
            "Peace, love, and perfectly rolled blunts ✌️",
            "Later bud! May your vibes stay lifted"
        ]
        dispatcher.utter_message(text=random.choice(farewells))
        return []

# Action to recommend strain by type
class ActionRecommendStrain(Action):
    def name(self) -> Text:
        return "action_recommend_strain"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        strain_type = None
        for ent in tracker.latest_message.get("entities", []):
            if ent.get("entity") == "strain_type":
                strain_type = ent.get("value").lower()
                break

        if strain_type and strain_type in STRAIN_DB:
            strain = random.choice(STRAIN_DB[strain_type])
            msg = f"How about trying *{strain}*? It's a solid {strain_type} with great vibes."
        else:
            all_strains = [s for strains in STRAIN_DB.values() for s in strains]
            strain = random.choice(all_strains)
            msg = f"Can't decide? Try *{strain}* — a crowd favorite across the board."

        dispatcher.utter_message(text=msg)
        return []

# Action to define slang terms
class ActionDefineSlang(Action):
    def name(self) -> Text:
        return "action_define_slang"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slang_term = None
        for ent in tracker.latest_message.get("entities", []):
            if ent.get("entity") == "slang_term":
                slang_term = ent.get("value").lower()
                break

        if slang_term and slang_term in SLANG_DEFINITIONS:
            definition = SLANG_DEFINITIONS[slang_term]
            msg = f"*{slang_term.title()}*: {definition}"
        else:
            msg = "That slang term’s a mystery to me — wanna try another?"

        dispatcher.utter_message(text=msg)
        return []

# Action to suggest munchie snacks
class ActionSuggestMunchies(Action):
    def name(self) -> Text:
        return "action_suggest_munchies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        snack = random.choice(MUNCHIE_SNACKS)
        msg = f"Got the munchies? How about some *{snack}* to keep your vibes tasty?"
        dispatcher.utter_message(text=msg)
        return []

# Action to handle fallback when no intent matches
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msgs = [
            "Hmm, I’m not sure I caught that — wanna rephrase?",
            "My digital budtender skills are rusty, can you try again?",
            "Lost in the haze, help me out with that one?"
        ]
        dispatcher.utter_message(text=random.choice(msgs))
        return []

# Action to provide grow tips
class ActionGrowTips(Action):
    def name(self) -> Text:
        return "action_grow_tips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tips = [
            "Use LED lights for efficient and consistent growth.",
            "Keep your grow room temperature between 70-85°F for best results.",
            "Make sure your plants get good airflow to avoid mold.",
            "Water only when the top inch of soil is dry — don’t overdo it!"
        ]
        msg = random.choice(tips)
        dispatcher.utter_message(text=msg)
        return []

# Action to provide legal info based on region (dummy example)
class ActionLegalInfo(Action):
    def name(self) -> Text:
        return "action_legal_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = None
        for ent in tracker.latest_message.get("entities", []):
            if ent.get("entity") == "location":
                location = ent.get("value").lower()
                break

        if location == "california":
            msg = "In California, adults 21+ can possess up to 28.5 grams of cannabis for personal use."
        elif location == "new york":
            msg = "New York allows possession of up to 3 ounces of cannabis for recreational users 21 and over."
        else:
            msg = "Cannabis laws vary widely. Drop your state or country and I'll get you the deets!"

        dispatcher.utter_message(text=msg)
        return []

# Add more actions here as needed for expanded features.