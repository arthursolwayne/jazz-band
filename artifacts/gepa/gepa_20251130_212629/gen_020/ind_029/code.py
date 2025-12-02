
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Drums')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time parameters (at 160 BPM, 1 beat = 0.375s, 1 bar = 1.5s)
# 4 bars = 6 seconds
bar_length = 1.5  # seconds per bar
beat_length = 0.375  # seconds per beat
note_length = 0.375  # quarter note duration

# BAR 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):  # 4 beats per bar
    # Kick on 1 and 3
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=i * beat_length, end=(i + 1) * beat_length)
        drums.notes.append(note)
    # Snare on 2 and 4
    if i % 2 == 1:
        note = pretty_midi.Note(velocity=100, pitch=38, start=i * beat_length, end=(i + 1) * beat_length)
        drums.notes.append(note)
    # Hihat on every eighth note
    for j in range(2):  # 2 eighth notes per beat
        note = pretty_midi.Note(velocity=80, pitch=42, start=(i * beat_length) + (j * beat_length / 2), end=(i * beat_length) + (j * beat_length / 2) + 0.125)
        drums.notes.append(note)

# BAR 2: Bass enters (Marcus), playing walking line in Dm
# Dm = D, F, A, C
# Walking line with chromatic approaches
bass_notes = [
    (62, 0.0),  # D4
    (61, 0.375),  # C4
    (63, 0.75),  # E4 (chromatic approach)
    (62, 1.125),  # D4
    (60, 1.5),  # C4 (beat 1 of bar 2)
    (62, 1.875),  # D4
    (63, 2.25),  # E4
    (62, 2.625),  # D4
    (60, 3.0),  # C4 (beat 1 of bar 3)
    (62, 3.375),  # D4
    (61, 3.75),  # C4
    (63, 4.125),  # E4
    (62, 4.5),  # D4
    (60, 4.875),  # C4
    (62, 5.25),  # D4
    (63, 5.625),  # E4
    (62, 6.0),  # D4
]

for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + note_length)
    bass.notes.append(note)

# BAR 2: Piano enters (Diane), comping on 2 and 4 with 7th chords
# Dm7 = D, F, A, C
# Comp on 2 and 4
# Bar 2: beat 2
chord = [62, 64, 67, 69]  # Dm7
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=0.75, end=1.125)
    piano.notes.append(note)

# Bar 2: beat 4
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=1.875, end=2.25)
    piano.notes.append(note)

# BAR 2: Sax enters (Dante) — motif starts
# Motif: D (62), F (64), A (67), B (69) — but with a twist
# Use the first three notes, leave the fourth hanging

# D (62) at beat 1
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
sax.notes.append(note)

# F (64) at beat 2
note = pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25)
sax.notes.append(note)

# A (67) at beat 3
note = pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625)
sax.notes.append(note)

# B (69) at beat 4 — held just slightly to make it linger
note = pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0)
sax.notes.append(note)

# BAR 3: Piano continues comping
# Bar 3: beat 2
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=3.0, end=3.375)
    piano.notes.append(note)

# Bar 3: beat 4
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=3.75, end=4.125)
    piano.notes.append(note)

# BAR 3: Bass continues with walking line
# Already covered in the bass_notes list above

# BAR 4: Piano continues comping
# Bar 4: beat 2
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=4.5, end=4.875)
    piano.notes.append(note)

# Bar 4: beat 4
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=5.25, end=5.625)
    piano.notes.append(note)

# BAR 4: Sax — returns to finish the motif
# Return to D (62) at beat 1 of bar 4
note = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875)
sax.notes.append(note)

# Reiterate motif briefly
note = pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625)
sax.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file saved as 'dante_intro.mid'")
