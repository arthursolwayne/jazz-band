
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D (38) -> Eb (39) -> G (43) -> A (45)
# Bar 3: B (46) -> C (48) -> D (50) -> Eb (51)
# Bar 4: F (53) -> G (55) -> A (57) -> Bb (58)
bass_notes = [
    (38, 1.5, 1.625), (39, 1.625, 1.75), (43, 1.75, 1.875), (45, 1.875, 2.0),
    (46, 2.0, 2.125), (48, 2.125, 2.25), (50, 2.25, 2.375), (51, 2.375, 2.5),
    (53, 2.5, 2.625), (55, 2.625, 2.75), (57, 2.75, 2.875), (58, 2.875, 3.0),
    (38, 3.0, 3.125), (39, 3.125, 3.25), (43, 3.25, 3.375), (45, 3.375, 3.5)
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C)
# Bar 3: G7 (G, B, D, F)
# Bar 4: A7 (A, C#, E, G)
# Bar 5: Bm7b5 (B, D, F, A)
piano_notes = [
    # Bar 2: D7
    (50, 1.5, 1.75), (53, 1.5, 1.75), (55, 1.5, 1.75), (58, 1.5, 1.75),
    # Bar 3: G7
    (62, 2.0, 2.25), (65, 2.0, 2.25), (67, 2.0, 2.25), (70, 2.0, 2.25),
    # Bar 4: A7
    (65, 2.5, 2.75), (68, 2.5, 2.75), (70, 2.5, 2.75), (73, 2.5, 2.75),
    # Bar 5: Bm7b5
    (67, 3.0, 3.25), (70, 3.0, 3.25), (72, 3.0, 3.25), (74, 3.0, 3.25)
]
for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50) -> F# (53) -> A (55) -> D (50) (first bar)
# Then leave it hanging (no note), then come back and finish it (repeat the motif)
sax_notes = [
    (50, 1.5, 1.6875), (53, 1.6875, 1.875), (55, 1.875, 2.0), (50, 2.0, 2.125),
    (50, 3.0, 3.1875), (53, 3.1875, 3.375), (55, 3.375, 3.5), (50, 3.5, 3.625)
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums: Continue the pattern for bars 2-4
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
midi.write("dante_intro.mid")
