
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

# Bass: walking line with roots and fifths, chromatic approaches
# D2-G2 (MIDI 38-43)
bass_notes = [
    (38, 1.5), (40, 1.75), (41, 2.0), (43, 2.25),
    (38, 2.5), (40, 2.75), (41, 3.0), (43, 3.25),
    (38, 3.5), (40, 3.75), (41, 4.0), (43, 4.25),
    (38, 4.5), (40, 4.75), (41, 5.0), (43, 5.25)
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: open voicings, resolve on the last bar
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes = [
    # Bar 2
    (50, 1.5), (53, 1.5), (55, 1.5), (58, 1.5),
    # Bar 3
    (55, 2.5), (58, 2.5), (60, 2.5), (62, 2.5),
    # Bar 4
    (60, 3.5), (64, 3.5), (67, 3.5), (71, 3.5)
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: one short motif, make it sing
# Motif: D4 (62) -> F#4 (66) -> E4 (64) -> D4 (62)
# Bar 2: Start motif
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5)
sax.notes.append(note)
# Bar 3: Leave it hanging
note = pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25)
sax.notes.append(note)
# Bar 4: Finish it
note = pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5)
sax.notes.append(note)

# Drums: continue kick, snare, hihat for full 4 bars
for bar in range(2, 4):
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

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
