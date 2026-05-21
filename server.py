import threading
import queue
import tkinter as tk
from flask import Flask, request
from flask_cors import CORS

# =====================================================================
# 1. FLASK SERVER SETUP (Background)
# =====================================================================
flask_app = Flask(__name__)
CORS(flask_app)

# A thread-safe queue to pass URLs from the server to the GUI
url_queue = queue.Queue()

@flask_app.route('/receive-url', methods=['POST'])
def receive_url():
    data = request.json
    url = data.get('url')
    if url:
        # Safely drop the URL into the queue for the GUI to grab
        url_queue.put(url) 
    return {"status": "success"}

def run_server():
    # CRITICAL: use_reloader=False stops Flask from starting your app twice
    flask_app.run(port=5000, use_reloader=False, debug=False)


# =====================================================================
# 2. GUI SETUP (Main Thread)
# =====================================================================
class TrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My URL Tracker Dashboard")
        self.root.geometry("500x350")

        # Header Label
        self.header = tk.Label(root, text="🌐 Live URL Tracker Running", font=("Arial", 14, "bold"))
        self.header.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(root, text="Waiting for history...", font=("Arial", 10, "italic"), fg="gray")
        self.status_label.pack(pady=5)

        # Listbox to display tracked URLs
        self.listbox = tk.Listbox(root, width=60, height=12, font=("Arial", 10))
        self.listbox.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)

        # Start the constant background check for new items in the queue
        self.check_for_new_urls()

    def check_for_new_urls(self):
        """Checks the queue for new URLs passed from the Flask server thread."""
        try:
            # Look at the queue without blocking the GUI
            while True:
                new_url = url_queue.get_nowait()
                
                # Add to GUI interface
                self.listbox.insert(0, new_url) # Inserts at the top
                self.status_label.config(text=f"Last tracked: {new_url[:50]}...", fg="green")
                
                url_queue.task_done()
        except queue.Empty:
            pass
        
        # Schedule this function to run again in 100 milliseconds
        self.root.after(100, self.check_for_new_urls)


# =====================================================================
# 3. RUN THE APP
# =====================================================================
if __name__ == '__main__':
    # Step A: Start Flask in a background "daemon" thread
    # (daemon=True means the server closes instantly when you close the GUI window)
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Step B: Start the GUI window on the main thread
    root = tk.Tk()
    app = TrackerApp(root)
    root.mainloop()