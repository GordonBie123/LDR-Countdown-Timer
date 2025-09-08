# LDR-Countdown-Timer
Silly stupid app made for long distance relationships

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- **Live Countdown Timer** - Displays days, hours, minutes, and seconds until your reunion
- **Custom Date Selection** - Set any future date and time for your countdown
- **Beautiful UI** - Gradient background with glassmorphism effects
- **Responsive Design** - Works perfectly on desktop and mobile devices
- **Time Selection** - Choose both date and time for precise countdowns
- **Timezone Support** - UI for timezone selection (feature coming soon)
- **Auto-validation** - Automatically handles past dates and resets to future dates

## Demo

The app features a stunning purple gradient background with a centered countdown display showing:
- Days remaining
- Hours remaining  
- Minutes remaining
- Seconds remaining

Each time unit is displayed in its own hoverable card with smooth animations.

## Requirements

- Python 3.7 or higher
- Streamlit
- pytz

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/days-until-reunion.git
cd days-until-reunion
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install streamlit pytz
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. The app will open in your default browser at `http://localhost:8501`

3. Click "Set Meeting Date" to choose your reunion date and time

4. Click "Save" to update the countdown

5. Use "Refresh Countdown" to update the timer (Streamlit doesn't auto-refresh)

## Customization

The app features custom CSS styling that you can modify in the `app.py` file:

- **Background**: Purple gradient (`#667eea` to `#764ba2`)
- **Cards**: Semi-transparent white with glassmorphism effect
- **Hover Effects**: Smooth transitions and transforms
- **Typography**: Clean, modern font styling

## Features in Detail

### Date Selection
- Click "Set Meeting Date" to reveal date and time pickers
- Dates can be set up to 10 years in the future
- Past dates automatically reset to 30 days from today

### Time Display
- Large, easy-to-read numbers
- Hover effects on each time unit
- Zero-padded format (e.g., "09" instead of "9")

### Additional Options
- Expandable instructions section
- Timezone selection interface (backend implementation pending)
- Manual refresh button for updating the countdown

## Configuration

The app includes several configurable defaults:

- **Default countdown**: 30 days from current date (or next Valentine's Day if applicable)
- **Date range**: Current date to 10 years in the future
- **Timezones**: US/Eastern and US/Pacific as defaults

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Future Enhancements

- [ ] Auto-refresh countdown without manual button click
- [ ] Functional timezone conversion
- [ ] Save multiple countdown dates
- [ ] Share countdown link feature
- [ ] Notification when countdown reaches zero
- [ ] Custom themes and color schemes

## Known Issues

- Countdown requires manual refresh (Streamlit limitation)
- Timezone selection UI present but not yet functional

## Author

Created with love for those counting down the days until their reunion.

---

*"had to nerf the relationship with distance or something"*
