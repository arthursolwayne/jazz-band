
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Acoustic Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Grand Piano
sax = pretty_midi.Instrument(program=69)    # Tenor Saxophone

# Time per bar at 160 BPM: 60 / 160 * 4 = 1.5 seconds
bar_length = 1.5
time_per_beat = bar_length / 4

# Bar 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beats 1 and 3 (time 0.0, 1.5)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.05))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.55))

# Snare on beats 2 and 4 (time 0.75, 2.25)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.8))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.3))

# Hi-hat on every eighth note (time 0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625)
for t in np.arange(0.0, 2.625, 0.375):
    if t != 0.0:  # skip the kick
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05))

# Bar 2: Everyone enters. Diane plays open voicings
# Time starts at bar_length = 1.5

# Bass line: Walking line with chromatic approaches (D2-G2)
# Roots and fifths, with chromatic approaches
bass_notes = [
    (1.5, 62),  # D2
    (1.75, 64),  # Eb2 (chromatic approach)
    (2.0, 67),  # G2
    (2.25, 65),  # F#2 (chromatic approach)
]
for t, p in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (1.5, 65),  # F
    (1.5, 69),  # C
    (1.5, 71),  # Eb
    (1.5, 73),  # Ab
]
for t, p in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.5))

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (2.0, 71),  # Bb
    (2.0, 69),  # D
    (2.0, 65),  # F
    (2.0, 73),  # Ab
]
for t, p in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.5))

# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    (2.5, 67),  # C
    (2.5, 72),  # E
    (2.5, 71),  # G
    (2.5, 73),  # Bb
]
for t, p in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.5))

# Sax: One short, memorable motif. Start it, leave it hanging.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Ab - Bb - (rest) -> C

# Bar 2: Start the motif (F - Ab - Bb)
sax_notes = [
    (1.5, 65),  # F
    (1.625, 69),  # Ab
    (1.75, 67),  # Bb
]
for t, p in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.125))

# Bar 4: Return to finish the motif (C)
sax_notes = [
    (2.75, 67),  # C
]
for t, p in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.125))

# Add instruments to the PrettyMIDI object
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Write to a MIDI file
pm.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
