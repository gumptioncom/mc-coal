from pytz.gae import pytz

from config import coal_config


def datetime_filter(value, format='%A, %B %d, %Y %I:%M:%S %p'):
    tf = format
    if '%P' in format:
        tf = format.replace('%P', '%p')
    if value:
        utc_dt = pytz.utc.localize(value)
        timezone_dt = utc_dt.astimezone(pytz.timezone(coal_config.TIMEZONE))
        ts = timezone_dt.strftime(tf)
        if '%p' in format:
            ts = ts.replace('AM', 'am').replace('PM', 'pm')
        return ts
    return ''


def username_pronoun_filter(username, user):
    return "YOU" if username == user.username else username


FILTERS = {
    'datetimeformat': datetime_filter,
    'username_pronoun': username_pronoun_filter
}
