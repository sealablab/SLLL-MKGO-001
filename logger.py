#!/usr/bin/env python3
#
# moku example: Basic Datalogger
#
# This example demonstrates use of the Datalogger instrument to log time-series
# voltage data to a (Binary or CSV) file.
#
# (c) 2021 Liquid Instruments Pty. Ltd.
#
import os
import time

from moku.instruments import Datalogger

# Connect to your Moku by its ip address using Datalogger('192.168.###.###')
# or by its serial number using Datalogger(serial=123)
i = Datalogger('192.168.127.44', force_connect=True)

try:
    # Configure the frontend
    i.set_frontend(channel=1, impedance='1MOhm', coupling="AC", range="10Vpp")
    # Log 100 samples per second
    i.set_samplerate(100)

    i.set_acquisition_mode(mode='Precision')

    # Generate Sine wave on Output1
    i.generate_waveform(channel=1, type='Sine', amplitude=1,
                        frequency=10e3)
    
    # Stop an existing log, if any, then start a new one. 10 seconds of both
    # channels
    logFile = i.start_logging(duration=2)

    # Track progress percentage of the data logging session
    logging_complete = False
    while not logging_complete:
        # Get current progress percentage and print it out
        progress = i.logging_progress()
        print(f"{progress}")
        logging_complete = progress['complete']
        # Wait for the logging session to progress by sleeping 0.5sec
        time.sleep(0.5)

    print("#TODO Download the log file to local directory")
    # Download log from Moku, use liconverter to convert this .li file to .csv
    i.download("persist", logFile['file_name'], os.path.join(os.getcwd(), logFile['file_name']))
    print("Downloaded log file to local directory.")

except Exception as e:
    print(f'Exception occurred: {e}')
finally:
    # Close the connection to the Moku device
    # This ensures network resources and released correctly
    i.relinquish_ownership()

