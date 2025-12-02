
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

# Bass line (Marcus)
bass_notes = [
    (36, 1.5, 0.375),      # F (root)
    (37, 1.875, 0.375),    # Gb (chromatic)
    (38, 2.25, 0.375),     # Ab (b7)
    (39, 2.625, 0.375),    # Bb (3)
    (37, 2.625, 0.375),    # Gb (chromatic)
    (38, 3.0, 0.375),      # Ab (b7)
    (40, 3.375, 0.375),    # B (5)
    (41, 3.75, 0.375),     # C (root)
    (42, 4.125, 0.375),    # C# (chromatic)
    (43, 4.5, 0.375),      # D (9)
    (44, 4.875, 0.375),    # Eb (b7)
    (45, 5.25, 0.375),     # E (11)
    (46, 5.625, 0.375),    # F (root)
    (47, 6.0, 0.375)       # F# (chromatic)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane)
piano_notes = [
    (43, 1.5, 0.375),   # D7 (Fm7)
    (45, 1.875, 0.375), # E (Fm7)
    (47, 2.25, 0.375),  # F# (Fm7)
    (48, 2.625, 0.375), # G (Fm7)
    (41, 3.0, 0.375),   # C (Fm7)
    (43, 3.375, 0.375), # D (Fm7)
    (46, 3.75, 0.375),  # F (Fm7)
    (48, 4.125, 0.375), # G (Fm7)
    (42, 4.5, 0.375),   # C (Fm7)
    (44, 4.875, 0.375), # D (Fm7)
    (47, 5.25, 0.375),  # F# (Fm7)
    (49, 5.625, 0.375), # G# (Fm7)
    (42, 6.0, 0.375)    # C (Fm7)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante)
sax_notes = [
    (46, 1.5, 0.25),    # F (start of motif)
    (48, 1.75, 0.25),   # G (second note)
    (49, 2.0, 0.25),    # G#
    (47, 2.25, 0.25),   # F#
    (46, 2.5, 0.25),    # F (rest)
    (46, 3.0, 0.25),    # F (return)
    (48, 3.25, 0.25),   # G
    (49, 3.5, 0.25),    # G#
    (47, 3.75, 0.25),   # F#
    (46, 4.0, 0.25),    # F (rest)
    (46, 4.5, 0.25),    # F (return)
    (48, 4.75, 0.25),   # G
    (49, 5.0, 0.25),    # G#
    (47, 5.25, 0.25),   # F#
    (46, 5.5, 0.25),    # F
    (46, 6.0, 0.25)     # F (end)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
