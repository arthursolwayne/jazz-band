
# jazz_intro.py
# A 4-bar jazz intro in Fm at 160 BPM, using pretty_midi
# Written for Dante Russo's quartet at The Cellar, with Wayne Shorter in the audience.

import pretty_midi
from pretty_midi import Note, Instrument, TempoChange

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_instrument = Instrument(program=33)  # Electric Bass
piano_instrument = Instrument(program=0)   # Acoustic Piano
drums_instrument = Instrument(program=0)   # Drums
sax_instrument = Instrument(program=64)    # Tenor Saxophone

# Time in seconds per bar (160 BPM = 60 / 160 = 0.375 sec per beat, 1.5 sec per bar)
bar_length = 1.5
note_duration = 0.25  # quarter note
half_duration = 0.5   # eighth note
eighth_duration = 0.125  # sixteenth note

# Time signatures and tempo
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# ----------- DRUMS (Little Ray): Bar 1 (Opening) -----------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    Note(35, 0.0, note_duration),  # Kick on 1
    Note(38, 0.375, note_duration),  # Snare on 2
    Note(42, 0.0, half_duration),   # Hihat on 1
    Note(42, 0.125, half_duration),  # Hihat on 1 + 8th
    Note(42, 0.25, half_duration),  # Hihat on 2
    Note(42, 0.375, half_duration),  # Hihat on 2 + 8th
    Note(42, 0.5, half_duration),   # Hihat on 3
    Note(42, 0.625, half_duration),  # Hihat on 3 + 8th
    Note(35, 0.75, note_duration),  # Kick on 3
    Note(38, 1.125, note_duration),  # Snare on 4
    Note(42, 0.75, half_duration),  # Hihat on 3
    Note(42, 0.875, half_duration),  # Hihat on 3 + 8th
    Note(42, 1.0, half_duration),   # Hihat on 4
    Note(42, 1.125, half_duration),  # Hihat on 4 + 8th
]
drums_instrument.notes.extend(drum_notes)
pm.instruments.append(drums_instrument)

# ----------- SAX (Dante): Bars 2-4 (Melody) -----------
# A short motif, with tension and resolution in Fm
# Start with a motif: Fm7 -> Bb -> Eb -> Ab -> C7 (chromatic approach to Bb)
# The motif is a question, and the resolution is the answer.

# Bar 2: Start the motif
sax_notes = [
    Note(84, 1.5, note_duration),  # F (C4)
    Note(79, 1.75, note_duration),  # Bb (Bb3)
    Note(76, 2.0, note_duration),  # Eb (Eb3)
    Note(72, 2.25, note_duration),  # Ab (Ab3)
    Note(77, 2.5, note_duration),  # B (B3)
    Note(84, 2.75, note_duration),  # F (C4)
    Note(87, 3.0, note_duration),  # A (A4)
    Note(84, 3.25, note_duration),  # F (C4)
    Note(81, 3.5, note_duration),  # D (D4)
    Note(84, 3.75, note_duration),  # F (C4)
    Note(81, 4.0, note_duration),  # D (D4)
    Note(87, 4.25, note_duration),  # A (A4)
    Note(84, 4.5, note_duration),  # F (C4)
    Note(87, 4.75, note_duration),  # A (A4)
    Note(84, 5.0, note_duration),  # F (C4)
]
sax_instrument.notes.extend(sax_notes)
pm.instruments.append(sax_instrument)

# ----------- PIANO (Diane): Bars 2-4 (Accompaniment) -----------
# 7th chords on 2 and 4, comp with tension and movement
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    Note(65, 2.0, note_duration),  # F3 (F)
    Note(60, 2.0, note_duration),  # C3 (C)
    Note(57, 2.0, note_duration),  # Ab2 (Ab)
    Note(55, 2.0, note_duration),  # Eb2 (Eb)

    # Bar 3: Bb7 on 2 and 4 (tension)
    Note(67, 3.0, note_duration),  # Bb3 (Bb)
    Note(62, 3.0, note_duration),  # F3 (F)
    Note(59, 3.0, note_duration),  # D2 (D)
    Note(57, 3.0, note_duration),  # Ab2 (Ab)

    # Bar 4: Fm7 on 2 and 4 (resolution)
    Note(65, 4.0, note_duration),  # F3 (F)
    Note(60, 4.0, note_duration),  # C3 (C)
    Note(57, 4.0, note_duration),  # Ab2 (Ab)
    Note(55, 4.0, note_duration),  # Eb2 (Eb)
]
piano_instrument.notes.extend(piano_notes)
pm.instruments.append(piano_instrument)

# ----------- BASS (Marcus): Bars 2-4 (Walking Line) -----------
# Chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Fm7 walking
    Note(45, 1.5, note_duration),  # C2 (C)
    Note(44, 1.75, note_duration),  # Bb2 (Bb)
    Note(43, 2.0, note_duration),  # Ab2 (Ab)
    Note(41, 2.25, note_duration),  # Eb2 (Eb)
    Note(44, 2.5, note_duration),  # Bb2 (Bb)
    Note(42, 2.75, note_duration),  # G2 (G)
    Note(41, 3.0, note_duration),  # Eb2 (Eb)
    Note(43, 3.25, note_duration),  # Ab2 (Ab)

    # Bar 3: Bb7 walking
    Note(47, 3.5, note_duration),  # D2 (D)
    Note(46, 3.75, note_duration),  # C2 (C)
    Note(45, 4.0, note_duration),  # Bb2 (Bb)
    Note(43, 4.25, note_duration),  # Ab2 (Ab)
    Note(46, 4.5, note_duration),  # C2 (C)
    Note(44, 4.75, note_duration),  # Bb2 (Bb)
    Note(43, 5.0, note_duration),  # Ab2 (Ab)
    Note(41, 5.25, note_duration),  # Eb2 (Eb)

    # Bar 4: Fm7 walking
    Note(45, 5.5, note_duration),  # C2 (C)
    Note(44, 5.75, note_duration),  # Bb2 (Bb)
    Note(43, 6.0, note_duration),  # Ab2 (Ab)
    Note(41, 6.25, note_duration),  # Eb2 (Eb)
]
bass_instrument.notes.extend(bass_notes)
pm.instruments.append(bass_instrument)

# Save the MIDI file
pm.write('dante_intro.mid')
