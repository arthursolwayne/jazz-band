
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
drum_notes = [
    (36, 0.0, 0.375),    # kick on 1
    (38, 0.375, 0.375),  # snare on 2
    (42, 0.0, 0.1875),   # hihat on 1
    (42, 0.1875, 0.1875),# hihat on &
    (42, 0.375, 0.1875), # hihat on 2
    (42, 0.5625, 0.1875),# hihat on &
    (42, 0.75, 0.1875),  # hihat on 3
    (42, 0.9375, 0.1875),# hihat on &
    (42, 1.125, 0.1875), # hihat on 4
    (36, 1.125, 0.375),  # kick on 3
    (38, 1.5, 0.375)     # snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),    # D
    (46, 1.875, 0.375),  # Eb
    (48, 2.25, 0.375),   # F
    (47, 2.625, 0.375),  # E
    (45, 2.625, 0.375),  # D
    (46, 3.0, 0.375),    # Eb
    (48, 3.375, 0.375),  # F
    (47, 3.75, 0.375),   # E
    (45, 3.75, 0.375),   # D
    (46, 4.125, 0.375),  # Eb
    (48, 4.5, 0.375),    # F
    (47, 4.875, 0.375),  # E
    (45, 4.875, 0.375)   # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (50, 1.5, 0.375),    # F7 - F
    (53, 1.5, 0.375),    # F7 - A
    (57, 1.5, 0.375),    # F7 - C
    (55, 1.5, 0.375),    # F7 - Bb
    # Bar 3 (2.625 - 3.375s)
    (50, 2.625, 0.375),  # F7 - F
    (53, 2.625, 0.375),  # F7 - A
    (57, 2.625, 0.375),  # F7 - C
    (55, 2.625, 0.375),  # F7 - Bb
    # Bar 4 (4.125 - 4.875s)
    (50, 4.125, 0.375),  # F7 - F
    (53, 4.125, 0.375),  # F7 - A
    (57, 4.125, 0.375),  # F7 - C
    (55, 4.125, 0.375)   # F7 - Bb
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: motif in F minor, expressive, with space
# Motif: F - Bb - Eb - D (1.5 - 2.25s)
# Then rest (2.25 - 2.625s)
# Then F - Bb - D (2.625 - 3.375s)
# Then rest (3.375 - 3.75s)
# Then F - Bb - Eb - D (3.75 - 4.5s)
# Then rest (4.5 - 4.875s)
# Then F - Bb (4.875 - 5.25s)
# Then rest (5.25 - 5.625s)
# Then F (5.625 - 6.0s)

sax_notes = [
    (53, 1.5, 0.375),    # F
    (50, 1.875, 0.375),  # Bb
    (48, 2.25, 0.375),   # Eb
    (47, 2.625, 0.375),  # D
    (53, 2.625, 0.375),  # F
    (50, 2.625, 0.375),  # Bb
    (53, 3.0, 0.375),    # F
    (50, 3.375, 0.375),  # Bb
    (53, 3.75, 0.375),   # F
    (50, 4.125, 0.375),  # Bb
    (53, 4.5, 0.375),    # F
    (50, 4.875, 0.375),  # Bb
    (53, 5.25, 0.375),   # F
    (50, 5.625, 0.375)   # Bb
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
