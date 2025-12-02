
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
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.75),   # Hihat on 2
    (36, 0.75, 1.125),   # Kick on 3
    (42, 1.125, 1.5),    # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    (D2, 1.5, 1.75),     # D2 on 1
    (F2, 1.75, 2.0),     # F2 on 2 (chromatic approach)
    (G2, 2.0, 2.25),     # G2 on 3
    (Bb2, 2.25, 2.5),    # Bb2 on 4 (chromatic approach)
    (C2, 2.5, 2.75),     # C2 on 1
    (Eb2, 2.75, 3.0),    # Eb2 on 2
    (F2, 3.0, 3.25),     # F2 on 3
    (Ab2, 3.25, 3.5),    # Ab2 on 4
    (Bb2, 3.5, 3.75),    # Bb2 on 1
    (Db2, 3.75, 4.0),    # Db2 on 2
    (D2, 4.0, 4.25),     # D2 on 3
    (F2, 4.25, 4.5),     # F2 on 4
    (G2, 4.5, 4.75),     # G2 on 1
    (Bb2, 4.75, 5.0),    # Bb2 on 2
    (C2, 5.0, 5.25),     # C2 on 3
    (Eb2, 5.25, 5.5),    # Eb2 on 4
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Piano: Open voicings, resolve on the last chord
piano_notes = [
    # Bar 2: Dm7 (Dm7) - Open voicing
    (D3, 1.5, 1.75),
    (F3, 1.5, 1.75),
    (A3, 1.5, 1.75),
    (C4, 1.5, 1.75),
    # Bar 3: G7 (G7) - Open voicing
    (G3, 2.0, 2.25),
    (B3, 2.0, 2.25),
    (D4, 2.0, 2.25),
    (F4, 2.0, 2.25),
    # Bar 4: Cm7 (Cm7) - Open voicing
    (C3, 2.5, 2.75),
    (Eb3, 2.5, 2.75),
    (G3, 2.5, 2.75),
    (Bb3, 2.5, 2.75),
    # Bar 2: Comp on 2 and 4
    (D4, 1.75, 2.0),
    (F4, 1.75, 2.0),
    (A4, 1.75, 2.0),
    (C5, 1.75, 2.0),
    # Bar 3: Comp on 2 and 4
    (G4, 2.25, 2.5),
    (B4, 2.25, 2.5),
    (D5, 2.25, 2.5),
    (F5, 2.25, 2.5),
    # Bar 4: Comp on 2 and 4
    (C4, 2.75, 3.0),
    (Eb4, 2.75, 3.0),
    (G4, 2.75, 3.0),
    (Bb4, 2.75, 3.0),
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (E4, 1.5, 1.75),     # Start the motif
    (F4, 1.75, 2.0),     # Leave it hanging
    (E4, 2.5, 2.75),     # Come back and finish it
    (D4, 2.75, 3.0),     # End with a resolution
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.875),    # Kick on 1
    (42, 1.875, 2.25),   # Hihat on 2
    (36, 2.25, 2.625),   # Kick on 3
    (42, 2.625, 3.0),    # Hihat on 4
    # Bar 3
    (36, 3.0, 3.375),    # Kick on 1
    (42, 3.375, 3.75),   # Hihat on 2
    (36, 3.75, 4.125),   # Kick on 3
    (42, 4.125, 4.5),    # Hihat on 4
    # Bar 4
    (36, 4.5, 4.875),    # Kick on 1
    (42, 4.875, 5.25),   # Hihat on 2
    (36, 5.25, 5.625),   # Kick on 3
    (42, 5.625, 6.0),    # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
