
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
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb (chromatic)
    (65, 2.25, 0.375),  # F
    (67, 2.625, 0.375),  # G
    (69, 3.0, 0.375),  # A
    (71, 3.375, 0.375),  # Bb (chromatic)
    (72, 3.75, 0.375),  # B
    (71, 4.125, 0.375),  # Bb
    (69, 4.5, 0.375),  # A
    (67, 4.875, 0.375),  # G
    (65, 5.25, 0.375),  # F
    (64, 5.625, 0.375)   # E (chromatic)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.5, 0.375),  # G7
    (71, 1.5, 0.375),
    (74, 1.5, 0.375),
    (72, 1.5, 0.375),
    # Bar 3
    (67, 3.0, 0.375),  # G7
    (71, 3.0, 0.375),
    (74, 3.0, 0.375),
    (72, 3.0, 0.375),
    # Bar 4
    (67, 4.5, 0.375),  # G7
    (71, 4.5, 0.375),
    (74, 4.5, 0.375),
    (72, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))

# Saxophone (Dante) - One short motif, make it sing
# D (62), F (65), G (67), D (62)
sax_notes = [
    (62, 1.5, 0.375),
    (65, 1.875, 0.375),
    (67, 2.25, 0.375),
    (62, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
