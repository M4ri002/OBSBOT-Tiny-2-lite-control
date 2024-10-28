# OBSBOT-Tiny-2-Lite-Control

Python script for controlling the OBSBOT Tiny 2 Lite. This script can retrieve and set camera states using OSC (Open Sound Control).

## OBSBOT Camera Control via OSC in Python

This project enables control of an OBSBOT camera via OSC messages using Python and the `python-osc` library. The script connects to and disconnects from the camera, requests device information, and retrieves gimbal position information.

## Requirements

1. **Python 3.6 or later**
2. **`python-osc` library**: Required for sending and receiving OSC messages.
3. **Activate OSC control in the OBSBOT Center application**: Make sure OSC control is enabled in OBSBOT Center.
4. **Configure IP and Port**: Set the same IP and port in both the OBSBOT Center application and this script to ensure correct communication. By default, the script uses `127.0.0.1` and port `16284`.
5. **Start OBSBOT Center**: Always launch the OBSBOT Center application before running this script to ensure it receives commands.

### Installation

Install the `python-osc` library via pip:

```bash
pip install python-osc
