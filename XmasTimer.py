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
    f"<h1 style='text-align: center; font-size: 72px;'>Time to Christmas: {countdown_display}</h1>",
    unsafe_allow_html=True,
    )

time.sleep(1)
