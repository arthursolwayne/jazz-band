
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.75), (38, 2.0), (43, 2.25),
    (40, 2.5), (42, 2.75), (40, 3.0), (43, 3.25),
    (42, 3.5), (44, 3.75), (42, 4.0), (45, 4.25),
    (44, 4.5), (46, 4.75), (44, 5.0), (47, 5.25)
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    (50, 1.5), (53, 1.5), (55, 1.5), (57, 1.5),
    (50, 1.75), (53, 1.75), (55, 1.75), (57, 1.75),
    (50, 2.0), (53, 2.0), (55, 2.0), (57, 2.0),
    (50, 2.25), (53, 2.25), (55, 2.25), (57, 2.25),
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Bar 3: Bm7 (B-D-F#-A)
piano_notes = [
    (56, 2.5), (58, 2.5), (60, 2.5), (62, 2.5),
    (56, 2.75), (58, 2.75), (60, 2.75), (62, 2.75),
    (56, 3.0), (58, 3.0), (60, 3.0), (62, 3.0),
    (56, 3.25), (58, 3.25), (60, 3.25), (62, 3.25),
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Bar 4: Gmaj7 (G-B-D-F#)
piano_notes = [
    (62, 3.5), (65, 3.5), (67, 3.5), (69, 3.5),
    (62, 3.75), (65, 3.75), (67, 3.75), (69, 3.75),
    (62, 4.0), (65, 4.0), (67, 4.0), (69, 4.0),
    (62, 4.25), (65, 4.25), (67, 4.25), (69, 4.25),
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Bar 2-4 same pattern as bar 1
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2 (1.5-2.0): Start motif
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=115, pitch=65, start=1.6, end=1.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.7, end=1.8)
sax.notes.append(note)

# Bar 3 (2.5-2.75): Come back to finish motif
note = pretty_midi.Note(velocity=115, pitch=65, start=2.5, end=2.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=2.6, end=2.75)
sax.notes.append(note)

# Add space between bars
note = pretty_midi.Note(velocity=70, pitch=60, start=2.0, end=2.5)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
