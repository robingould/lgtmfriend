import requests
from datetime import datetime, timezone, timedelta
import json

def handle_responses(msg) -> str:
    
    p_msg = msg.lower()

    if p_msg == "!test":
        return "what do you want..."
    
    if p_msg == "!add":
        return "I'm supposed to add that Github project to my list, right? Sorry.. I'll get to that in a sec... I... I don't know life just isn't the same any more I guess..."
    
    if p_msg == "!check":
        return "I'm supposed to check your Github projects here, I guess..."
    else:
        return "unknown"