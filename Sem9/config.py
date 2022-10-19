BOT_API_TOKEN = "5596063847:AAHudqTDymhEvjW_8QVug19SXWekw_FVn2Q"
WEATHER_API_KEY = 'aa9ac989126c8375654ebe35e72034ee'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)