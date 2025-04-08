import time
from collections import deque
from typing import Deque, Generator, Optional, Tuple

import pynmea2
import serial

from . import config

# Type alias for GPS coordinates
GPSCoord = Tuple[float, float]

# Initialize a deque to store the last N GPS readings for filtering
gps_buffer: Deque[GPSCoord] = deque(maxlen=10)


def parse_nmea_sentence(sentence: str) -> Optional[pynmea2.nmea.NMEASentence]:
    """
    Parse a single NMEA sentence and return a pynmea2 message object.
    """
    try:
        return pynmea2.parse(sentence)
    except pynmea2.nmea.ParseError:
        return None


def extract_location_data(
    msg: pynmea2.nmea.NMEASentence,
) -> Tuple[Optional[float], Optional[float]]:
    """
    Extract latitude and longitude from a pynmea2 message object.
    """
    if isinstance(msg, pynmea2.types.talker.GGA):
        lat = msg.latitude
        lon = msg.longitude
        return lat, lon
    return None, None


def filter_gps_data(lat: float, lon: float) -> Tuple[float, float]:
    """
    Apply a simple moving average filter to GPS data to reduce noise.
    """
    gps_buffer.append((lat, lon))
    if len(gps_buffer) == gps_buffer.maxlen:
        avg_lat = sum(lat for lat, _ in gps_buffer) / len(gps_buffer)
        avg_lon = sum(lon for _, lon in gps_buffer) / len(gps_buffer)
        return avg_lat, avg_lon
    return lat, lon


def read_gps_data() -> Generator[Tuple[float, float], None, None]:
    """
    Continuously read GPS data from the specified serial port.
    """
    try:
        with serial.Serial(
            config.GPS_PORT, config.BAUD_RATE, timeout=config.TIMEOUT
        ) as ser:
            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if line:
                    msg = parse_nmea_sentence(line)
                    if msg:
                        lat, lon = extract_location_data(msg)
                        if lat is not None and lon is not None:
                            filtered_lat, filtered_lon = filter_gps_data(lat, lon)
                            yield filtered_lat, filtered_lon
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGPS data reading stopped by user.")
