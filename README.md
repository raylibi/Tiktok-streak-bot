# Tiktok Streak Bot

## How to use:
1. Install the required libraries:  
a. pip install playwright  
b. playwright install chromium
2. Open the sendmessage.py file and fill in target_name with your friend’s display name.
    How to get the display name:  
    a. Directly:
    - Open Messages on TikTok and check the name displayed there. 
    
    b. Inspect element (untuk lebih akurat):
    - Open the Messages menu on TikTok Web.
    - Open Inspect Element, then select Select element in the page (Ctrl + Shift + C).
    - Hover over and select your friend’s name.
    - Copy your friend’s name from the selected <p> tag.
    - Paste that name into target_name.
3. Run python auth.py in the terminal.
4. A browser will open. Log in manually to your TikTok account (via QR Code, Email, or Phone Number). If a captcha fails to load, refresh the page and repeat the login process, or use the QR code method to avoid captcha.
5. After successfully logging in and the FYP page opens, press Enter.
6. The bot will automatically create a session.json file in the project folder. This file contains your login cookies.
7. Run the bot using python tiktok-auto.py in the terminal. The bot will send messages to each of your friends so the streak doesn’t break (remind your friends to reply so the streak stays active).
