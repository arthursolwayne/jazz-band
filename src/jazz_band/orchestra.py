"""
Orchestra Configuration - MIDI mappings for 5-part jazz ensemble.
"""

# MIDI programs (0-indexed)
PROGRAMS = {
    "bass": 33,   # Electric Bass
    "piano": 0,   # Acoustic Grand
    "sax": 66,    # Tenor Sax
}

# MIDI channels (0-indexed, drums on 9)
CHANNELS = {
    "bass": 0,
    "piano": 1,
    "sax": 2,
    "drums": 9,
}

# Drum pitches (GM percussion)
DRUMS = {
    "kick": 36,
    "snare": 38,
    "hihat": 42,
}

# Pitch ranges
RANGES = {
    "bass": (28, 55),   # E1 to G3
    "piano": (21, 108), # A0 to C8
    "sax": (44, 76),    # Ab2 to E5
}
