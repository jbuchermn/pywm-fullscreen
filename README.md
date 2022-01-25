# pywm-fullscreen

This is a trivial implementation of a Wayland compositor using [pywm](https://github.com/jbuchermn/pywm) - it serves as its reference implementation and to profile / identify and fix performance issues (at the moment this is focused on an unnecessarily high idle cpu load).

`pywm-fullscreen`takes various command line options, most importantly `-e`(as in `-e firefox`), an application to run and display fullscreen. Check out [args.py](pywm_fullscreen/args.py) for all arguments. Install via `pip` or `nix flake`.
