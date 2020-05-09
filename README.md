# processwallpaper

Inspired by https://github.com/anirudhajith/process-wallpaper

Which is only for linux systems.

This works on windows as well.

Run this in background.

```py
# example.py
import time

from main import update_wallpaper

if __name__ == "__main__":
    while True:
        time.sleep(10)
        update_wallpaper()

```

