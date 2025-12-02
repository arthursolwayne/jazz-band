
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 & 2
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - Walking line in Fm
bass_notes = [
    (36, 1.5, 1.5),     # F (1)
    (38, 1.5, 1.5),     # Gb (2)
    (37, 1.5, 1.5),     # Ab (3)
    (35, 1.5, 1.5),     # E (4)
    (37, 1.5, 1.5),     # Ab (1)
    (39, 1.5, 1.5),     # Bb (2)
    (38, 1.5, 1.5),     # Gb (3)
    (36, 1.5, 1.5),     # F (4)
    (35, 1.5, 1.5),     # E (1)
    (37, 1.5, 1.5),     # Ab (2)
    (38, 1.5, 1.5),     # Gb (3)
    (36, 1.5, 1.5),     # F (4)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (41, 1.5, 1.5),     # Bb7 (2)
    (41, 1.5, 1.5),     # Bb7 (4)
    # Bar 3
    (41, 1.5, 1.5),     # Bb7 (2)
    (41, 1.5, 1.5),     # Bb7 (4)
    # Bar 4
    (41, 1.5, 1.5),     # Bb7 (2)
    (41, 1.5, 1.5),     # Bb7 (4)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante) - Short motif
sax_notes = [
    (43, 1.5, 1.625),   # Gm (1)
    (42, 1.625, 1.875), # F (2)
    (40, 1.875, 2.125), # Eb (3)
    (42, 2.125, 2.5),   # F (4)
    (43, 2.5, 2.625),   # Gm (1)
    (42, 2.625, 2.875), # F (2)
    (40, 2.875, 3.125), # Eb (3)
    (42, 3.125, 3.5),   # F (4)
    (43, 3.5, 3.625),   # Gm (1)
    (42, 3.625, 3.875), # F (2)
    (40, 3.875, 4.125), # Eb (3)
    (42, 4.125, 4.5),   # F (4)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.875),   # Kick on 1
    (38, 1.875, 1.875), # Snare on 2
    (36, 2.25, 2.625),  # Kick on 3
    (38, 2.625, 2.625), # Snare on 4
    # Bar 3
    (36, 3.0, 3.375),   # Kick on 1
    (38, 3.375, 3.375), # Snare on 2
    (36, 3.75, 4.125),  # Kick on 3
    (38, 4.125, 4.125), # Snare on 4
    # Bar 4
    (36, 4.5, 4.875),   # Kick on 1
    (38, 4.875, 4.875), # Snare on 2
    (36, 5.25, 5.625),  # Kick on 3
    (38, 5.625, 5.625), # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("jazz_intro.mid")
