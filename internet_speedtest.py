import speedtest
import threading
import itertools
import time
import sys


def spinner(task_name, stop_event):
    for c in itertools.cycle("|/-\\"):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\r{task_name}... {c}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 50 + "\r")


def run_with_spinner(task_name, func):
    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(task_name, stop_event))
    t.start()
    try:
        result = func()
    finally:
        stop_event.set()
        t.join()
    return result


def speed_test():
    print("=" * 45)
    print(" Internet Speed Test")
    print("=" * 45)

    try:
        st = speedtest.Speedtest(secure=True)
        run_with_spinner("Finding best server", st.get_best_server)

        down_speed = run_with_spinner("Testing download speed", st.download)
        down_speed = round(down_speed / 10**6, 2)

        up_speed = run_with_spinner("Testing upload speed", st.upload)
        up_speed = round(up_speed / 10**6, 2)

        ping = round(st.results.ping, 2)

        print("\nTest completed successfully!\n")
        print(f"Download Speed : {down_speed} Mbps")
        print(f"Upload Speed   : {up_speed} Mbps")
        print(f"Ping           : {ping} ms")

    except Exception as e:
        print(f"\nError during speed test: {e}")


if __name__ == "__main__":
    speed_test()
    input("\nPress Enter to exit...")
