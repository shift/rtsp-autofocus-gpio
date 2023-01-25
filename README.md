# Autofocus

This little project is designed to trigger a GPIO event on a RaspberryPi when the python script detects blurry imaves coming from the currently hardcoded RTSP stream.

I use this on an older Canon DSLR without eye-based video auto focus, connected via OBS used for video calls and recording.

## Hardware

 * Trigger cable for your camera plus jack plug, or cut the end off and solder ito a board/add dupoint/JST connector.
 * 2N2222 transistor
 * Optional 1K resistor, I chose not to use this and haven't noticed any issues, but listing it here as other peoples designs include it.

Pins:
 * GPIO26 (physical pin 37)
 * GND (physical pin 39)

```
                                      c________ Camera middle connector
                 1K (optional)       /
GPIO26 ---------/\/\/------------b--|   2N2222
                                     \
GND ----------------------------------e-------- Camera base connector
```
