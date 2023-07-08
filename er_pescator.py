import vgamepad as vg
import keyboard as kb
import time

#global state
executing = False
#prevent overlapping of multiple executions
lock = False
#log rumble inputs sent to the controller
log_rumble_values = False

def rumble_callback(client, target, large_motor, small_motor, led_number, user_data):
    global lock, executing
    
    if executing and log_rumble_values:
        print(f"time: {time.time()}, large motor: {large_motor}, small motor: {small_motor}")
    if 200 < large_motor < 255 and 220 < small_motor < 255  and not lock and executing:
        lock = True
        
        print("PRESSING X")
        #fish up
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()
        time.sleep(0.5)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()
        #next throw
        time.sleep(4)
        if executing:
            print("FISHING")
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(1.5)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(5)
            print("WAITING...")

            lock = False


gamepad = vg.VX360Gamepad()

print("Commands:\n 1 -> start fishing routine\n 0 -> abort fishing routine\n\n")

def start(event):
    global executing

    gamepad.register_notification(callback_function=rumble_callback)
    #press a button to wake the device up
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    time.sleep(0.5)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    time.sleep(0.5)

    print("Starting with the first throw...")
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    time.sleep(1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    executing = True

def abort(event):
    global executing

    gamepad.unregister_notification()
    print("Aborting...")
    executing = False
    
kb.on_press_key("1", start)
kb.on_press_key("0", abort)







