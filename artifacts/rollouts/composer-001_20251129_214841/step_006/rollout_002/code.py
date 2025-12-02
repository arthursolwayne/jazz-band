
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.75),    # Kick on 1
    (38, 0.75, 0.75),   # Snare on 2
    (42, 0.0, 1.5),     # Hihat on every eighth
    (42, 0.375, 0.375),
    (42, 0.75, 0.375),
    (42, 1.125, 0.375),
    (36, 1.5, 0.75),    # Kick on 3
    (38, 1.5, 0.75),    # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (60, 1.5, 0.375),   # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375),   # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375),   # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375), # B
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.5, 0.375),   # C7 (C, E, B)
    (64, 1.5, 0.375),
    (67, 1.5, 0.375),
    # Bar 3
    (60, 3.0, 0.375),   # C7 (C, E, B)
    (64, 3.0, 0.375),
    (67, 3.0, 0.375),
    # Bar 4
    (60, 4.5, 0.375),   # C7 (C, E, B)
    (64, 4.5, 0.375),
    (67, 4.5, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # C
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375), # C
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.75),    # Kick on 1
    (38, 2.25, 0.75),   # Snare on 2
    (36, 3.0, 0.75),    # Kick on 3
    (38, 3.75, 0.75),   # Snare on 4
    # Bar 3
    (36, 4.5, 0.75),    # Kick on 1
    (38, 5.25, 0.75),   # Snare on 2
    (36, 6.0, 0.75),    # Kick on 3
    (38, 6.75, 0.75),   # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add hihat to every eighth in bars 2-4
for i in range(1.5, 6.0, 0.375):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i, end=i + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
