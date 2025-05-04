from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from .spirituality_data import (
    get_concept_info,
    get_meditation_guide,
    get_sacred_text_info,
    get_practice_guide
)

class ActionFetchConceptInfo(Action):
    def name(self) -> Text:
        return "action_fetch_concept_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        concept = tracker.get_slot("concept")
        if not concept:
            dispatcher.utter_message(text="I'm not sure which concept you're asking about. Could you specify?")
            return []
        
        concept_info = get_concept_info(concept.lower())
        
        if concept_info:
            message = f"**{concept.title()}**\n\n{concept_info['description']}"
            
            if "related_concepts" in concept_info and concept_info["related_concepts"]:
                related = ", ".join(concept_info["related_concepts"])
                message += f"\n\nRelated concepts you might explore: {related}"
            
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text=f"I don't have specific information about {concept}. Would you like to explore another concept?")
        
        return []

class ActionSuggestMeditation(Action):
    def name(self) -> Text:
        return "action_suggest_meditation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        experience_level = tracker.get_slot("experience_level")
        time_available = tracker.get_slot("time_available")
        
        if not experience_level:
            experience_level = "beginner"
            
        if not time_available:
            time_available = 10  # Default to 10 minutes
        else:
            try:
                time_available = float(time_available)
            except (ValueError, TypeError):
                time_available = 10
        
        meditation = get_meditation_guide(experience_level, time_available)
        
        if meditation:
            message = f"**{meditation['name']}**\n\n"
            message += f"Duration: {meditation['duration']} minutes\n\n"
            message += f"{meditation['instructions']}"
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="I don't have a specific meditation practice that matches your criteria. Would you like a general meditation guide?")
        
        return []

class ActionExploreSacredText(Action):
    def name(self) -> Text:
        return "action_explore_sacred_text"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        sacred_text = tracker.get_slot("sacred_text")
        if not sacred_text:
            dispatcher.utter_message(text="Which sacred text would you like to learn about?")
            return []
        
        text_info = get_sacred_text_info(sacred_text.lower())
        
        if text_info:
            message = f"**{text_info['name']}**\n\n{text_info['description']}"
            
            if "key_teachings" in text_info and text_info["key_teachings"]:
                teachings = "\n- ".join(text_info["key_teachings"])
                message += f"\n\n**Key Teachings:**\n- {teachings}"
            
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text=f"I don't have specific information about {sacred_text}. Would you like to explore another text?")
        
        return []

class ActionProvideSpiritualPractice(Action):
    def name(self) -> Text:
        return "action_provide_spiritual_practice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        practice_type = tracker.get_slot("practice_type")
        if not practice_type:
            dispatcher.utter_message(text="What type of spiritual practice are you interested in?")
            return []
        
        practice_guide = get_practice_guide(practice_type.lower())
        
        if practice_guide:
            message = f"**{practice_guide['name']}**\n\n{practice_guide['description']}\n\n"
            message += f"**Steps:**\n{practice_guide['steps']}"
            
            if "benefits" in practice_guide and practice_guide["benefits"]:
                benefits = "\n- ".join(practice_guide["benefits"])
                message += f"\n\n**Benefits:**\n- {benefits}"
            
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text=f"I don't have specific information about {practice_type}. Would you like to explore another spiritual practice?")
        
        return []
    
class ActionRespondToSpiritualChitchat(Action):
    def name(self) -> Text:
        return "action_respond_to_spiritual_chitchat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = tracker.latest_message.get('text')
        
        # Simple responses for common chitchat
        chitchat_responses = {
            "hello": "Namaste 🙏 How can I assist you on your spiritual journey today?",
            "hi": "Namaste 🙏 How can I assist you on your spiritual journey today?",
            "namaste": "Namaste 🙏 I'm honored to connect with you.",
            "thank you": "You're welcome. May your spiritual journey bring you peace and wisdom.",
            "thanks": "You're welcome. May your spiritual journey bring you peace and wisdom.",
            "goodbye": "Namaste 🙏 May peace and clarity accompany you on your spiritual journey."
        }
        
        # Check for matches in simple chitchat
        for key, response in chitchat_responses.items():
            if key in message.lower():
                dispatcher.utter_message(text=response)
                return []
        
        # Default response for other chitchat
        dispatcher.utter_message(text="I'm here to help with your questions about Indian spirituality. Feel free to ask about specific concepts, meditation practices, or sacred texts.")
        return [] 