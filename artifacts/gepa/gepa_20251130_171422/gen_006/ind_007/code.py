
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature track
time_signature = pretty_midi.TimeSignature()
time_signature.numerator = 4
time_signature.denominator = 4
time_signature.time = 0
pm.time_signature_changes = [time_signature]

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
bass_instrument = pretty_midi.Instrument(program=33)  # Double Bass
piano_instrument = pretty_midi.Instrument(program=0)  # Acoustic Piano
drums_instrument = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

pm.instruments = [sax_instrument, bass_instrument, piano_instrument, drums_instrument]

# Set note durations (seconds per beat at 160 BPM = 0.375s)
beat = 0.375
bar = 1.5
note_duration = beat / 2  # 8th note
rest = 0.1  # space between notes

# BAR 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3 (bars are 0 to 1.5, 1.5 to 3, etc.)
drum_notes = [
    (0, 35, 100, 0.1),  # Kick on beat 1
    (beat, 37, 100, 0.1),  # Snare on beat 2
    (beat * 2, 35, 100, 0.1),  # Kick on beat 3
    (beat * 3, 37, 100, 0.1),  # Snare on beat 4
]

# Add hihat on every eighth note
for i in range(8):
    time = i * beat / 2
    drums_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05))

for note in drum_notes:
    start, pitch, velocity, duration = note
    drums_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# BAR 2: Bass line - walking line with chromatic approaches
# F7 chord: F, A, C, E, B (with chromatic passing tones)

bass_notes = [
    (1.5, 65, 80, 0.375),  # F
    (1.875, 66, 80, 0.375),  # F#
    (2.25, 67, 80, 0.375),  # G (chromatic)
    (2.625, 68, 80, 0.375),  # G#
    (3.0, 69, 80, 0.375),  # A
    (3.375, 70, 80, 0.375),  # A#
    (3.75, 71, 80, 0.375),  # B
    (4.125, 72, 80, 0.375),  # C
    (4.5, 71, 80, 0.375),  # B (chromatic)
    (4.875, 69, 80, 0.375),  # A
    (5.25, 68, 80, 0.375),  # G#
    (5.625, 67, 80, 0.375),  # G
    (6.0, 65, 80, 0.375),  # F
]

for note in bass_notes:
    start, pitch, velocity, duration = note
    bass_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# BAR 2: Piano - 7th chords on 2 and 4
# F7: F, A, C, E, B
# F7 on beat 2 and 4

piano_notes = [
    # Beat 2 (start = 1.875)
    (1.875, 65, 100, 0.5),  # F
    (1.875, 70, 100, 0.5),  # A
    (1.875, 69, 100, 0.5),  # C
    (1.875, 67, 100, 0.5),  # E
    (1.875, 71, 100, 0.5),  # B

    # Beat 4 (start = 3.0)
    (3.0, 65, 100, 0.5),  # F
    (3.0, 70, 100, 0.5),  # A
    (3.0, 69, 100, 0.5),  # C
    (3.0, 67, 100, 0.5),  # E
    (3.0, 71, 100, 0.5),  # B
]

for note in piano_notes:
    start, pitch, velocity, duration = note
    piano_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# BAR 2: Saxophone - motif starts

# F (65), Bb (62) - is that a chromatic? No. F, Bb is a tritone. It's a question.
# Use dynamic, expressive phrasing — space is key.

sax_notes = [
    (1.5, 65, 110, 0.25),  # F
    (1.75, 62, 100, 0.25),  # Bb (tritone)
    (2.0, 65, 90, 0.25),  # F again
    (2.25, 62, 85, 0.25),  # Bb
    (2.5, 65, 100, 0.25),  # F
    (2.75, 62, 90, 0.25),  # Bb
    (3.0, 65, 110, 0.25),  # F
    (3.25, 62, 95, 0.25),  # Bb
]

for note in sax_notes:
    start, pitch, velocity, duration = note
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# BAR 3 and 4: Continue the motif with space and variation
# Let the saxophone line breathe, create tension

sax_notes.extend([
    (3.5, 65, 90, 0.375),  # F
    (3.875, 62, 95, 0.375),  # Bb
    (4.25, 67, 100, 0.375),  # C (chromatic lead into resolution)
    (4.625, 65, 110, 0.375),  # F
    (5.0, 69, 100, 0.375),  # A
    (5.375, 67, 95, 0.375),  # G
    (5.75, 65, 110, 0.375),  # F
])

for note in sax_notes:
    start, pitch, velocity, duration = note
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Save the MIDI file
pm.write("dante_russo_intro.mid")
