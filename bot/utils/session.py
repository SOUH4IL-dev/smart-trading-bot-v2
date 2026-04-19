from datetime import datetime
import pytz

def session_filter():
    hour = datetime.now(pytz.utc).hour
    return (7 <= hour <= 16) or (12 <= hour <= 21)