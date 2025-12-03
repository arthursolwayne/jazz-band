
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums in bar 1
for note in [36, 38, 42]:
    for beat in range(4):
        time = beat * 0.375
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5),   # D2
    (40, 1.875), # Eb2 (chromatic approach)
    (43, 2.25),  # G2
    (45, 2.625), # Ab2 (chromatic approach)
    (48, 3.0),   # C3
    (50, 3.375), # Db3 (chromatic approach)
    (53, 3.75),  # E3
    (55, 4.125), # F3 (chromatic approach)
    (58, 4.5),   # A3
    (60, 4.875), # Bb3 (chromatic approach)
    (64, 5.25),  # D4
    (66, 5.625), # Eb4 (chromatic approach)
]
for pitch, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note_obj)

# Piano chords (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),
    (67, 1.875), (69, 1.875), (72, 1.875), (76, 1.875),
    (62, 2.25), (64, 2.25), (67, 2.25), (72, 2.25),
    (62, 2.625), (67, 2.625), (69, 2.625), (72, 2.625)
]
for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Bar 3: Gm7 (G Bb D F)
piano_notes = [
    (67, 3.0), (69, 3.0), (72, 3.0), (74, 3.0),
    (69, 3.375), (72, 3.375), (74, 3.375), (76, 3.375),
    (67, 3.75), (72, 3.75), (74, 3.75), (76, 3.75),
    (67, 4.125), (72, 4.125), (76, 4.125), (79, 4.125)
]
for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Bar 4: Cmaj7 (C E G B)
piano_notes = [
    (60, 4.5), (64, 4.5), (67, 4.5), (71, 4.5),
    (67, 4.875), (71, 4.875), (74, 4.875), (76, 4.875),
    (60, 5.25), (64, 5.25), (67, 5.25), (71, 5.25),
    (60, 5.625), (67, 5.625), (71, 5.625), (76, 5.625)
]
for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Drums in bars 2-4
for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 1) * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note_obj = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note_obj)
        if beat == 1 or beat == 3:
            note_obj = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note_obj)
        note_obj = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note_obj)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25), (65, 2.625)
]
for pitch, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Bar 3: Leave it hanging
sax_notes = [
    (62, 3.0), (65, 3.375), (67, 3.75), (65, 4.125)
]
for pitch, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Bar 4: Come back and finish it
sax_notes = [
    (67, 4.5), (65, 4.875), (62, 5.25), (64, 5.625)
]
for pitch, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
