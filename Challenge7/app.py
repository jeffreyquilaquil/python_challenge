import datetime, time, sys, wave, struct, os

try:
    from playsound import playsound
except ImportError:
    playsound = None

def generate_beep(filename="beep.wav"):
    if os.path.exists(filename):
        return
    
    # Simple beep: 1000Hz for 1 second
    sample_rate = 44100
    duration = 1.0
    frequency = 1000.0
    
    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        for i in range(int(sample_rate * duration)):
            value = int(32767.0 * 0.5 * (1.0 if (i // (sample_rate // frequency // 2)) % 2 == 0 else -1.0))
            data = struct.pack('<h', value)
            f.writeframesraw(data)


def alarm_clock():
    
    while True:
        now = datetime.datetime.now()
        print(f"Current time: {now.strftime('%H:%M:%S')}")
        user_input = input("Please enter a valid time to set an alarm example (6:30): ")
        try:
            alarm_time = [int(n) for n in user_input.split(":")]
            if not (0 <= alarm_time[0] < 24 and 0 <= alarm_time[1] < 60):
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid time format.")
            continue

    now = datetime.datetime.now()
    current_time_in_seconds = (now.hour * 3600) + (now.minute * 60) + now.second
    alarm_time_in_seconds = (alarm_time[0] * 3600) + (alarm_time[1] * 60)

    # Calculate seconds until the alarm triggers
    seconds_to_wait = alarm_time_in_seconds - current_time_in_seconds

    # If the time has already passed today, set it for tomorrow
    if seconds_to_wait <= 0:
        seconds_to_wait += 24 * 3600

    print(f"Alarm set. It will go off in {datetime.timedelta(seconds=seconds_to_wait)}.")

    try:
        while seconds_to_wait > 0:
            timer = datetime.timedelta(seconds=seconds_to_wait)
            print(f"Time remaining: {timer}", end="\r")
            time.sleep(1)
            seconds_to_wait -= 1
    except KeyboardInterrupt:
        print("\nAlarm Cancelled")
        sys.exit(0)

    print("\nRing Ring... Time to wake up!")

    if playsound:
        generate_beep()
        try:
            playsound("beep.wav")
        except Exception as e:
            print(f"(Audio alert failed: {e})")
    else:
        print("(Audio alert skipped: playsound module not installed)")


if __name__ == "__main__":
    alarm_clock()