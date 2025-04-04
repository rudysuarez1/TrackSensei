import serial
import time

# Open serial port
gps_port = "/dev/ttyTHS1"  # Change this if needed
baud_rate = 115200  # Default for LC29H, change if necessary

#open serial connection
#ser = serial.Serial(gps_port, baud_rate, timeout=1)


def parse_gpgga(sentence):
    """Simple parser for $GPGGA sentence to extract latitude and longitude"""
    parts = sentence.split(',')
    if len(parts) >= 6:
        lat = parts[2]
        lon = parts[4]
        return lat, lon
    return None, None

try:
    with serial.Serial(gps_port, baud_rate, timeout=1) as ser, open("gps_data.txt", "w") as file:
        print("Reading GPS data... Press Ctrl+C to stop.")
        
        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if line:
                print(line)  # Display in terminal
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Add timestamp
                file.write(f"{timestamp} - {line}\n")  # Save with timestamp

                # Check if the line is a GPGGA sentence and parse
                if line.startswith("$GPGGA"):
                    lat, lon = parse_gpgga(line)
                    if lat and lon:
                        print(f"Latitude: {lat}, Longitude: {lon}")
except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nStopped by user.")

