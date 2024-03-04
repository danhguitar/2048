from pynput import keyboard

def dosomething(key):
    print(key)

with keyboard.Listener(on_release=dosomething) as Listener:
    Listener.join()