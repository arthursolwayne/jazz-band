
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
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (38, 0.0), (42, 0.375), (41, 0.75), (38, 1.125),
    # Bar 3
    (42, 1.5), (46, 1.875), (45, 2.25), (42, 2.625),
    # Bar 4
    (46, 3.0), (43, 3.375), (41, 3.75), (38, 4.125)
]
for i, (pitch, time) in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=1.5 + time, end=1.5 + time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    (62, 1.5), (67, 1.5), (69, 1.5), (72, 1.5),
    # Bar 3: Bm7 (B-D-F#-A)
    (67, 2.0), (72, 2.0), (74, 2.0), (76, 2.0),
    # Bar 4: G7 (G-B-D-F)
    (71, 2.5), (76, 2.5), (79, 2.5), (81, 2.5)
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=1.5 + time, end=1.5 + time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), B (71), D (62)
sax_notes = [
    (62, 1.5), (67, 1.5 + 0.1875), (71, 1.5 + 0.375), (62, 1.5 + 0.5625),
    (62, 1.5 + 1.125), (67, 1.5 + 1.3125), (71, 1.5 + 1.5), (62, 1.5 + 1.6875)
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=1.5 + time, end=1.5 + time + 0.125)
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(3):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
