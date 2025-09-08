import streamlit as st
import datetime
from datetime import datetime, timedelta
import pytz

# Page configuration
st.set_page_config(
    page_title="Days Until Reunion",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Center alignment for all content */
    .main {
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Title styling */
    h1 {
        color: white !important;
        text-align: center;
        font-weight: 300 !important;
        margin-bottom: 10px !important;
    }
    
    /* Countdown container */
    .countdown-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
    }
    
    /* Time unit styling */
    .time-unit {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .time-unit:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.3);
    }
    
    /* Number styling */
    .time-number {
        font-size: 48px;
        font-weight: 700;
        color: white;
        line-height: 1;
    }
    
    /* Label styling */
    .time-label {
        font-size: 14px;
        color: rgba(255, 255, 255, 0.8);
        text-transform: uppercase;
        margin-top: 8px;
    }
    
    /* Meeting date display */
    .meeting-date {
        color: white;
        font-size: 24px;
        text-align: center;
        margin: 20px 0;
        font-weight: 300;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: white;
        color: #667eea;
        border: none;
        padding: 12px 40px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: auto;
        margin: 0 auto;
        display: block;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Date input styling */
    .stDateInput > div > div > input {
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        background: rgba(255, 255, 255, 0.1);
        color: white;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Success message styling */
    .stSuccess {
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'meeting_date' not in st.session_state:
    # Default to 30 days from now (or next Valentine's Day if it's in the future)
    today = datetime.now()
    next_valentines = datetime(today.year, 2, 14, 0, 0, 0)
    
    # If Valentine's Day has passed this year, use next year's
    if next_valentines < today:
        next_valentines = datetime(today.year + 1, 2, 14, 0, 0, 0)
    
    # Use Valentine's Day if it's within reasonable range, otherwise 30 days from now
    if (next_valentines - today).days <= 365:
        st.session_state.meeting_date = next_valentines
    else:
        st.session_state.meeting_date = today + timedelta(days=30)
else:
    # Check if existing meeting date is in the past and reset if needed
    if st.session_state.meeting_date < datetime.now():
        st.session_state.meeting_date = datetime.now() + timedelta(days=30)

if 'show_date_picker' not in st.session_state:
    st.session_state.show_date_picker = False

def calculate_time_until_meeting():
    """Calculate time remaining until meeting date"""
    now = datetime.now()
    meeting = st.session_state.meeting_date
    
    # If meeting date is in the past, return zeros
    if meeting < now:
        return 0, 0, 0, 0
    
    # Calculate difference
    time_diff = meeting - now
    
    # Extract days, hours, minutes, seconds
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

def format_meeting_date():
    """Format meeting date for display"""
    return st.session_state.meeting_date.strftime("%B %d, %Y")

# Main app
st.markdown("<h1>💚 Days Until Reunion 💚</h1>", unsafe_allow_html=True)

# Check if meeting date is in the past
if st.session_state.meeting_date < datetime.now():
    st.warning("⚠️ Your meeting date is in the past! Please set a new date.")

# Meeting date display
st.markdown(f'<div class="meeting-date">{format_meeting_date()}</div>', unsafe_allow_html=True)

# Create countdown display
days, hours, minutes, seconds = calculate_time_until_meeting()

# Countdown container
st.markdown('<div class="countdown-box">', unsafe_allow_html=True)

# Create 4 columns for time units
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f'''
        <div class="time-unit">
            <div class="time-number">{days:02d}</div>
            <div class="time-label">Days</div>
        </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
        <div class="time-unit">
            <div class="time-number">{hours:02d}</div>
            <div class="time-label">Hours</div>
        </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
        <div class="time-unit">
            <div class="time-number">{minutes:02d}</div>
            <div class="time-label">Minutes</div>
        </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown(f'''
        <div class="time-unit">
            <div class="time-number">{seconds:02d}</div>
            <div class="time-label">Seconds</div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Add some space
st.markdown("<br>", unsafe_allow_html=True)

# Button to set meeting date
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Set Meeting Date", use_container_width=True):
        st.session_state.show_date_picker = not st.session_state.show_date_picker

# Date picker (shown when button is clicked)
if st.session_state.show_date_picker:
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Calculate min and max dates
        min_date = datetime.now().date()
        max_date = min_date + timedelta(days=365 * 10)  # 10 years from now
        
        # Ensure current meeting date is within bounds
        current_meeting_date = st.session_state.meeting_date.date()
        if current_meeting_date < min_date:
            current_meeting_date = min_date
        elif current_meeting_date > max_date:
            current_meeting_date = max_date
        
        new_date = st.date_input(
            "Choose your meeting date:",
            value=current_meeting_date,
            min_value=min_date,
            max_value=max_date,
            key="date_picker"
        )
        
        new_time = st.time_input(
            "Choose meeting time:",
            value=st.session_state.meeting_date.time(),
            key="time_picker"
        )
        
        if st.button("Save", use_container_width=True):
            # Combine date and time
            st.session_state.meeting_date = datetime.combine(new_date, new_time)
            st.session_state.show_date_picker = False
            st.success("Meeting date updated! 💚")
            st.rerun()

# Add a manual refresh button for updating the countdown
st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Refresh Countdown ↻", use_container_width=True):
        st.rerun()
        
# Add instructions
with st.expander("ℹ️ How to use"):
    st.write("""
    1. Click **'Set Meeting Date'** to choose when you'll meet
    2. Select the date and time
    3. Click **'Save'** to update the countdown
    4. Click **'Refresh Countdown'** to update the timer
    
    Note: The countdown doesn't auto-refresh in Streamlit. Click the refresh button to update.
    """)

# Optional: Add timezone support
with st.expander("⚙️ Advanced Settings"):
    col1, col2 = st.columns(2)
    with col1:
        your_timezone = st.selectbox(
            "Your timezone:",
            pytz.common_timezones,
            index=pytz.common_timezones.index('US/Eastern') if 'US/Eastern' in pytz.common_timezones else 0
        )
    with col2:
        partner_timezone = st.selectbox(
            "Partner's timezone:",
            pytz.common_timezones,
            index=pytz.common_timezones.index('US/Pacific') if 'US/Pacific' in pytz.common_timezones else 0
        )
    st.info("Timezone support coming soon!")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: rgba(255,255,255,0.6); font-size: 14px;'>
had to nerf the relationship with distance or something
</div>
""", unsafe_allow_html=True)