
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Dm
bass_notes = [
    (62, 1.5, 0.375),    # D (root) on 1
    (64, 1.875, 0.375),  # Eb (chromatic) on 2
    (65, 2.25, 0.375),   # F on 3
    (62, 2.625, 0.375),  # D on 4
    (67, 3.0, 0.375),    # G on 1
    (69, 3.375, 0.375),  # A on 2
    (71, 3.75, 0.375),   # Bb on 3
    (67, 4.125, 0.375),  # G on 4
    (65, 4.5, 0.375),    # F on 1
    (67, 4.875, 0.375),  # G on 2
    (69, 5.25, 0.375),   # A on 3
    (65, 5.625, 0.375)   # F on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375),  # D7 - D
    (66, 1.875, 0.375),  # D7 - F#
    (67, 1.875, 0.375),  # D7 - G
    (70, 1.875, 0.375),  # D7 - B
    # Bar 3
    (62, 3.375, 0.375),  # D7 - D
    (66, 3.375, 0.375),  # D7 - F#
    (67, 3.375, 0.375),  # D7 - G
    (70, 3.375, 0.375),  # D7 - B
    # Bar 4
    (62, 4.875, 0.375),  # D7 - D
    (66, 4.875, 0.375),  # D7 - F#
    (67, 4.875, 0.375),  # D7 - G
    (70, 4.875, 0.375)   # D7 - B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - motif in Dm
# Bar 2: Start the motif
sax_notes = [
    (62, 1.5, 0.375),    # D on 1
    (64, 1.875, 0.375),  # Eb on 2
    (65, 2.25, 0.375),   # F on 3
    (62, 2.625, 0.375),  # D on 4
    (65, 3.0, 0.375),    # F on 1
    (67, 3.375, 0.375),  # G on 2
    (65, 3.75, 0.375),   # F on 3
    (62, 4.125, 0.375),  # D on 4
    (64, 4.5, 0.375),    # Eb on 1
    (65, 4.875, 0.375),  # F on 2
    (67, 5.25, 0.375),   # G on 3
    (69, 5.625, 0.375)   # A on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
