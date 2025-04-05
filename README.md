🏎️ TrackSensei

TrackSensei is a real-time data gathering and analysis application built for the Jetson Nano. It’s designed to help motorsport enthusiasts and engineers collect detailed telemetry — starting with GPS data — to analyze driver performance lap-by-lap.

📍 Current Features

Real-time GPS data logging via GNSS module (e.g. Waveshare LC29H)

Lightweight and portable Python architecture

Time-stamped raw NMEA sentence logging

Latitude and Longitude parsing from GPGGA sentences

Modular design for future sensor integration (acceleration, elevation, etc.)

💠 Project Structure

TrackSensei/
├── app/
│   ├── __init__.py
│   ├── main.py               # Entry point for data logging
│   ├── gps_functions.py      # GPS parsing and serial handling
├── data/
│   └── gps_data.txt          # Logged raw GPS data with timestamps
├── docs/
│   └── setup.md              # Setup instructions for Jetson Nano
├── requirements.txt
└── README.md

⚙️ Getting Started

git clone https://github.com/rudysuarez1/TrackSensei.git
cd TrackSensei
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app/main.py

🧹 Dependencies

pynmea2 – For parsing NMEA GPS sentences

pyserial – For communicating over UART/Serial

(see requirements.txt)

🧱 Built With

Jetson Nano 2GB

Python 3.8+

Waveshare GPS HAT (LC29H)

Pop!_OS (for development environment)

🚧 Roadmap



🤝 Contributing

Open to contributions once hardware support is stabilized. Feel free to open issues or PRs!