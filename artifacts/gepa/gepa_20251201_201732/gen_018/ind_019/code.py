
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument
import os

# Configuration
BPM = 160
TEMPO = 60.0 / BPM  # seconds per beat
TIME_SIGNATURE = (4, 4)
KEY = 'Dm'  # D minor
OUTPUT_FILE = "dante_russo_intro.mid"

# Calculate durations
BEAT_DURATION = 1.0 / BPM * 60  # seconds per beat
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time
BAR_COUNT = 4

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(*TIME_SIGNATURE, time=0.0)]

# Create instruments
bass_instrument = Instrument(program=33)  # Acoustic Bass
piano_instrument = Instrument(program=0)  # Acoustic Grand Piano
drums_instrument = Instrument(program=0)  # Drums
sax_instrument = Instrument(program=64)  # Tenor Saxophone

pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# -------------------------------
# 1. DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth, dynamic contrast
# Bar 1 only
# -------------------------------

def create_drums():
    time = 0.0
    for bar in range(1):
        for beat in range(4):
            # Kick on 1 and 3
            if beat in [0, 2]:
                note = Note(36, 110, time, time + 0.1)
                drums_instrument.notes.append(note)
            # Snare on 2 and 4
            if beat in [1, 3]:
                note = Note(38, 100, time, time + 0.1)
                drums_instrument.notes.append(note)
            # Hi-hat on every eighth
            for eighth in range(2):
                note = Note(42, 80, time + eighth * 0.25, time + eighth * 0.25 + 0.05)
                drums_instrument.notes.append(note)
            time += BEAT_DURATION

create_drums()

# -------------------------------
# 2. BASS: Marcus
# Walking line in Dm, roots and fifths, chromatic approaches
# D2-G2, MIDI 38-43
# -------------------------------

def create_bass():
    # Dm7: D, F, A, C
    # Walking line with chromatic approaches
    bass_notes = [
        # Bar 1
        (38, 0.0),  # D2
        (40, 0.25),  # F2 (chromatic approach)
        (43, 0.5),  # A2
        (40, 0.75),  # F2
        # Bar 2
        (38, 1.0),  # D2
        (42, 1.25),  # G2 (chromatic approach)
        (43, 1.5),  # A2
        (40, 1.75),  # F2
        # Bar 3
        (38, 2.0),  # D2
        (42, 2.25),  # G2
        (43, 2.5),  # A2
        (44, 2.75),  # Bb2 (chromatic approach)
        # Bar 4
        (38, 3.0),  # D2
        (40, 3.25),  # F2
        (43, 3.5),  # A2
        (40, 3.75),  # F2
    ]
    for pitch, start in bass_notes:
        note = Note(pitch, 80, start, start + 0.25)
        bass_instrument.notes.append(note)

create_bass()

# -------------------------------
# 3. PIANO: Diane
# Open voicings, different chord each bar, resolve on the last
# Comp on 2 and 4
# -------------------------------

def create_piano():
    # Bar 1: Dm7 (D F A C) - open voicing
    # Bar 2: G7 (G B D F) - open voicing
    # Bar 3: Cm7 (C Eb G Bb) - open voicing
    # Bar 4: F7 (F A C Eb) - open voicing

    # Bar 1: Dm7 - D (D4), F (F4), A (A4), C (C5)
    notes = [
        (62, 0.0, 100),  # D4
        (65, 0.0, 100),  # F4
        (69, 0.0, 100),  # A4
        (67, 0.0, 100),  # C5
    ]

    # Bar 2: G7 - G (G4), B (B4), D (D5), F (F5)
    notes.extend([
        (67, 1.0, 100),  # G4
        (71, 1.0, 100),  # B4
        (72, 1.0, 100),  # D5
        (76, 1.0, 100),  # F5
    ])

    # Bar 3: Cm7 - C (C4), Eb (Eb4), G (G4), Bb (Bb4)
    notes.extend([
        (60, 2.0, 100),  # C4
        (63, 2.0, 100),  # Eb4
        (67, 2.0, 100),  # G4
        (69, 2.0, 100),  # Bb4
    ])

    # Bar 4: F7 - F (F4), A (A4), C (C5), Eb (Eb5)
    notes.extend([
        (65, 3.0, 100),  # F4
        (69, 3.0, 100),  # A4
        (72, 3.0, 100),  # C5
        (74, 3.0, 100),  # Eb5
    ])

    # Comp on 2 and 4 (every bar has a chord, but now resolve on the 4th beat)
    for pitch, start, velocity in notes:
        note = Note(pitch, velocity, start, start + 0.25)
        piano_instrument.notes.append(note)

create_piano()

# -------------------------------
# 4. SAX: You (Dante)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# No scale runs. Use space. Let the silence speak.
# -------------------------------

def create_sax():
    # Dm7: D, F, A, C
    # Motif: D, F, A, [rest] (first bar)
    # Then: D, F, A, C (resolve on the last beat of bar 4)
    sax_notes = [
        # Bar 1
        (62, 0.0, 100),  # D4
        (65, 0.5, 100),  # F4
        (69, 1.0, 100),  # A4
        # Bar 2
        (62, 1.5, 100),  # D4
        (65, 2.0, 100),  # F4
        (69, 2.5, 100),  # A4
        # Bar 3
        (62, 3.0, 100),  # D4
        (65, 3.5, 100),  # F4
        (69, 4.0, 100),  # A4
        # Bar 4
        (67, 4.5, 100),  # C5 (resolve)
    ]
    for pitch, start, velocity in sax_notes:
        note = Note(pitch, velocity, start, start + 0.25)
        sax_instrument.notes.append(note)

create_sax()

# Save the MIDI file
pm.write(OUTPUT_FILE)

print(f"Composition saved to: {os.path.abspath(OUTPUT_FILE)}")
print("Wayne leans forward.")
