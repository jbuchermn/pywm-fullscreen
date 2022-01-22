from __future__ import annotations

import logging

from .compositor import Compositor

logger = logging.getLogger(__name__)

def run(execute: str) -> None:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(filename)s:%(lineno)s %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    for l in ["pywm_fullscreen"]:
        log = logging.getLogger(l)
        log.setLevel(logging.DEBUG)
        log.addHandler(handler)

    wm = Compositor(execute=execute)

    try:
        wm.run()
    except Exception:
        logger.exception("Unexpected")
    finally:
        wm.terminate()
