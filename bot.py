import os
import time
import re
from playwright.sync_api import sync_playwright, Page, Browser, Playwright

class tiktokbot:
    def __init__(self, session_path: str = "session.json", headless: bool = True):
        self.session_path = session_path
        self.headless = headless
        self.playwright: Playwright = None
        self.browser: Browser = None
        self.page: Page = None
        self.context: context = None

    def start(self):
        #starting playwright
        if not os.path.exists(self.session_path):
            raise FileNotFoundError(f"file {self.session_path} not found")
        
        print("memulai playwright")
        self.playwright = sync_playwright().start()

        #launch browser
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(storage_state=self.session_path)
        self.page = self.context.new_page()

        #open tiktok
        url = f"https://www.tiktok.com"

        self.page.goto(url, timeout=30000, wait_until="domcontentloaded")

        messages_button = self.page.locator("button[aria-label='Messages']")
        messages_button.wait_for(state="visible", timeout=30000)
        messages_button.click()
        time.sleep(2)

    def send_streak(self, displayname: str, message: str):
        if not self.page:
            print("Browser is not started yet")
            return           
        
        try:            
            #in inbox menu
            chat_items = self.page.locator("div[data-e2e='chat-list-item']")
            chat_items.first.wait_for(state="visible", timeout=30000)
            exact_name = re.compile(rf"^{re.escape(displayname)}$", re.IGNORECASE)
            target_chat = chat_items.filter(has=self.page.locator("p", has_text=exact_name)).first
            safename = displayname.encode('ascii', 'ignore').decode('ascii')

            try:
                target_chat.wait_for(state="visible", timeout=5000)
                print(f"chat {safename} found")
                target_chat.click()

            except Exception:
                print(f"failed to find {safename}")
                return
            
            #write a message
            chat_box = self.page.locator("div[contenteditable='true'][role='textbox']")
            chat_box.wait_for(state="visible", timeout=10000)

            chat_box.click()
            time.sleep(0.5)
            chat_box.fill(message)
            print("writing message...")

            send_btn = self.page.locator("[data-e2e='message-send']")
            if send_btn.is_visible():
                send_btn.click()
                print("message sent")
            else:
                self.page.keyboard.press("Enter")
                print("sent via enter")


        except Exception as e:
            print(f"error: {e}")

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

        
