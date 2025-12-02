
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

# Drums in Bar 1
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100)   # Snare on 3
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F minor
bass_notes = [
    (1.5, 45, 100),  # C
    (1.75, 46, 100), # C#
    (2.0, 44, 100),  # B
    (2.25, 45, 100), # C
    (2.5, 47, 100),  # D
    (2.75, 48, 100), # D#
    (3.0, 47, 100),  # D
    (3.25, 45, 100), # C
    (3.5, 43, 100),  # A
    (3.75, 44, 100), # B
    (4.0, 42, 100),  # A
    (4.25, 43, 100), # A#
    (4.5, 42, 100),  # A
    (4.75, 40, 100), # G
    (5.0, 39, 100),  # G#
    (5.25, 40, 100)  # G
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62, 100),  # F7 - F
    (2.0, 67, 100),  # F7 - Bb
    (2.0, 69, 100),  # F7 - C
    (2.0, 71, 100),  # F7 - E
    # Bar 3
    (3.5, 62, 100),  # F7 - F
    (3.5, 67, 100),  # F7 - Bb
    (3.5, 69, 100),  # F7 - C
    (3.5, 71, 100),  # F7 - E
    # Bar 4
    (5.0, 62, 100),  # F7 - F
    (5.0, 67, 100),  # F7 - Bb
    (5.0, 69, 100),  # F7 - C
    (5.0, 71, 100)   # F7 - E
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums in Bars 2-4
drum_pattern = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_pattern:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Saxophone (Dante) - Melody
sax_notes = [
    (1.5, 66, 100),  # F
    (1.75, 69, 100), # A
    (2.0, 67, 100),  # Bb
    (2.25, 66, 100), # F
    (2.5, 64, 100),  # D
    (2.75, 66, 100), # F
    (3.0, 69, 100),  # A
    (3.25, 71, 100), # C
    (3.5, 69, 100),  # A
    (3.75, 67, 100), # Bb
    (4.0, 66, 100),  # F
    (4.25, 64, 100), # D
    (4.5, 62, 100),  # C
    (4.75, 64, 100), # D
    (5.0, 66, 100),  # F
    (5.25, 69, 100)  # A
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
