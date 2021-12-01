# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json

from typing import Any, Text, Dict, List

from google.auth.transport import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, ConversationPaused, ConversationResumed, SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher

class ActionService(Action):

     def name(self) -> Text:
         return "action_service"

     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/Payment{"issue_type":"Payment"}', "title": "My Payment is not updated"},
            {"payload":'/Bounce{"issue_type":"Bounce"}', "title": "Review my bounce or penal charges"},
            {"payload":'/Extra{"issue_type":"Extra"}', "title": "I paid extra Emi or charges"},
            {"payload":'/Uninstall{"issue_type":"Uninstall"}', "title": "I want to uninstall the application"},
            {"payload":'/Locked{"issue_type":"Locked"}', "title": "My device is locked"},
            {"payload":'/Different{"issue_type":"Different"}', "title": "I am facing a different issue"},
            {"payload": '/Emi{"issue_type":"Emi"}', "title": "Need more time to pay Emi"},
            {"payload": '/Human{"issue_type":"Human"}', "title": "Need more talk to human"},

        ]
        dispatcher.utter_message(text="Please select the topic you are looking for help", buttons=buttons)


        return []



class CheckLock(Action):

    def name(self) -> Text:
        return "check_lock"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(text= "You have an overdue emi payment. Please make the payment to unlock the phone")
        return []


class CheckDevicePayment(Action):

    def name(self) -> Text:
        return "check_payment_D"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #for blob in tracker.latest_message['entities']:
        #print(tracker.slots)
        #print(tracker.latest_message)
        message="Unable to find any new payments. Please share the payment details"
        status="success";
     
        dispatcher.utter_message(text= message)
        return [SlotSet("syncstatus", status)]


class CheckPersonalPayment(Action):

    def name(self) -> Text:
        return "check_payment_P"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= "Unable to find any new payments. Please share the payment details")

        return []


class ValidateDiffForm(Action):

    def name(self) -> Text:
        return "Diff_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
    ) -> List[EventType]:
                required_slots = ["Diff_title"]

                for slot_name in required_slots:
                    if tracker.slots.get(slot_name) is None:
                        return[SlotSet("requested_slot",slot_name)]

                return[SlotSet("requested_slot",None)]


class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_Diff_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict",
            ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thanks for the information. Our customer care Executive will contact you soon")

        return[]


class CheckLoanStatus(Action):

    def name(self) -> Text:
        return "check_loan_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= "Your personal loan is not completed yet. You will be able to uninstall the "
                                       "application once it is completed.")

        return []


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        dispatcher.utter_message(text=" New Session started")

        # any slots that should be carried over should come after the
        # `session_started` event


        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events




class fetch_id(Action):

    def name(self) -> Text:
        return "fetch_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data=1
        return []


class check_bounce_charge(Action):

    def name(self) -> Text:
        return "check_bounce_charge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= "  checking ")

        return []


class Notdeducted(Action):

    def name(self) -> Text:
        return "action_Notdeducted"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= " As per our records mandate was presented and rejected by your bank citing insufficent funds  ")

        return []

class Nachmandate(Action):

    def name(self) -> Text:
        return "action_nachmandate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text= " As per our records mandate was presented and rejected by your bank stating insufficient funds."
                                       "Please confirm the payment status with your bank ")

        return []




