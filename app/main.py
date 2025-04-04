import time
import config
from gps_functions import read_gps_data

def main():
    gps_reader = read_gps_data()
    for lat, lon in gps_reader:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - Latitude: {lat}, Longitude: {lon}")

if __name__ == "__main__":
    main()

