
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
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (62, 1.5, 0.375),  # D (root)
    (64, 1.875, 0.375), # Eb (chromatic)
    (65, 2.25, 0.375),  # E (chromatic)
    (62, 2.625, 0.375), # D
    (67, 2.625, 0.375), # F (chromatic)
    (69, 3.0, 0.375),   # G (chromatic)
    (67, 3.375, 0.375), # F
    (69, 3.75, 0.375),  # G
    (62, 4.125, 0.375), # D
    (64, 4.5, 0.375),   # Eb
    (65, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (67, 5.25, 0.375),  # F
    (69, 5.625, 0.375), # G
    (67, 6.0, 0.375)    # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (62, 1.875, 0.375),  # D7: D, F#, A, C
    (69, 1.875, 0.375),
    (67, 1.875, 0.375),
    (64, 1.875, 0.375),
    (62, 3.0, 0.375),    # D7 again
    (69, 3.0, 0.375),
    (67, 3.0, 0.375),
    (64, 3.0, 0.375),
    (62, 4.5, 0.375),    # D7 again
    (69, 4.5, 0.375),
    (67, 4.5, 0.375),
    (64, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.6875)

    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)

# Saxophone (Dante) - short motif, start it, leave it hanging
sax_notes = [
    (65, 1.5, 0.1875),  # E
    (67, 1.6875, 0.1875), # F
    (69, 1.875, 0.1875),  # G
    (65, 2.0625, 0.1875), # E
    (72, 2.25, 0.1875),   # B
    (69, 2.4375, 0.1875), # G
    (67, 2.625, 0.1875),  # F
    (65, 2.8125, 0.1875), # E
    (69, 3.0, 0.1875),    # G
    (72, 3.1875, 0.1875), # B
    (67, 3.375, 0.1875),  # F
    (69, 3.5625, 0.1875), # G
    (67, 3.75, 0.1875),   # F
    (62, 3.9375, 0.1875), # D
    (65, 4.125, 0.1875),  # E
    (67, 4.3125, 0.1875), # F
    (69, 4.5, 0.1875),    # G
    (67, 4.6875, 0.1875), # F
    (62, 4.875, 0.1875),  # D
    (65, 5.0625, 0.1875), # E
    (67, 5.25, 0.1875),   # F
    (72, 5.4375, 0.1875), # B
    (69, 5.625, 0.1875),  # G
    (65, 5.8125, 0.1875), # E
    (62, 6.0, 0.1875)     # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
