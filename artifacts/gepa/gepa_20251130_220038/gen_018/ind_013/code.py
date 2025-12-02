
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
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Chromatic walking line in D
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375), # F
    (67, 3.0, 0.375),   # G
    (69, 3.375, 0.375), # A
    (71, 3.75, 0.375),  # B
    (72, 4.125, 0.375), # C
    (69, 4.5, 0.375),   # A
    (67, 4.875, 0.375), # G
    (65, 5.25, 0.375),  # F
    (64, 5.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping rhythm
piano_notes = [
    # Bar 2: D7
    (62, 1.5, 0.375),  # D
    (67, 1.5, 0.375),  # G
    (72, 1.5, 0.375),  # C
    (74, 1.5, 0.375),  # F# (7th)
    # Bar 3: A7
    (69, 3.0, 0.375),  # A
    (74, 3.0, 0.375),  # D
    (79, 3.0, 0.375),  # G
    (81, 3.0, 0.375),  # B (7th)
    # Bar 4: D7
    (62, 4.5, 0.375),  # D
    (67, 4.5, 0.375),  # G
    (72, 4.5, 0.375),  # C
    (74, 4.5, 0.375)   # F# (7th)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif in D, one short phrase, leave it hanging
sax_notes = [
    # Bar 2: D (62) - start on 1
    (62, 1.5, 0.375),  # D
    # Bar 2: F# (67) - start on 2
    (67, 1.875, 0.375),  # F#
    # Bar 3: B (71) - start on 1
    (71, 3.0, 0.375),  # B
    # Bar 3: D (62) - start on 2
    (62, 3.375, 0.375),  # D
    # Bar 4: D (62) - start on 3
    (62, 4.5, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
