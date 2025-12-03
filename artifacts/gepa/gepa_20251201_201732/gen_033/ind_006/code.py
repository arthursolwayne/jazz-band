
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Fill the bar with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=80, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 0.0),  # D2
    (40, 0.375),  # F2 (chromatic approach up)
    (43, 0.75),  # A2
    (41, 1.125),  # G2 (chromatic approach down)
    (43, 1.5),  # A2
    (45, 1.875),  # C3 (chromatic approach up)
    (48, 2.25),  # E3
    (46, 2.625),  # D3 (chromatic approach down)
    (48, 3.0),  # E3
    (50, 3.375),  # G3 (chromatic approach up)
    (53, 3.75),  # B3
    (51, 4.125),  # A3 (chromatic approach down)
    (53, 4.5),  # B3
    (55, 4.875),  # D4 (chromatic approach up)
    (58, 5.25),  # F4
    (56, 5.625)  # E4 (chromatic approach down)
]
for note in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[1] + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    (62, 1.5), (67, 1.5), (69, 1.5), (72, 1.5),
    # Bar 3: Gm7 (G-Bb-D-F)
    (71, 3.0), (76, 3.0), (78, 3.0), (81, 3.0),
    # Bar 4: C7 (C-E-G-Bb)
    (60, 4.5), (64, 4.5), (67, 4.5), (70, 4.5)
]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[1] + 0.375)
    piano.notes.append(piano_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    for beat in [0, 1, 2, 3]:
        note = pretty_midi.Note(velocity=80, pitch=42, start=(bar - 1) * 1.5 + beat * 0.375, end=(bar - 1) * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=110, pitch=38, start=(bar - 1) * 1.5 + beat * 0.375, end=(bar - 1) * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in [0, 1, 2, 3]:
        note = pretty_midi.Note(velocity=80, pitch=36, start=(bar - 1) * 1.5 + beat * 0.375, end=(bar - 1) * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - A - (rest)
sax_notes = [
    (62, 1.5, 1.875),  # D
    (67, 1.875, 2.25),  # F#
    (69, 2.25, 2.625),  # A
    (69, 3.0, 3.375),  # A (return)
    (67, 3.375, 3.75),  # F#
    (62, 3.75, 4.125)   # D
]
for note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
