import streamlit as st
import time
from datetime import datetime, timedelta

# Streamlit app setup
#st.title("Countdown to Christmas")

# Add a dancing Santa GIF as background or decorative element
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px;">
        <div class="tenor-gif-embed" data-postid="19705759" data-share-method="host" data-aspect-ratio="1" data-width="100%"><a href="https://tenor.com/view/happy-christmas-dancing-santa-gif-19705759">Happy Christmas Dancing Santa GIF</a>from <a href="https://tenor.com/search/happy+christmas-gifs">Happy Christmas GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define Christmas date for the current year
def get_christmas_date():
    today = datetime.now()
    year = today.year
    christmas_date = datetime(year, 12, 25)
    # If it's already after Christmas this year, set to next year's Christmas
    if today > christmas_date:
        christmas_date = datetime(year + 1, 12, 25)
    return christmas_date

# Get the Christmas date
christmas_date = get_christmas_date()

# Display countdown
placeholder = st.empty()

while True:
    now = datetime.now()
    time_remaining = christmas_date - now

    # Extract days, hours, minutes, and seconds from the timedelta
    days = time_remaining.days
    seconds = time_remaining.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_display = f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"

    # Update the display
    placeholder.markdown(
        f"<h1 style='text-align: center; font-size: 64px;'>Time to Christmas: <br>{countdown_display}</h1>",
        unsafe_allow_html=True,
    )

    time.sleep(1)
