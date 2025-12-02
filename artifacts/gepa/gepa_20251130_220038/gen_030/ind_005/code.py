
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
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),  # Snare on 3
    (1.875, 42, 100), # Hihat on &3
    (2.25, 42, 100), # Hihat on &4
    (2.625, 42, 100), # Hihat on &4
    (3.0, 36, 100)   # Kick on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, no repeats
bass_notes = [
    (1.5, 62, 100),  # D
    (1.875, 60, 100), # C
    (2.25, 64, 100),  # Eb
    (2.625, 62, 100), # D
    (3.0, 65, 100),   # F
    (3.375, 64, 100), # Eb
    (3.75, 62, 100),  # D
    (4.125, 60, 100), # C
    (4.5, 64, 100),   # Eb
    (4.875, 62, 100), # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0s)
    (1.75, 64, 100),  # F7 - F, A, C, Eb
    (2.0, 69, 90),    # A
    (2.25, 60, 90),   # C
    (2.5, 62, 90),    # Eb
    # Bar 3 (3.0-4.5s)
    (3.25, 64, 100),  # F7
    (3.5, 69, 90),    # A
    (3.75, 60, 90),   # C
    (4.0, 62, 90),    # Eb
    # Bar 4 (4.5-6.0s)
    (4.75, 64, 100),  # F7
    (5.0, 69, 90),    # A
    (5.25, 60, 90),   # C
    (5.5, 62, 90),    # Eb
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Melody in Dm - one short motif, make it sing
sax_notes = [
    (1.5, 62, 100),   # D (start of melody)
    (1.875, 64, 100), # Eb
    (2.25, 60, 100),  # C
    (2.625, 64, 100), # Eb
    (3.0, 62, 100),   # D (repeat)
    (3.375, 64, 100), # Eb
    (3.75, 60, 100),  # C
    (4.125, 58, 100), # Bb
    (4.5, 62, 100),   # D (ending)
    (4.875, 64, 100), # Eb
    (5.25, 60, 100),  # C
    (5.625, 62, 100)  # D (resolution)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.375, 42, 100), # Hihat on &1
    (3.75, 42, 100), # Hihat on &2
    (4.125, 38, 100), # Snare on 3
    (4.5, 42, 100), # Hihat on &3
    (4.875, 42, 100), # Hihat on &4
    (5.25, 42, 100), # Hihat on &4
    (5.625, 36, 100), # Kick on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
