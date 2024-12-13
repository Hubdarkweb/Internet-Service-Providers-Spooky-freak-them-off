import random
import webbrowser
import time
import threading

def load_links(file_path):
    """Load URLs from a file."""
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
        return [link.strip() for link in links if link.strip()]
    except FileNotFoundError:
        print("Error: Spooky.txt file not found.")
        return []

def random_open(links, delay=5):
    """Open random links at regular intervals."""
    if not links:
        print("No links found. Check your Spooky.txt file.")
        return
    while True:
        link = random.choice(links)
        print(f"Freaking them out by opening: {link}")
        webbrowser.open(link)
        time.sleep(random.randint(1, delay))

def multi_thread_open(links, num_threads=3, delay=5):
    """Use multiple threads to open links for maximum misdirection."""
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=random_open, args=(links, delay))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    spooky_file = "Spooky.txt"
    links_list = load_links(spooky_file)
    print("Launching ISP SPOOKY FREAK THEM OFF... hold on!")
    multi_thread_open(links_list, num_threads=5, delay=3)
