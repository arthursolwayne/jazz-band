
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
    (1.0, 38, 100),  # Snare on 2
    (1.75, 42, 100), # Hihat on &2
    (2.0, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.75, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 64, 100),  # F (1.5)
    (1.75, 63, 100), # Eb
    (2.0, 65, 100),  # G
    (2.25, 62, 100), # D
    (2.5, 64, 100),  # F
    (2.75, 63, 100), # Eb
    (3.0, 65, 100),  # G
    (3.25, 62, 100), # D
    (3.5, 64, 100),  # F
    (3.75, 63, 100), # Eb
    (4.0, 65, 100),  # G
    (4.25, 62, 100), # D
    (4.5, 64, 100),  # F
    (4.75, 63, 100), # Eb
    (5.0, 65, 100),  # G
    (5.25, 62, 100)  # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64, 100),  # F7: F, A, C, Eb
    (1.5, 72, 100),  # F7
    (1.5, 69, 100),  # F7
    (1.5, 65, 100),  # F7
    (2.0, 64, 100),  # Bb7: Bb, D, F, Ab
    (2.0, 71, 100),  # Bb7
    (2.0, 68, 100),  # Bb7
    (2.0, 66, 100),  # Bb7
    (2.5, 64, 100),  # F7
    (2.5, 72, 100),  # F7
    (2.5, 69, 100),  # F7
    (2.5, 65, 100),  # F7
    (3.0, 64, 100),  # Bb7
    (3.0, 71, 100),  # Bb7
    (3.0, 68, 100),  # Bb7
    (3.0, 66, 100),  # Bb7
    (3.5, 64, 100),  # F7
    (3.5, 72, 100),  # F7
    (3.5, 69, 100),  # F7
    (3.5, 65, 100),  # F7
    (4.0, 64, 100),  # Bb7
    (4.0, 71, 100),  # Bb7
    (4.0, 68, 100),  # Bb7
    (4.0, 66, 100),  # Bb7
    (4.5, 64, 100),  # F7
    (4.5, 72, 100),  # F7
    (4.5, 69, 100),  # F7
    (4.5, 65, 100),  # F7
    (5.0, 64, 100),  # Bb7
    (5.0, 71, 100),  # Bb7
    (5.0, 68, 100),  # Bb7
    (5.0, 66, 100)   # Bb7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
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
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax: Melody in Fm, one short motif, make it sing, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 64, 100),  # F
    (1.75, 67, 100), # A
    (2.0, 64, 100),  # F
    (2.25, 62, 100), # D
    (2.5, 64, 100),  # F
    (2.75, 67, 100), # A
    (3.0, 64, 100),  # F
    (3.25, 62, 100), # D
    (3.5, 64, 100),  # F
    (3.75, 67, 100), # A
    (4.0, 64, 100),  # F
    (4.25, 62, 100), # D
    (4.5, 64, 100),  # F
    (4.75, 67, 100), # A
    (5.0, 64, 100),  # F
    (5.25, 62, 100), # D
    (5.5, 64, 100),  # F
    (5.75, 67, 100), # A
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
