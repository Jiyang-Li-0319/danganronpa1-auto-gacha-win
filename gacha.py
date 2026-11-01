import time
import threading
import pydirectinput
from pynput import keyboard
from pynput.keyboard import Key

# ================= 配置区 =================
COIN_KEY = 's'
CONFIRM_KEY = 'enter'
WAIT_AFTER_COIN = 1.0
WAIT_AFTER_CONFIRM = 7.5
TOGGLE_KEY = Key.f9
# =========================================

is_running = False
remaining = 0          # 剩余要投的币数
lock = threading.Lock()

def gacha_loop(total):
    global is_running, remaining
    print(f"[START] Will pull {total} times. Press F9 to stop early.")
    while is_running and remaining > 0:
        with lock:
            pydirectinput.press(COIN_KEY)
        print(f"[ACTION] S  (remaining: {remaining - 1})")
        time.sleep(WAIT_AFTER_COIN)

        if not is_running:
            break

        with lock:
            pydirectinput.press(CONFIRM_KEY)
        print("[ACTION] Enter")
        time.sleep(WAIT_AFTER_CONFIRM)

        with lock:
            remaining -= 1

    # 投完了（或手动停止）
    if remaining == 0 and is_running:
        print("[DONE] All coins used. Auto-stopping.")
        is_running = False
    print("[STOP] Loop ended.")

def on_press(key):
    global is_running
    try:
        if key == TOGGLE_KEY:
            if not is_running and remaining > 0:
                is_running = True
                t = threading.Thread(target=gacha_loop, args=(remaining,), daemon=True)
                t.start()
            elif is_running:
                is_running = False
                print("[PAUSE] Auto gacha stopped.")
    except AttributeError:
        pass

if __name__ == "__main__":
    print("Script ready.")
    while True:
        try:
            raw = input("How many coins to use? (e.g. 10): ").strip()
            n = int(raw)
            if n > 0:
                remaining = n
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Will pull {remaining} times. Enter gacha screen, press F9 to start.")
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        print("ERROR:", repr(e))
        import traceback
        traceback.print_exc()