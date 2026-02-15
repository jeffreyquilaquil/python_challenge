from plyer import notification
import time

def system_alert():
    print("Attempting to send notification...")
    try:
        notification.notify(
            title = 'Alert',
            message = 'Message Alert!',
            timeout = 2
        )
        print("Notification sent successfully!")
    except Exception as e:
        print(f"Failed to send notification: {e}")

    time.sleep(7)

if __name__ == "__main__":
    system_alert()