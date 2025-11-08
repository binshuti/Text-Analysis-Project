import urllib.request

def fetch_text(url: str) -> str:
    """
    Downloads plain text from the given URL and returns it decoded as UTF-8.
    Raises an exception with a clear message if something goes wrong.
    """
    try:
        with urllib.request.urlopen(url) as resp:
            raw = resp.read().decode("utf-8", errors="ignore")
        return raw
    except Exception as e:
        raise RuntimeError(f"Failed to fetch URL {url}: {e}")
