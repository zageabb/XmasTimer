import streamlit as st
import time
from datetime import datetime, timedelta

# Streamlit app setup
#st.title("Countdown to Christmas")

# Add a dancing Santa GIF as background or decorative element
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px;">
        <iframe src="https://giphy.com/embed/EcWmyeOIlYQ8FloLBO/video" width="480" height="271" style="border:none;" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
        <p><a href="https://giphy.com/clips/santa-jingle-bells-christmas-discount-EcWmyeOIlYQ8FloLBO">via GIPHY</a></p>
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
        f"<h1 style='text-align: center; font-size: 64px;'>Time to Christmas: {countdown_display}</h1>",
        unsafe_allow_html=True,
    )

    time.sleep(1)
