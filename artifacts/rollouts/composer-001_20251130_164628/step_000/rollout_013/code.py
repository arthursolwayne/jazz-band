
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
    (36, 0.0, 1.0),   # Kick on beat 1
    (38, 1.0, 1.0),   # Snare on beat 2
    (42, 0.0, 1.0),   # Hihat on beat 1
    (42, 1.0, 1.0),   # Hihat on beat 2
    (42, 2.0, 1.0),   # Hihat on beat 3
    (42, 3.0, 1.0),   # Hihat on beat 4
    (36, 3.0, 1.0),   # Kick on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375), # F#
    (44, 2.25, 0.375),  # E
    (45, 2.625, 0.375), # F
    # Bar 3
    (47, 2.625, 0.375),  # G
    (46, 2.625, 0.375),  # F#
    (45, 2.625, 0.375),  # F
    (44, 3.0, 0.375),    # E
    # Bar 4
    (43, 3.375, 0.375),  # D
    (44, 3.75, 0.375),   # E
    (45, 4.125, 0.375),  # F
    (46, 4.5, 0.375),    # F#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - comping on 2 and 4, 7th chords
# Bar 2
piano_notes = [
    (53, 1.875, 0.375),  # A7 (C, E, G, Bb)
    (50, 1.875, 0.375),  # F7 (A, C, E, G)
    (50, 1.875, 0.375),  # F7 (A, C, E, G)
    (50, 1.875, 0.375),  # F7 (A, C, E, G)
    # Bar 3
    (53, 3.0, 0.375),    # A7
    (50, 3.0, 0.375),    # F7
    (50, 3.0, 0.375),    # F7
    (50, 3.0, 0.375),    # F7
    # Bar 4
    (53, 4.5, 0.375),    # A7
    (50, 4.5, 0.375),    # F7
    (50, 4.5, 0.375),    # F7
    (50, 4.5, 0.375),    # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),   # Kick on beat 1
    (38, 1.875, 0.375), # Snare on beat 2
    (42, 1.5, 0.375),   # Hihat on beat 1
    (42, 1.875, 0.375), # Hihat on beat 2
    (42, 2.25, 0.375),  # Hihat on beat 3
    (42, 2.625, 0.375), # Hihat on beat 4
    (36, 2.625, 0.375), # Kick on beat 3
    (38, 3.0, 0.375),   # Snare on beat 4
    (36, 3.375, 0.375), # Kick on beat 1
    (38, 3.75, 0.375),  # Snare on beat 2
    (42, 3.375, 0.375), # Hihat on beat 1
    (42, 3.75, 0.375),  # Hihat on beat 2
    (42, 4.125, 0.375), # Hihat on beat 3
    (42, 4.5, 0.375),   # Hihat on beat 4
    (36, 4.5, 0.375),   # Kick on beat 3
    (38, 4.875, 0.375), # Snare on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - short motif, make it sing
# Melody: F, G, Bb, F (Bar 2), then repeat and finish on Bb
sax_notes = [
    (53, 1.5, 0.375),  # F
    (55, 1.875, 0.375), # G
    (51, 2.25, 0.375),  # Bb
    (53, 2.625, 0.375), # F
    (53, 3.0, 0.375),   # F
    (55, 3.375, 0.375), # G
    (51, 3.75, 0.375),  # Bb
    (51, 4.125, 0.375), # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_intro.mid")
