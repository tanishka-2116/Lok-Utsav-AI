import difflib

festival_data = {
    "diwali": "Diwali is the festival of lights celebrating victory of good over evil...",
    "holi": "Holi is the festival of colors marking spring and triumph of good over evil...",
    "ganesh chaturthi": "Ganesh Chaturthi celebrates birth of Lord Ganesha...",
    "navratri": "Navratri is nine nights of worship dedicated to Goddess Durga...",
    "maha shivratri": "Mahashivratri marks the divine marriage of Shiva and Parvati...",
    "rath yatra": "Rath Yatra is the chariot festival of Lord Jagannath in Puri..."
}

def get_festival_answer(query):
    query = query.lower()

    matches = difflib.get_close_matches(query, festival_data.keys(), n=1, cutoff=0.4)

    if matches:
        return festival_data[matches[0]]
    else:
        return "Sorry, I could not find information about that festival yet."

