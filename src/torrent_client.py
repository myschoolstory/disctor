import libtorrent as lt
import time
import os

def download_torrent(torrent_url):
    """Download a torrent from the given URL."""
    try:
        ses = lt.session()
        ses.listen_on(6881, 6891)

        params = {
            'save_path': './downloads/',
            'storage_mode': lt.storage_mode_t.storage_mode_sparse,
            'url': torrent_url
        }

        handle = lt.add_magnet_uri(ses, torrent_url, params)
        print(f"Downloading: {torrent_url}")

        while not handle.has_metadata():
            time.sleep(1)

        print("Metadata acquired, starting download...")
        while handle.status().state != lt.torrent_status.seeding:
            s = handle.status()
            print(f"Download rate: {s.download_rate / 1000} kB/s, Progress: {s.progress * 100:.2f}%")
            time.sleep(1)

        return f"Download completed: {handle.name()}"
    except Exception as e:
        return f"Error downloading torrent: {e}"

def upload_torrent(file_path):
    """Upload a torrent from the given file path."""
    try:
        if not os.path.exists(file_path):
            return "File does not exist."

        # Assuming the file is a .torrent file
        ses = lt.session()
        info = lt.torrent_info(file_path)
        handle = ses.add_torrent({'ti': info, 'save_path': './uploads/'})
        print(f"Uploading: {file_path}")

        while not handle.is_seed():
            s = handle.status()
            print(f"Upload rate: {s.upload_rate / 1000} kB/s, Progress: {s.progress * 100:.2f}%")
            time.sleep(1)

        return f"Upload completed: {handle.name()}"
    except Exception as e:
        return f"Error uploading torrent: {e}"

def seed_torrent(torrent_url):
    """Seed a torrent from the given URL."""
    try:
        ses = lt.session()
        ses.listen_on(6881, 6891)

        params = {
            'save_path': './seeds/',
            'storage_mode': lt.storage_mode_t.storage_mode_sparse,
            'url': torrent_url
        }

        handle = lt.add_magnet_uri(ses, torrent_url, params)
        print(f"Seeding: {torrent_url}")

        while not handle.has_metadata():
            time.sleep(1)

        print("Metadata acquired, starting seeding...")
        while handle.status().state != lt.torrent_status.seeding:
            s = handle.status()
            print(f"Seeding rate: {s.upload_rate / 1000} kB/s, Progress: {s.progress * 100:.2f}%")
            time.sleep(1)

        return f"Seeding started: {handle.name()}"
    except Exception as e:
        return f"Error seeding torrent: {e}"
