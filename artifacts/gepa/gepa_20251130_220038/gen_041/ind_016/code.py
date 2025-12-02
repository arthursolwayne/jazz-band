
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
    (0.0, 36, 100),        # Kick on beat 1
    (0.75, 42, 100),       # Hihat on beat 2
    (1.125, 38, 100),      # Snare on beat 3
    (1.5, 42, 100),        # Hihat on beat 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62, 100),       # D
    (1.875, 61, 100),     # C#
    (2.25, 63, 100),      # D#
    (2.625, 65, 100),     # F
    (3.0, 65, 100),       # F
    (3.375, 64, 100),     # E
    (3.75, 66, 100),      # F#
    (4.125, 67, 100),     # G
    (4.5, 69, 100),       # A
    (4.875, 68, 100),     # Ab
    (5.25, 70, 100),      # Bb
    (5.625, 72, 100),     # B
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 67, 100),     # G7
    (1.875, 71, 100),     # B
    (1.875, 72, 100),     # C
    (2.625, 67, 100),     # G7
    (2.625, 71, 100),     # B
    (2.625, 72, 100),     # C
    # Bar 3
    (3.375, 71, 100),     # B7
    (3.375, 74, 100),     # D#
    (3.375, 76, 100),     # F#
    (4.125, 71, 100),     # B7
    (4.125, 74, 100),     # D#
    (4.125, 76, 100),     # F#
    # Bar 4
    (4.875, 67, 100),     # G7
    (4.875, 71, 100),     # B
    (4.875, 72, 100),     # C
    (5.625, 67, 100),     # G7
    (5.625, 71, 100),     # B
    (5.625, 72, 100),     # C
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax: Melody — introduce a motif, leave it hanging, come back and finish it
# Motif: D (62) -> F# (66) -> A (69) -> D (62)
sax_notes = [
    (1.5, 62, 100),       # D
    (1.625, 66, 100),     # F#
    (1.75, 69, 100),      # A
    (1.875, 62, 100),     # D
    (2.25, 62, 100),      # D (return)
    (2.375, 66, 100),     # F#
    (2.5, 69, 100),       # A
    (2.625, 62, 100),     # D
    (3.0, 62, 100),       # D
    (3.125, 66, 100),     # F#
    (3.25, 69, 100),      # A
    (3.375, 62, 100),     # D
    (3.75, 62, 100),      # D
    (3.875, 66, 100),     # F#
    (4.0, 69, 100),       # A
    (4.125, 62, 100),     # D
    (4.5, 62, 100),       # D
    (4.625, 66, 100),     # F#
    (4.75, 69, 100),      # A
    (4.875, 62, 100),     # D
    (5.25, 62, 100),      # D
    (5.375, 66, 100),     # F#
    (5.5, 69, 100),       # A
    (5.625, 62, 100),     # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Drums for bars 2-4
drum_notes = [
    (1.5, 36, 100),        # Kick on beat 1
    (1.875, 42, 100),      # Hihat on beat 2
    (2.25, 38, 100),       # Snare on beat 3
    (2.625, 42, 100),      # Hihat on beat 4
    (3.0, 36, 100),        # Kick on beat 1
    (3.375, 42, 100),      # Hihat on beat 2
    (3.75, 38, 100),       # Snare on beat 3
    (4.125, 42, 100),      # Hihat on beat 4
    (4.5, 36, 100),        # Kick on beat 1
    (4.875, 42, 100),      # Hihat on beat 2
    (5.25, 38, 100),       # Snare on beat 3
    (5.625, 42, 100),      # Hihat on beat 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
