
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat on 1
    (42, 0.125, 0.125),  # Hihat on 2
    (38, 0.125, 0.375),  # Snare on 2
    (42, 0.25, 0.125),  # Hihat on 3
    (36, 0.375, 0.375),  # Kick on 3
    (42, 0.375, 0.125),  # Hihat on 3
    (42, 0.5, 0.125),  # Hihat on 4
    (38, 0.5, 0.375),  # Snare on 4
    (42, 0.625, 0.125),  # Hihat on 4
    (42, 0.75, 0.125),  # Hihat on 5
    (42, 0.875, 0.125),  # Hihat on 6
    (42, 1.0, 0.125),  # Hihat on 7
    (42, 1.125, 0.125),  # Hihat on 8
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (43, 1.5, 0.375),  # F
    (41, 1.875, 0.375),  # Eb
    (42, 2.25, 0.375),  # D
    (44, 2.625, 0.375),  # F
    # Bar 3 (3.0 - 4.5s)
    (45, 3.0, 0.375),  # G
    (43, 3.375, 0.375),  # F
    (42, 3.75, 0.375),  # E
    (44, 4.125, 0.375),  # F
    # Bar 4 (4.5 - 6.0s)
    (41, 4.5, 0.375),  # Eb
    (42, 4.875, 0.375),  # D
    (44, 5.25, 0.375),  # F
    (45, 5.625, 0.375),  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (44, 1.5, 0.25),  # F7 (F, A, C, Eb)
    (46, 1.5, 0.25),
    (48, 1.5, 0.25),
    (41, 1.5, 0.25),
    (44, 1.75, 0.25),
    (46, 1.75, 0.25),
    (48, 1.75, 0.25),
    (41, 1.75, 0.25),
    # Bar 3 (3.0 - 4.5s)
    (44, 3.0, 0.25),
    (46, 3.0, 0.25),
    (48, 3.0, 0.25),
    (41, 3.0, 0.25),
    (44, 3.25, 0.25),
    (46, 3.25, 0.25),
    (48, 3.25, 0.25),
    (41, 3.25, 0.25),
    # Bar 4 (4.5 - 6.0s)
    (44, 4.5, 0.25),
    (46, 4.5, 0.25),
    (48, 4.5, 0.25),
    (41, 4.5, 0.25),
    (44, 4.75, 0.25),
    (46, 4.75, 0.25),
    (48, 4.75, 0.25),
    (41, 4.75, 0.25),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: short motif, start on 1, leave it hanging
sax_notes = [
    (44, 1.5, 0.375),  # F
    (46, 1.875, 0.375),  # G
    (44, 2.25, 0.375),  # F
    (42, 2.625, 0.375),  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
