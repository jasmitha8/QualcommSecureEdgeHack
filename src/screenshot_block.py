#!/usr/bin/env python3
"""
Simple Screenshot Blocker - Demo Version
Shows fullscreen popup when Win+Shift+S is detected
"""

import tkinter as tk
from tkinter import ttk
import keyboard
import threading
import time
import sys

class SimpleScreenshotBlocker:
    def __init__(self):
        print("🛡️  Simple Screenshot Blocker - Demo Version")
        print("🚀 Blocks Win+Shift+S with fullscreen popup!")
        print("=" * 50)
        
        self.monitoring = False
        self.blocked_count = 0
        self.popup_window = None
        
        # Setup main window (hidden)
        self.root = tk.Tk()
        self.root.withdraw()  # Hide main window
        
        print("✅ Simple blocker ready!")

    def create_blocking_popup(self):
        """Create fullscreen blocking popup"""
        if self.popup_window:
            return  # Already showing
        
        # Create popup window
        self.popup_window = tk.Toplevel(self.root)
        self.popup_window.title("Screenshot Blocked")
        
        # Make it fullscreen and topmost
        self.popup_window.attributes('-fullscreen', True)
        self.popup_window.attributes('-topmost', True)
        self.popup_window.configure(bg='#1a1a2e')
        
        # Create content frame
        content_frame = tk.Frame(self.popup_window, bg='#1a1a2e')
        content_frame.pack(expand=True, fill='both')
        
        # Main blocking message
        title_label = tk.Label(
            content_frame, 
            text="🛡️ SCREENSHOT BLOCKED",
            font=('Arial', 48, 'bold'),
            fg='#ff6b6b',
            bg='#1a1a2e'
        )
        title_label.pack(pady=(200, 20))
        
        # Subtitle
        subtitle_label = tk.Label(
            content_frame,
            text="AI Protection Active - Sensitive Content Detected",
            font=('Arial', 24),
            fg='#4ecdc4',
            bg='#1a1a2e'
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Info text
        info_text = f"""
This screenshot attempt has been blocked because:
• Protected application detected (VS Code)
• Potentially sensitive content visible
• AI security system active

Blocked Screenshots: {self.blocked_count}
Time: {time.strftime('%H:%M:%S')}
        """
        
        info_label = tk.Label(
            content_frame,
            text=info_text,
            font=('Arial', 16),
            fg='#ffffff',
            bg='#1a1a2e',
            justify='center'
        )
        info_label.pack(pady=(0, 50))
        
        # Close button
        close_button = tk.Button(
            content_frame,
            text="Click here or press ESC to close",
            font=('Arial', 18, 'bold'),
            bg='#ff6b6b',
            fg='white',
            relief='flat',
            padx=30,
            pady=15,
            command=self.close_popup
        )
        close_button.pack()
        
        # Bind escape key to close
        self.popup_window.bind('<Escape>', lambda e: self.close_popup())
        self.popup_window.bind('<Button-1>', lambda e: self.close_popup())
        
        # Focus the window
        self.popup_window.focus_force()
        self.popup_window.grab_set()
        
        print(f"🚫 FULLSCREEN POPUP SHOWN - Screenshot blocked!")

    def close_popup(self):
        """Close the blocking popup"""
        if self.popup_window:
            self.popup_window.grab_release()
            self.popup_window.destroy()
            self.popup_window = None
            print("✅ Popup closed")

    def on_screenshot_detected(self):
        """Called when Win+Shift+S is detected"""
        self.blocked_count += 1
        print(f"\n📸 Win+Shift+S detected! Blocking attempt #{self.blocked_count}")
        
        # Show popup in main thread
        self.root.after(0, self.create_blocking_popup)

    def setup_hotkey_detection(self):
        """Setup hotkey detection"""
        try:
            # Register Win+Shift+S hotkey
            keyboard.add_hotkey('win+shift+s', self.on_screenshot_detected, suppress=True)
            print("✅ Win+Shift+S hotkey registered with suppression")
            
            # Also catch other screenshot combinations for demo
            keyboard.add_hotkey('print screen', self.on_screenshot_detected, suppress=True)
            keyboard.add_hotkey('alt+print screen', self.on_screenshot_detected, suppress=True)
            
            return True
        except Exception as e:
            print(f"❌ Hotkey setup failed: {e}")
            return False

    def start_monitoring(self):
        """Start the blocker"""
        if self.monitoring:
            return
        
        print("\n🚀 Starting simple screenshot blocker...")
        print("📸 Try Win+Shift+S to see the blocking popup!")
        print("🛑 Close this window to stop\n")
        
        if not self.setup_hotkey_detection():
            print("❌ Failed to setup hotkey detection!")
            return False
        
        self.monitoring = True
        
        # Add close button to console info
        def show_control_window():
            control = tk.Toplevel(self.root)
            control.title("Screenshot Blocker Control")
            control.geometry("400x200")
            control.attributes('-topmost', True)
            
            tk.Label(control, text="🛡️ Screenshot Blocker Active", 
                    font=('Arial', 16, 'bold')).pack(pady=20)
            
            status_label = tk.Label(control, text=f"Blocked: {self.blocked_count}", 
                                  font=('Arial', 12))
            status_label.pack(pady=10)
            
            def update_status():
                status_label.config(text=f"Blocked: {self.blocked_count}")
                control.after(1000, update_status)
            update_status()
            
            tk.Label(control, text="Try Win+Shift+S to test blocking!", 
                    font=('Arial', 10)).pack(pady=5)
            
            tk.Button(control, text="Stop Blocker", command=self.stop_monitoring,
                     bg='#ff6b6b', fg='white', font=('Arial', 12, 'bold')).pack(pady=20)
        
        # Show control window after short delay
        self.root.after(1000, show_control_window)
        
        return True

    def stop_monitoring(self):
        """Stop the blocker"""
        self.monitoring = False
        
        try:
            keyboard.unhook_all_hotkeys()
            keyboard.unhook_all()
        except:
            pass
        
        if self.popup_window:
            self.close_popup()
        
        print(f"\n🛑 Screenshot blocker stopped")
        print(f"📊 Total blocked: {self.blocked_count}")
        
        # Close application
        self.root.quit()

    def run(self):
        """Run the blocker"""
        try:
            if self.start_monitoring():
                # Run tkinter main loop
                self.root.mainloop()
        except KeyboardInterrupt:
            print("\n🛑 Stopping...")
            self.stop_monitoring()
        except Exception as e:
            print(f"❌ Error: {e}")
            self.stop_monitoring()

def main():
    """Main function"""
    print("🎯 Simple Screenshot Blocker - Demo Version")
    print("🔐 Shows fullscreen popup to block Win+Shift+S")
    print("=" * 50)
    
    try:
        blocker = SimpleScreenshotBlocker()
        blocker.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")

if __name__ == "__main__":
    main()