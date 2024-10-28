import sys
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.udp_client import OscMessage

ip = "127.0.0.1"
port = 16284

address_general = "/OBSBOT/WebCam/General/"
address_tiny = "/OBSBOT/WebCam/Tiny/"
address_tail = "/OBSBOT/Camera/TailAir/"
address_meet = "/OBSBOT/WebCam/Meet/"

# Create client
client = SimpleUDPClient(ip, port)


def get_response(timeout=1):
    for response in client.get_messages(timeout):
        print("response: ", response)
        print("response address: ", response.address)
        for arg in response.params:
            print("arg: ", arg)


if __name__ == "__main__":
    # Connect server
    client.send_message(address_general + "Connected", 1)
    get_response(1)

    client.send_message(address_general + "GetDeviceInfo", 1)
    get_response(1)

    client.send_message(address_general + "GetGimbalPosInfo", 1)
    get_response(1)

    # Disconnect
    client.send_message(address_general + "Disconnected", 1)
    print("Send Disconnect")
