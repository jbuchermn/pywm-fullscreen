from __future__ import annotations
from typing import Any

import os
import logging

from pywm import (
    PyWM,
    PyWMDownstreamState,
)

from .view import View

conf_pywm: dict[str, Any] = {}
conf_outputs: list[dict[str, Any]] = []

logger = logging.getLogger(__name__)

class Compositor(PyWM[View]):
    def __init__(self, execute: str) -> None:
        PyWM.__init__(self, View, **conf_pywm, outputs=conf_outputs, debug=True)
        self._execute = execute

    def process(self) -> PyWMDownstreamState:
        return PyWMDownstreamState()

    def main(self) -> None:
        logger.debug("Compositor main...")
        os.system("%s &" % self._execute)

    def destroy_view(self, view: View) -> None:
        logger.info("Destroying view %s", view)
        if len([v for v in self._views.values() if v._handle != view._handle]) == 0:
            self.terminate()
