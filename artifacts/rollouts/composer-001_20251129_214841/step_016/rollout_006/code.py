
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (42, 1.125, 0.1875),  # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375)  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),  # D
    (64, 2.625, 0.375),  # D#
    (65, 3.0, 0.375),  # E
    (67, 3.375, 0.375),  # F#
    (68, 3.75, 0.375),  # G
    (69, 4.125, 0.375),  # G#
    (71, 4.5, 0.375),  # A#
    (72, 4.875, 0.375),  # B
    (71, 5.25, 0.375),  # A#
    (70, 5.625, 0.375),  # A
    (69, 6.0, 0.375)  # G#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (60, 1.5, 0.375),  # C7: C
    (64, 1.5, 0.375),  # C7: E
    (67, 1.5, 0.375),  # C7: G
    (71, 1.5, 0.375),  # C7: B
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.375),  # D7: D
    (67, 3.0, 0.375),  # D7: G
    (70, 3.0, 0.375),  # D7: A
    (74, 3.0, 0.375),  # D7: C
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 0.375),  # C7: C
    (64, 4.5, 0.375),  # C7: E
    (67, 4.5, 0.375),  # C7: G
    (71, 4.5, 0.375),  # C7: B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - Motif: G Bb D (Cmaj7) with a suspended feel
# Start on bar 2, leave it hanging, come back and finish it
sax_notes = [
    (67, 1.5, 0.1875),  # G
    (62, 1.6875, 0.1875),  # Bb
    (69, 1.875, 0.1875),  # D
    (67, 2.0625, 0.1875),  # G
    (62, 2.25, 0.1875),  # Bb
    (69, 2.4375, 0.1875),  # D
    (67, 2.625, 0.1875),  # G
    (62, 2.8125, 0.1875),  # Bb
    (69, 3.0, 0.1875),  # D
    (67, 3.1875, 0.1875),  # G
    (62, 3.375, 0.1875),  # Bb
    (69, 3.5625, 0.1875),  # D
    (67, 3.75, 0.1875),  # G
    (62, 3.9375, 0.1875),  # Bb
    (69, 4.125, 0.1875),  # D
    (67, 4.3125, 0.1875),  # G
    (62, 4.5, 0.1875),  # Bb
    (69, 4.6875, 0.1875),  # D
    (67, 4.875, 0.1875),  # G
    (62, 5.0625, 0.1875),  # Bb
    (69, 5.25, 0.1875),  # D
    (67, 5.4375, 0.1875),  # G
    (62, 5.625, 0.1875),  # Bb
    (69, 5.8125, 0.1875),  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
