import vgamepad as vg
import keyboard as kb
import time

#log rumble inputs sent to the controller
log_rumble_values = False

#global state
executing = False
#prevent overlapping of multiple executions
lock = False

anti_afk_counter_reset = 5
anti_afk_counter = anti_afk_counter_reset

def rumble_callback(client, target, large_motor, small_motor, led_number, user_data):
    global lock, executing, anti_afk_counter, anti_afk_counter_reset
    
    if executing and log_rumble_values:
        print(f"time: {time.time()}, large motor: {large_motor}, small motor: {small_motor}")
    if 200 < large_motor < 255 and 220 < small_motor < 255  and not lock and executing:
        lock = True
        
        time.sleep(0.1)
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
            if anti_afk_counter == 0:
                print("JUMPING")
                anti_afk_counter = anti_afk_counter_reset
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                gamepad.update()
                time.sleep(0.5)
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                gamepad.update()
                time.sleep(2)
            else:
                anti_afk_counter -= 1
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

print("Commands:\n 9 -> start fishing routine\n 0 -> abort fishing routine\n\n")

def start(event):
    global executing, anti_afk_counter, anti_afk_counter_reset

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
    anti_afk_counter = anti_afk_counter_reset

def abort(event):
    global executing, lock

    gamepad.unregister_notification()
    print("Aborting...")
    lock = False
    executing = False
    
kb.on_press_key("9", start)
kb.on_press_key("0", abort)






