from __future__ import annotations

import logging
import time
import sys

try:
    import yappi  # type: ignore
    YAPPI = True
except:
    YAPPI = False

from .compositor import Compositor
from .args import args

logger = logging.getLogger(__name__)

def run() -> None:
    print("pywm-fullscreen (python) - args are %s" % str(sys.argv), flush=True)


    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(filename)s:%(lineno)s %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    for l in ["pywm_fullscreen"]:
        log = logging.getLogger(l)
        log.setLevel(logging.DEBUG)
        log.addHandler(handler)

    wm = Compositor()

    try:
        if YAPPI and args.profile:
            yappi.start()
        wm.run()
    except Exception:
        logger.exception("Unexpected")
    finally:
        wm.terminate()

        if YAPPI and args.profile:
            time.sleep(2.)
            yappi.stop()
            for thread in yappi.get_thread_stats():
                print("----------- THREAD (%s) (%d) ----------------" % (thread.name, thread.id))
                stats = yappi.get_func_stats(ctx_id=thread.id)
                for s in stats:
                    where = "%s.%s:%d" % (s.module, s.name, s.lineno)
                    if len(where) > 100:
                        where = where[-100:]

                    print("%0100s %5d * %.10f = %.10f (%.10f)" % (where, s.ncall, s.tavg, s.ttot, s.tsub))

                stats.save("/tmp/yappistats_%d" % thread.id, type="pstat")
