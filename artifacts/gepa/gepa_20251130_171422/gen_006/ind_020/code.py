
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100)   # Kick on 3
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D (root)
    (1.75, 60, 100),  # C (chromatic approach)
    (2.0, 64, 100),  # F (3rd)
    (2.25, 65, 100),  # F#
    (2.5, 67, 100),  # A (5th)
    (2.75, 65, 100),  # F#
    (3.0, 64, 100),  # F
    (3.25, 62, 100),  # D
    (3.5, 60, 100),  # C
    (3.75, 62, 100),  # D
    (4.0, 64, 100),  # F
    (4.25, 65, 100),  # F#
    (4.5, 67, 100),  # A
    (4.75, 65, 100),  # F#
    (5.0, 64, 100),  # F
    (5.25, 62, 100),  # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62, 100),  # D
    (2.0, 67, 100),  # A
    (2.0, 69, 100),  # C
    (2.0, 71, 100),  # D
    # Bar 3
    (3.0, 62, 100),  # D
    (3.0, 67, 100),  # A
    (3.0, 69, 100),  # C
    (3.0, 71, 100),  # D
    # Bar 4
    (4.0, 62, 100),  # D
    (4.0, 67, 100),  # A
    (4.0, 69, 100),  # C
    (4.0, 71, 100),  # D
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    # Bar 3
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65, 100),  # F
    (1.75, 67, 100), # A
    (2.0, 65, 100),  # F
    (2.25, 62, 100), # D
    (2.5, 67, 100),  # A
    (2.75, 65, 100), # F
    (3.0, 62, 100),  # D
    (3.25, 65, 100), # F
    (3.5, 67, 100),  # A
    (3.75, 65, 100), # F
    (4.0, 62, 100),  # D
    (4.25, 65, 100), # F
    (4.5, 67, 100),  # A
    (4.75, 65, 100), # F
    (5.0, 62, 100),  # D
    (5.25, 65, 100), # F
    (5.5, 67, 100),  # A
    (5.75, 65, 100), # F
    (6.0, 62, 100)   # D
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
