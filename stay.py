#cli based script to keep mac awake when iphone is connected to same wifi network
import os
import subprocess  #to run system commands
import time
import signal
import sys  #to handle exit signals


iphone_ip_wifi = "192.168.1.78"  #iphone's local ip address

def notify(title: str, message: str) -> None:  
    """Send a macOS notification."""
    subprocess.run([
        "osascript",
        "-e",
        f'display notification "{message}" with title "{title}"' 
    ])

def ping_device(ip: str) -> bool:        
    """Check if a device is reachable via ping."""
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1000", ip],     
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0     
    except Exception:
        return False

def sleep_mac() -> None:       
    """Put the Mac to sleep."""
    os.system("pmset sleepnow")   #command to put mac to sleep

def signal_handler(sig, frame):   
    """Handle Ctrl+C to exit gracefully."""
    print("\nStay mode stopped manually.")
    notify("Stay", "Monitoring stopped.")
    sys.exit(0)         #exit the script

def main():   
    print("Stay mode activated (Wi-Fi monitoring enabled).") #message to show when script starts
    notify("Stay", "Monitoring iPhone Wi-Fi connection...") #notification when script starts

    signal.signal(signal.SIGINT, signal_handler)
    connected_once = False

    while True:
        connected = ping_device(iphone_ip_wifi )     #to heck if iphone is connected to same wifi as mac

        if connected and not connected_once: 
            print("iPhone connected to same Wi-Fi. Monitoring...")     #message to show when iphone connects mac
            notify("Stay", "iPhone connected. Monitoring started.")     #notification when iphone connects mac
            connected_once = True

        elif connected_once and not connected:
            print("iPhone disconnected. Putting Mac to sleep...")      #message to show when iphone disconnects from mac
            notify("Stay", "iPhone disconnected. Mac will sleep.")   #notification when iphone disconnects from amac
            time.sleep(2)  #short delay before sleeping the mac
            sleep_mac()
            break

        time.sleep(5)

if __name__ == "__main__":
    main()
