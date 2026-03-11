from screenshot import capture_chart
from telegram_sender import send_photo
from config import CHART_URL


def main():

    print("Opening TradingView chart...")

    screenshot = capture_chart(CHART_URL)

    print("Sending to Telegram...")

    send_photo(screenshot)

    print("Done ✅")


if __name__ == "__main__":
    main()
