
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 1.5),    # D
    (63, 1.5, 1.5),    # Eb (chromatic approach)
    (64, 1.5, 1.5),    # E
    (65, 1.5, 1.5),    # F
    (67, 3.0, 1.5),    # G
    (68, 3.0, 1.5),    # Ab
    (69, 3.0, 1.5),    # A
    (70, 3.0, 1.5),    # Bb
    (72, 4.5, 1.5),    # B
    (73, 4.5, 1.5),    # C
    (74, 4.5, 1.5),    # C#
    (76, 4.5, 1.5)     # D
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    (62, 1.5, 1.5), (67, 1.5, 1.5), (69, 1.5, 1.5), (72, 1.5, 1.5),
    # Bar 3: Bm7 (B D F# A)
    (69, 3.0, 1.5), (74, 3.0, 1.5), (67, 3.0, 1.5), (69, 3.0, 1.5),
    # Bar 4: F7 (F A C Eb)
    (65, 4.5, 1.5), (69, 4.5, 1.5), (72, 4.5, 1.5), (67, 4.5, 1.5)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Motif - start, leave it hanging, come back and finish
# Motif: D (62), F# (67), A (69), rest
sax_notes = [
    (62, 1.5, 1.75),  # D
    (67, 1.75, 2.0),  # F#
    (69, 2.0, 2.25),  # A
    (62, 3.0, 3.25),  # D
    (67, 3.25, 3.5),  # F#
    (69, 3.5, 3.75),  # A
    (62, 4.5, 4.75),  # D
    (67, 4.75, 5.0),  # F#
    (69, 5.0, 5.25)   # A
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.875),  # Kick on 1
    (38, 1.875, 1.875),  # Snare on 2
    (36, 2.25, 2.625),  # Kick on 3
    (38, 2.625, 2.625),  # Snare on 4
    # Bar 3
    (36, 3.0, 3.375),  # Kick on 1
    (38, 3.375, 3.375),  # Snare on 2
    (36, 3.75, 4.125),  # Kick on 3
    (38, 4.125, 4.125),  # Snare on 4
    # Bar 4
    (36, 4.5, 4.875),  # Kick on 1
    (38, 4.875, 4.875),  # Snare on 2
    (36, 5.25, 5.625),  # Kick on 3
    (38, 5.625, 5.625)   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Add hihat on every eighth
for bar in range(2, 5):
    for i in range(0, 4):
        start = 1.5 + (bar - 2) * 1.5 + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
