STAY - Keep your Mac awake only when your iPhone is connected to Wi-Fi
======================================================================

OVERVIEW
--------
Stay is a simple command-line tool for macOS that keeps your Mac awake 
while your iPhone is connected to the same Wi-Fi network. When your 
iPhone disconnects, your Mac automatically goes to sleep. This helps 
save battery and adds an extra layer of security.

DEMO VIDEO
----------
Watch the demonstration video showing how Stay works here: <br>

[![Watch the demo video](thumbnail.png)](https://github.com/thisisanimesh01/stay/blob/main/demo.mp4)


FEATURES
--------
- Monitors iPhone Wi-Fi connection in real time
- Keeps Mac awake while connected
- Automatically puts Mac to sleep when iPhone disconnects
- Sends macOS notifications for connection updates
- Can be run manually or set to start automatically

REQUIREMENTS
------------
- macOS (Monterey or newer recommended)
- Python 3 installed
- iPhone and Mac connected to the same Wi-Fi network

SETUP INSTRUCTIONS
------------------
1. Save the script file "stay.py" in any folder. 
   Example: ~/Desktop/me/stay.py

2. Make the script executable:
   chmod +x ~/Desktop/me/stay.py

3. Create a global shortcut command (symbolic link):
   sudo ln -s /Users/<your_username>/Desktop/me/stay.py /usr/local/bin/stay
   (Replace <your_username> with your actual Mac username)

4. Make sure the script starts with this line:
   #!/usr/bin/env python3

5. Run the script:
   stay

   You should see the message:
   Stay mode activated (Wi-Fi monitoring enabled).

   The script will monitor your iPhone connection continuously.
   When the iPhone disconnects, your Mac will automatically go to sleep.

STOPPING THE SCRIPT
-------------------
To stop monitoring, press:
   Ctrl + C

RUNNING IN BACKGROUND (OPTIONAL)
--------------------------------
If you want to run the script without keeping the terminal open:
   nohup stay &

AUTOMATIC STARTUP (OPTIONAL)
----------------------------
To make the script start automatically when you log in:
1. Open System Settings -> General -> Login Items
2. Click the + icon
3. Add the stay.py script from its folder

IPHONE IP SETUP
---------------
The script requires your iPhone's local IP address to detect connection.
To find it:
1. On iPhone, open Settings -> Wi-Fi
2. Tap the (i) icon next to your connected Wi-Fi
3. Note down the IP Address
4. Update the IPHONE_IP variable in stay.py with that address

   Example:
   IPHONE_IP = "use your iphone_ip_wifi"

AUTHOR
------
Developed by: Animesh Yadav
Purpose: A simple and smart Mac automation utility

LICENSE
-------
MIT License (c) 2025 Animesh Yadav
