from __future__ import annotations
from typing import Any

import os
import logging
import time

from pywm import (
    PyWM,
    PyWMDownstreamState,
)

from .view import View
from .args import args

conf_pywm: dict[str, Any] = {
    'xkb_model': args.keyboard_model,
    'xkb_layout': args.keyboard_layout,
    'xkb_options': args.keyboard_options,

    'xcursor_theme': args.xcursor_theme,
    'xcursor_size': args.xcursor_size,

    'natural_scroll': not args.no_natural_scroll,

    'encourage_csd': False,
    'enable_xwayland': False,
    'texture_shaders': 'noeffect'
}
conf_outputs: list[dict[str, Any]] = []

logger = logging.getLogger(__name__)

class Compositor(PyWM[View]):
    def __init__(self) -> None:
        PyWM.__init__(self, View, **conf_pywm, outputs=conf_outputs, debug=True)

    def process(self) -> PyWMDownstreamState:
        return PyWMDownstreamState()

    def main(self) -> None:
        logger.debug("Compositor main...")
        self.update_cursor()
        os.system("%s &" % args.execute)

        time.sleep(2.)

        if len(self._views) == 0:
            self.terminate()

    def destroy_view(self, view: View) -> None:
        logger.info("Destroying view %s", view)
        if len([v for v in self._views.values() if v._handle != view._handle]) == 0:
            self.terminate()
