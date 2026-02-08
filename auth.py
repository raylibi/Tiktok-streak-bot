import os
from playwright.sync_api import sync_playwright

session_file = "session.json"

def first_login():
    print("Tiktok First Authentication")

    #check older authentication if exist
    if os.path.exists(session_file):
        print(f"session file {session_file} is already exist\n new login will affect the older session")
    
    with sync_playwright() as p:

        args = [
            "--disable-blink-features=AutomationControlled", 
            "--no-sandbox",
            "--disable-infobars",
        ]

        print("open browser")
        browser = p.chromium.launch(headless=False, args=args, ignore_default_args=["--enable-automation"])
        context = browser.new_context(
            viewport=None
        )
        page = context.new_page()

        #tiktok login
        try:
            page.goto("https://www.tiktok.com")
        except Exception as e:
            print(f"error: {e}")

        print("INSTRUCTION")
        print("Please login manually to your tiktok")
        print("Reload the page if the captcha is exist")
        print("Use QR Code login to avoid captcha")
        print("Wait until you're in")
        print("Dont close your browser")
        print("Go back here and press enter")

        input("Press enter if the login is success")

        print("saving session...")
        try:
            context.storage_state(path=session_file)
            print(f"session {session_file} is saved")
            print("now you can run tiktok-auto.py")
        except Exception as e:
            print(f"error: {e}")
            browser.close()

if __name__ == "__main__":
    first_login()