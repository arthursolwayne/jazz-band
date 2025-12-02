
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 80), # Hihat on 2
    (0.75, 38, 100), # Snare on 2
    (1.125, 42, 80), # Hihat on 3
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 80), # Hihat on 4
    (2.25, 38, 100), # Snare on 4
    (2.625, 42, 80)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches, melodic
bass_notes = [
    (1.5, 64, 80),   # F
    (1.75, 65, 75),  # Gb
    (2.0, 67, 85),   # A
    (2.25, 69, 80),  # Bb
    (2.5, 71, 75),   # B
    (2.75, 72, 85),  # C
    (3.0, 74, 80),   # Db
    (3.25, 76, 75),  # D
    (3.5, 77, 85),   # Eb
    (3.75, 79, 80),  # E
    (4.0, 81, 75),   # F
    (4.25, 83, 85),  # Gb
    (4.5, 85, 80),   # A
    (4.75, 87, 75),  # Bb
    (5.0, 89, 85),   # B
    (5.25, 91, 80),  # C
    (5.5, 93, 75),   # Db
    (5.75, 95, 85)   # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64, 100),  # F7 (F, A, C, Eb)
    (1.5, 69, 100),
    (1.5, 72, 100),
    (1.5, 67, 100),
    (2.0, 64, 100),
    (2.0, 69, 100),
    (2.0, 72, 100),
    (2.0, 67, 100),
    (3.0, 64, 100),
    (3.0, 69, 100),
    (3.0, 72, 100),
    (3.0, 67, 100),
    (4.0, 64, 100),
    (4.0, 69, 100),
    (4.0, 72, 100),
    (4.0, 67, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66, 100),  # G
    (1.75, 71, 100), # Bb
    (2.0, 66, 100),  # G
    (2.25, 74, 100), # Db
    (2.5, 69, 100),  # A
    (3.0, 66, 100),  # G
    (3.25, 71, 100), # Bb
    (3.5, 69, 100),  # A
    (3.75, 74, 100), # Db
    (4.0, 66, 100),  # G (resolve)
    (4.25, 69, 100), # A
    (4.5, 71, 100),  # Bb
    (4.75, 74, 100)  # Db
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
