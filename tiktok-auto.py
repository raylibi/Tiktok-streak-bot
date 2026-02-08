from bot import tiktokbot
import sendmessage
import time
import sys
import io

def main():
    print("=== TIKTOK STREAK BOT ===")

    target_names, message = sendmessage.message()

    bot = tiktokbot(headless=False)

    try:
        bot.start()

        for friend_name in target_names:
            bot.send_streak(friend_name, message)

            time.sleep(1)

        print("\n all chat are sent")

    except Exception as e:
        print(f"an error occurred {e}")

    finally:
        print("closing browser...")
        bot.stop()

if __name__ == "__main__":
    main()