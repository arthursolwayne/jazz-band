
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.125, 38, 100), # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (1.5, 60, 100),  # F
    (1.75, 61, 100), # Gb
    (2.0, 59, 100),  # E
    (2.25, 60, 100), # F
    (2.5, 62, 100),  # G
    (2.75, 63, 100), # Ab
    (3.0, 60, 100),  # F
    (3.25, 61, 100), # Gb
    (3.5, 59, 100),  # E
    (3.75, 60, 100), # F
    (4.0, 62, 100),  # G
    (4.25, 63, 100), # Ab
    (4.5, 60, 100),  # F
    (4.75, 61, 100), # Gb
    (5.0, 59, 100),  # E
    (5.25, 60, 100)  # F
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane)
piano_notes = [
    (1.5, 64, 100),  # F7
    (1.5, 67, 100),  # A7
    (1.75, 65, 100), # G7
    (1.75, 69, 100), # C8
    (2.0, 64, 100),  # F7
    (2.0, 67, 100),  # A7
    (2.25, 65, 100), # G7
    (2.25, 69, 100), # C8
    (2.5, 64, 100),  # F7
    (2.5, 67, 100),  # A7
    (2.75, 65, 100), # G7
    (2.75, 69, 100), # C8
    (3.0, 64, 100),  # F7
    (3.0, 67, 100),  # A7
    (3.25, 65, 100), # G7
    (3.25, 69, 100), # C8
    (3.5, 64, 100),  # F7
    (3.5, 67, 100),  # A7
    (3.75, 65, 100), # G7
    (3.75, 69, 100), # C8
    (4.0, 64, 100),  # F7
    (4.0, 67, 100),  # A7
    (4.25, 65, 100), # G7
    (4.25, 69, 100), # C8
    (4.5, 64, 100),  # F7
    (4.5, 67, 100),  # A7
    (4.75, 65, 100), # G7
    (4.75, 69, 100)  # C8
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_pattern = [
    (1.5, 36, 100), (1.5, 42, 100), # 1
    (1.75, 38, 100), (1.75, 42, 100), # 2
    (2.0, 36, 100), (2.0, 42, 100), # 3
    (2.25, 38, 100), (2.25, 42, 100), # 4
    (2.5, 36, 100), (2.5, 42, 100), # 1
    (2.75, 38, 100), (2.75, 42, 100), # 2
    (3.0, 36, 100), (3.0, 42, 100), # 3
    (3.25, 38, 100), (3.25, 42, 100), # 4
    (3.5, 36, 100), (3.5, 42, 100), # 1
    (3.75, 38, 100), (3.75, 42, 100), # 2
    (4.0, 36, 100), (4.0, 42, 100), # 3
    (4.25, 38, 100), (4.25, 42, 100), # 4
    (4.5, 36, 100), (4.5, 42, 100), # 1
    (4.75, 38, 100), (4.75, 42, 100)  # 2
]
for time, note, velocity in drum_pattern:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Saxophone (Dante) - one short motif, make it sing
sax_notes = [
    # Bar 2
    (1.5, 62, 100),  # G (Fm)
    (1.625, 64, 100), # A
    (1.75, 62, 100),  # G
    (1.875, 65, 100), # Bb
    # Bar 3
    (2.0, 62, 100),  # G
    (2.125, 64, 100), # A
    (2.25, 62, 100),  # G
    (2.375, 65, 100), # Bb
    # Bar 4
    (2.5, 62, 100),  # G
    (2.625, 64, 100), # A
    (2.75, 62, 100),  # G
    (2.875, 65, 100)  # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")
