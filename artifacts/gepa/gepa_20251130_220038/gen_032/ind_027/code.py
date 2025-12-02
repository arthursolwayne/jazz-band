
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1& (1/8)
    (42, 0.375, 0.1875),# Hihat on 2& (2/8)
    (38, 0.5, 0.375),   # Snare on 3
    (42, 0.5, 0.1875),  # Hihat on 3& (3/8)
    (42, 0.875, 0.1875),# Hihat on 4& (4/8)
    (36, 1.0, 0.375)    # Kick on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in D
bass_notes = [
    (62, 1.5, 0.375),  # D (1)
    (64, 1.875, 0.375),# Eb (2)
    (65, 2.25, 0.375), # E (3)
    (67, 2.625, 0.375),# F# (4)
    (69, 3.0, 0.375),  # G (1)
    (71, 3.375, 0.375),# A (2)
    (72, 3.75, 0.375), # Bb (3)
    (74, 4.125, 0.375),# B (4)
    (76, 4.5, 0.375),  # C (1)
    (77, 4.875, 0.375),# C# (2)
    (79, 5.25, 0.375), # D (3)
    (81, 5.625, 0.375) # D# (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.375),  # D7 (2)
    (67, 1.875, 0.375),  # F# (2)
    (72, 1.875, 0.375),  # Bb (2)
    (76, 1.875, 0.375),  # C (2)
    (62, 2.625, 0.375),  # D7 (4)
    (67, 2.625, 0.375),  # F# (4)
    (72, 2.625, 0.375),  # Bb (4)
    (76, 2.625, 0.375),  # C (4)
    (62, 4.125, 0.375),  # D7 (2)
    (67, 4.125, 0.375),  # F# (2)
    (72, 4.125, 0.375),  # Bb (2)
    (76, 4.125, 0.375),  # C (2)
    (62, 4.875, 0.375),  # D7 (4)
    (67, 4.875, 0.375),  # F# (4)
    (72, 4.875, 0.375),  # Bb (4)
    (76, 4.875, 0.375)   # C (4)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Hihat on 1&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Hihat on 2&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Hihat on 3&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on 4&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125))

# Sax (Dante) - motif in D, start it, leave it hanging, come back and finish it
# Motif: D - F# - Bb - C
# Start at bar 2, play D (62), F# (67), Bb (72), then leave it hanging on C (76)
# Then come back at bar 3 and finish it with a D (62) on the 3rd beat
sax_notes = [
    (62, 1.875, 0.375),  # F#
    (67, 1.875, 0.375),
    (72, 1.875, 0.375),  # Bb
    (76, 1.875, 0.375),  # C
    (62, 3.0, 0.375)     # D (finish the motif on the 3rd beat of bar 3)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
