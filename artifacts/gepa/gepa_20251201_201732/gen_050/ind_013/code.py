
import pretty_midi
from pretty_midi import Note, Instrument
import numpy as np

# Constants
BPM = 160
BEAT_DURATION = 60.0 / BPM  # in seconds
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time
TIME_SIGNATURE = (4, 4)

# Key: F minor
ROOT = 'F'
SCALE = ['F', 'G', 'Ab', 'Bb', 'B', 'Db', 'Eb']  # F Locrian for tension
KEY = 'Fm'

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM, time_signature_numerator=4, time_signature_denominator=4)

# Define instruments
drums = Instrument(program=10, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# --- DRUMS: Little Ray (22) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def play_drums(pm, start_time):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.1)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start_time, end=start_time + 0.1)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=start_time + 0.1)

    # Bar 1: Kick on 1, snare on 3, hihat on every eighth
    bar1 = start_time
    kick.start = bar1
    kick.end = bar1 + 0.1
    dr = bar1 + 0.375 * 3
    snare.start = dr
    snare.end = dr + 0.1
    for i in range(8):
        hihat.start = bar1 + i * 0.375
        hihat.end = hihat.start + 0.1
        pm.instruments[0].notes.append(hihat.copy())

    # Bar 2-4: Kick on 1, snare on 3, hihat on every eighth
    for bar in range(2, 5):
        start = bar1 + (bar - 1) * BAR_DURATION
        kick.start = start
        kick.end = start + 0.1
        dr = start + 0.375 * 3
        snare.start = dr
        snare.end = dr + 0.1
        for i in range(8):
            hihat.start = start + i * 0.375
            hihat.end = hihat.start + 0.1
            pm.instruments[0].notes.append(hihat.copy())
    pm.instruments[0].notes.append(kick)
    pm.instruments[0].notes.append(snare)

play_drums(pm, 0.0)

# --- BASS: Marcus (60 years old) ---
# Walking line (roots and fifths with chromatic approaches)
def play_bass(pm, start_time):
    # Fm7: F, Ab, C, Db
    # Roots and fifths with chromatic approaches
    # Bar 1: F -> Ab (chromatic approach)
    # Bar 2: Bb -> B (chromatic approach)
    # Bar 3: Eb -> D (chromatic approach)
    # Bar 4: F -> G (chromatic approach)

    # Fm i - ii - iii - iv
    # F -> Ab (chromatic up)
    # Bb -> B (chromatic up)
    # Eb -> D (chromatic down)
    # F -> G (chromatic up)

    for bar in range(4):
        start = start_time + bar * BAR_DURATION
        if bar == 0:
            # F -> Ab, chromatic up
            note1 = Note(velocity=100, pitch=53, start=start, end=start + 0.25)
            note2 = Note(velocity=100, pitch=54, start=start + 0.25, end=start + 0.5)
            pm.instruments[1].notes.append(note1)
            pm.instruments[1].notes.append(note2)
        elif bar == 1:
            # Bb -> B, chromatic up
            note1 = Note(velocity=100, pitch=48, start=start, end=start + 0.25)
            note2 = Note(velocity=100, pitch=49, start=start + 0.25, end=start + 0.5)
            pm.instruments[1].notes.append(note1)
            pm.instruments[1].notes.append(note2)
        elif bar == 2:
            # Eb -> D, chromatic down
            note1 = Note(velocity=100, pitch=50, start=start, end=start + 0.25)
            note2 = Note(velocity=100, pitch=49, start=start + 0.25, end=start + 0.5)
            pm.instruments[1].notes.append(note1)
            pm.instruments[1].notes.append(note2)
        elif bar == 3:
            # F -> G, chromatic up
            note1 = Note(velocity=100, pitch=53, start=start, end=start + 0.25)
            note2 = Note(velocity=100, pitch=55, start=start + 0.25, end=start + 0.5)
            pm.instruments[1].notes.append(note1)
            pm.instruments[1].notes.append(note2)

play_bass(pm, 0.0)

# --- PIANO: Diane (angry, open voicings, comp on 2 and 4) ---
def play_piano(pm, start_time):
    # Bar 1: Fm7 (F, Ab, C, Eb) – open voicing
    # Bar 2: Bb7 (Bb, Db, F, Ab) – open voicing
    # Bar 3: Eb7 (Eb, G, Bb, Db) – open voicing
    # Bar 4: F7 (F, A, C, Eb) – open voicing

    # Comp on 2 and 4 with open voicings
    for bar in range(4):
        start = start_time + bar * BAR_DURATION
        if bar == 0:
            # Fm7 – open voicing
            notes = [53, 56, 60, 57]  # F, Ab, C, Eb
            for pitch in notes:
                note = Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
                pm.instruments[2].notes.append(note)
        elif bar == 1:
            # Bb7 – open voicing
            notes = [50, 53, 57, 60]  # Bb, Db, F, Ab
            for pitch in notes:
                note = Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
                pm.instruments[2].notes.append(note)
        elif bar == 2:
            # Eb7 – open voicing
            notes = [50, 55, 57, 60]  # Eb, G, Bb, Db
            for pitch in notes:
                note = Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
                pm.instruments[2].notes.append(note)
        elif bar == 3:
            # F7 – open voicing
            notes = [53, 55, 60, 64]  # F, A, C, Eb
            for pitch in notes:
                note = Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
                pm.instruments[2].notes.append(note)

play_piano(pm, 0.0)

# --- SAX: You (Dante) – one short motif, make it sing, leave it hanging
def play_sax(pm, start_time):
    # Bar 1: You are the question
    # Bar 2: You start the melody
    # Bar 3: You build
    # Bar 4: You leave it hanging

    # Bar 1: silence
    # Bar 2: Motif
    # Bar 3: continuation
    # Bar 4: suspension

    # Notes: F, Ab, Bb, B
    # Motif: F (start), Ab (chromatic), Bb (resolution), B (suspension)

    bar2_start = start_time + 1 * BAR_DURATION
    bar3_start = start_time + 2 * BAR_DURATION
    bar4_start = start_time + 3 * BAR_DURATION

    # Bar 2: sax motif
    # F -> Ab -> Bb -> B
    # F (53) -> Ab (56) -> Bb (57) -> B (59)
    # Length: 0.5s per note
    # Play F, Ab, Bb, B with slight delay to build tension

    note1 = Note(velocity=110, pitch=53, start=bar2_start, end=bar2_start + 0.5)
    note2 = Note(velocity=110, pitch=56, start=bar2_start + 0.5, end=bar2_start + 1.0)
    note3 = Note(velocity=110, pitch=57, start=bar2_start + 1.0, end=bar2_start + 1.5)
    note4 = Note(velocity=110, pitch=59, start=bar2_start + 1.5, end=bar2_start + 2.0)
    pm.instruments[3].notes.append(note1)
    pm.instruments[3].notes.append(note2)
    pm.instruments[3].notes.append(note3)
    pm.instruments[3].notes.append(note4)

    # Bar 3: continuation
    # Tie B (59) into a new note (Ab, 56)
    note5 = Note(velocity=110, pitch=56, start=bar3_start + 0.5, end=bar3_start + 1.5)
    pm.instruments[3].notes.append(note5)

    # Bar 4: suspension on B (59)
    note6 = Note(velocity=110, pitch=59, start=bar4_start, end=bar4_start + 1.0)
    pm.instruments[3].notes.append(note6)

play_sax(pm, 0.0)

# Save MIDI file
pm.write("jazz_intro_dante_russo.mid")
