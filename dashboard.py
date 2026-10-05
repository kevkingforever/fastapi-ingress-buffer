# dashboard.py
import tkinter as tk
from tkinter import ttk
import requests
import json
import threading

ROOT_WORKSPACE = r"C:\Users\HP\Desktop"

# SPECIFICATION CHECK: Pointed directly to your custom project endpoint to pull logs safely
TARGET_URL = "https://universal-sovereign-engine-delta.vercel.app/api/extract"

# PRODUCTION SECURITY BOUNDARY: Hardcoded private token stripped for public repository safety
SECURE_TOKEN = "YOUR_SECURE_API_KEY_HERE"

class DetachedSovereignBoardroom:
    def __init__(self, root):
        self.root = root
        self.root.title("REGISTRY-HUB: DEPLOYED CONSOLE DATA WINDOW")
        self.root.geometry("850x650")  # Amplified window height parameters
        self.root.configure(bg="#050505")
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(".", background="#050505", foreground="#aaaaaa", fieldbackground="#050505")
        
        # Main Header Title Banner
        header = tk.Label(root, text="REGISTRY-HUB // SYSTEM MONITOR\n[ ADMINISTRATIVE SUBSYSTEM WINDOW ]", 
                         bg="#050505", fg="#888888", font=("Courier New", 11, "bold"), pady=15)
        header.pack(fill=tk.X, side=tk.TOP)
        
        # ── SYSTEM MONITORING CANVASES ──────────────────────────────────────────
        monitor_frame = tk.Frame(root, bg="#050505", highlightbackground="#151515", highlightthickness=1)
        monitor_frame.pack(fill=tk.X, padx=20, pady=10, side=tk.TOP)
        
        self.clock_lbl = tk.Label(monitor_frame, text="CORE RUNTIME SPEED : BASELINE INVARIANT STANDING", bg="#050505", fg="#aaaaaa", font=("Courier New", 10))
        self.clock_lbl.pack(anchor=tk.W, padx=15, pady=6)
        
        self.valve_lbl = tk.Label(monitor_frame, text="STRATUM PERIMETER  : LAYER 50 CORE MATRIX ISOLATED", bg="#050505", fg="#00aaaa", font=("Courier New", 10))
        self.valve_lbl.pack(anchor=tk.W, padx=15, pady=6)

        # ── THE REVERSIBLE REGISTRY VIEW WINDOW ─────────────────────────────────
        lbl_history = tk.Label(root, text="[ CHRONO-VAULT DATA STREAM ]", bg="#050505", fg="#555555", font=("Courier New", 9, "bold"))
        lbl_history.pack(anchor=tk.W, padx=20, pady=(10, 2), side=tk.TOP)
        
        log_frame = tk.Frame(root, bg="#050505")
        log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5, side=tk.TOP)
        
        self.log_text = tk.Text(log_frame, bg="#080808", fg="#88ff88", insertbackground="white", 
                                font=("Courier New", 10), relief=tk.FLAT, bd=0, state=tk.DISABLED)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(log_frame, command=self.log_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        
        # ── FIXED BOTTOM CONTROL BAR ────────────────────────────────────────────
        btn_frame = tk.Frame(root, bg="#090909", padx=15, pady=10, bd=1, relief=tk.SUNKEN)
        btn_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # The Visible Refresh Action Trigger Button
        refresh_btn = tk.Button(btn_frame, text="REFRESH SYSTEM DATA LOGS", bg="#151515", fg="#00ff00", 
                                activebackground="#222222", activeforeground="#ffffff", relief=tk.RAISED, bd=1,
                                font=("Courier New", 9, "bold"), padx=12, pady=6, command=self.trigger_extraction)
        refresh_btn.pack(side=tk.LEFT)
        
        self.status_lbl = tk.Label(btn_frame, text="Console Interface Invariant", bg="#090909", fg="#666666", font=("Courier New", 9))
        self.status_lbl.pack(side=tk.RIGHT, pady=6)

    def append_log(self, content):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete("1.0", tk.END)
        self.log_text.insert(tk.END, content)
        self.log_text.config(state=tk.DISABLED)
        self.log_text.see(tk.END)

    def fetch_stream_worker(self):
        headers = {"x-signature-key": SECURE_TOKEN}
        try:
            response = requests.get(TARGET_URL, headers=headers, timeout=10)
            if response.status_code == 200:
                raw_data = response.json()
                self.append_log(json.dumps(raw_data, indent=2))
                
                if raw_data.get("stratum_51_horizon") and len(raw_data["stratum_51_horizon"]) > 0:
                    last_line = raw_data["stratum_51_horizon"][-1]
                    metrics = json.loads(last_line)
                    self.clock_lbl.config(text=f"CORE RUNTIME SPEED : {metrics.get('dt_delta')} ns DELTA TIMELINE")
                self.status_lbl.config(text="Live Vault Inversion Sync Complete", fg="#00ff00")
            else:
                self.status_lbl.config(text=f"Access Denied: HTTP {response.status_code}", fg="#ff0000")
        except Exception:
            self.status_lbl.config(text="Cloud memory loops idle.", fg="#ffaa00")

    def trigger_extraction(self):
        self.status_lbl.config(text="Querying live stratified layers...", fg="#ffaa00")
        threading.Thread(target=self.fetch_stream_worker, daemon=True).start()

if __name__ == "__main__":
    app_root = tk.Tk()
    app = DetachedSovereignBoardroom(app_root)
    app_root.mainloop()
