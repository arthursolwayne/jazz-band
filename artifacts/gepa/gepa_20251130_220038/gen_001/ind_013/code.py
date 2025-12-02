
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
    (0.0, 36, 100),    # Kick on 1
    (0.375, 42, 100),  # Hihat on 2
    (0.75, 38, 100),   # Snare on 3
    (1.125, 42, 100),  # Hihat on 4
    (1.5, 36, 100),    # Kick on 1
    (1.875, 42, 100),  # Hihat on 2
    (2.25, 38, 100),   # Snare on 3
    (2.625, 42, 100),  # Hihat on 4
    (3.0, 36, 100),    # Kick on 1
    (3.375, 42, 100),  # Hihat on 2
    (3.75, 38, 100),   # Snare on 3
    (4.125, 42, 100),  # Hihat on 4
    (4.5, 36, 100),    # Kick on 1
    (4.875, 42, 100),  # Hihat on 2
    (5.25, 38, 100),   # Snare on 3
    (5.625, 42, 100)   # Hihat on 4
]
for start, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D
    (1.875, 60, 100), # C
    (2.25, 63, 100),  # D#
    (2.625, 62, 100), # D
    (3.0, 60, 100),   # C
    (3.375, 63, 100), # D#
    (3.75, 62, 100),  # D
    (4.125, 60, 100), # C
    (4.5, 63, 100),   # D#
    (4.875, 62, 100), # D
    (5.25, 60, 100),  # C
    (5.625, 63, 100)  # D#
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64, 100), # F
    (1.875, 69, 100), # Bb
    (2.25, 71, 100),  # D
    (2.25, 62, 100),  # G
    # Bar 3
    (3.375, 64, 100), # F
    (3.375, 69, 100), # Bb
    (3.75, 71, 100),  # D
    (3.75, 62, 100),  # G
    # Bar 4
    (4.875, 64, 100), # F
    (4.875, 69, 100), # Bb
    (5.25, 71, 100),  # D
    (5.25, 62, 100)   # G
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 67, 100),  # Bb
    (1.5, 70, 100),  # D
    (1.625, 69, 100), # C
    (1.75, 67, 100),  # Bb
    (2.0, 70, 100),   # D
    (2.125, 69, 100), # C
    (2.25, 67, 100),  # Bb
    (2.5, 70, 100),   # D
    (2.625, 69, 100), # C
    (2.75, 67, 100),  # Bb
    (3.0, 70, 100),   # D
    (3.125, 69, 100), # C
    (3.25, 67, 100),  # Bb
    (3.5, 70, 100),   # D
    (3.625, 69, 100), # C
    (3.75, 67, 100),  # Bb
    (4.0, 70, 100),   # D
    (4.125, 69, 100), # C
    (4.25, 67, 100),  # Bb
    (4.5, 70, 100),   # D
    (4.625, 69, 100), # C
    (4.75, 67, 100),  # Bb
    (5.0, 70, 100),   # D
    (5.125, 69, 100), # C
    (5.25, 67, 100),  # Bb
    (5.5, 70, 100),   # D
    (5.625, 69, 100), # C
    (5.75, 67, 100)   # Bb
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
