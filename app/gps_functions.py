# gps_functions.py

import serial
import time
import pynmea2
from collections import deque
import config  # Import the configuration module

# Initialize a deque to store the last N GPS readings for filtering
gps_buffer = deque(maxlen=10)

def parse_nmea_sentence(sentence):
    """
    Parse a single NMEA sentence and return a pynmea2 message object.
    """
    try:
        return pynmea2.parse(sentence)
    except pynmea2.nmea.ParseError:
        return None

def extract_location_data(msg):
    """
    Extract latitude and longitude from a pynmea2 message object.
    """
    if isinstance(msg, pynmea2.GGA):
        lat = msg.latitude
        lon = msg.longitude
        return lat, lon
    return None, None

def filter_gps_data(lat, lon):
    """
    Apply a simple moving average filter to GPS data to reduce noise.
    """
    gps_buffer.append((lat, lon))
    if len(gps_buffer) == gps_buffer.maxlen:
        avg_lat = sum(lat for lat, lon in gps_buffer) / len(gps_buffer)
        avg_lon = sum(lon for lat, lon in gps_buffer) / len(gps_buffer)
        return avg_lat, avg_lon
    return lat, lon

def read_gps_data():
    """
    Continuously read GPS data from the specified serial port.
    """
    try:
        with serial.Serial(config.GPS_PORT, config.BAUD_RATE, timeout=config.TIMEOUT) as ser:
            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if line:
                    msg = parse_nmea_sentence(line)
                    if msg:
                        lat, lon = extract_location_data(msg)
                        if lat and lon:
                            lat, lon = filter_gps_data(lat, lon)
                            yield lat, lon
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGPS data reading stopped by user.")
