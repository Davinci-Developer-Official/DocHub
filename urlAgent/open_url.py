import webbrowser
import time

urls = [
    "https://github.com",
    "https://stackoverflow.com",
    "https://pypi.org"
]

def open_browser():
    for url in urls:
        webbrowser.open_new_tab(url)
        time.sleep(1)  # Wait 1 second between opening tabs
