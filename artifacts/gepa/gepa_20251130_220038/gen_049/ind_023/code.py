
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
    (3.0, 36, 100),  # Kick on 1 (next bar)
]

for time, note, velocity in drum_notes:
    if time < 1.5:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62, 100), # D
    (1.75, 60, 100), # C
    (2.0, 63, 100), # Eb
    (2.25, 62, 100), # D
    (2.5, 65, 100), # F
    (2.75, 63, 100), # Eb
    (3.0, 62, 100), # D
    (3.25, 60, 100), # C
    (3.5, 63, 100), # Eb
    (3.75, 62, 100), # D
    (4.0, 65, 100), # F
    (4.25, 63, 100), # Eb
    (4.5, 62, 100), # D
    (4.75, 60, 100), # C
    (5.0, 63, 100), # Eb
    (5.25, 62, 100), # D
    (5.5, 65, 100), # F
    (5.75, 63, 100), # Eb
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62, 100), # D7: D, F#, A, C
    (1.75, 67, 100), # A
    (1.75, 64, 100), # F#
    (1.75, 60, 100), # C
    (2.25, 62, 100), # D7
    (2.25, 67, 100), # A
    (2.25, 64, 100), # F#
    (2.25, 60, 100), # C
    (2.75, 62, 100), # D7
    (2.75, 67, 100), # A
    (2.75, 64, 100), # F#
    (2.75, 60, 100), # C
    (3.25, 62, 100), # D7
    (3.25, 64, 100), # F#
    (3.25, 60, 100), # C
    (3.25, 67, 100), # A
    (3.75, 62, 100), # D7
    (3.75, 64, 100), # F#
    (3.75, 60, 100), # C
    (3.75, 67, 100), # A
    (4.25, 62, 100), # D7
    (4.25, 64, 100), # F#
    (4.25, 60, 100), # C
    (4.25, 67, 100), # A
    (4.75, 62, 100), # D7
    (4.75, 64, 100), # F#
    (4.75, 60, 100), # C
    (4.75, 67, 100), # A
    (5.25, 62, 100), # D7
    (5.25, 64, 100), # F#
    (5.25, 60, 100), # C
    (5.25, 67, 100), # A
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 38, 100), # Snare on 2
    (1.875, 42, 100), # Hihat on &2
    (2.0, 42, 100), # Hihat on 3
    (2.25, 36, 100), # Kick on 3
    (2.5, 38, 100), # Snare on 4
    (2.625, 42, 100), # Hihat on &4
    (2.75, 42, 100), # Hihat on 1
    (3.0, 36, 100), # Kick on 1
    (3.25, 38, 100), # Snare on 2
    (3.375, 42, 100), # Hihat on &2
    (3.5, 42, 100), # Hihat on 3
    (3.75, 36, 100), # Kick on 3
    (4.0, 38, 100), # Snare on 4
    (4.125, 42, 100), # Hihat on &4
    (4.25, 42, 100), # Hihat on 1
    (4.5, 36, 100), # Kick on 1
    (4.75, 38, 100), # Snare on 2
    (4.875, 42, 100), # Hihat on &2
    (5.0, 42, 100), # Hihat on 3
    (5.25, 36, 100), # Kick on 3
    (5.5, 38, 100), # Snare on 4
    (5.625, 42, 100), # Hihat on &4
    (5.75, 42, 100), # Hihat on 1
]

for time, note, velocity in drum_notes:
    if time >= 1.5 and time <= 6.0:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    (1.5, 62, 100), # D
    (1.75, 64, 100), # F
    (2.0, 65, 100), # G
    (2.25, 62, 100), # D (resolves)
    (2.5, 62, 100), # D (hold)
    (2.75, 64, 100), # F
    (3.0, 65, 100), # G
    (3.25, 62, 100), # D (resolves)
    (3.5, 67, 100), # A (new motif)
    (3.75, 65, 100), # G
    (4.0, 64, 100), # F
    (4.25, 62, 100), # D (resolves)
    (4.5, 62, 100), # D (hold)
    (4.75, 64, 100), # F
    (5.0, 65, 100), # G
    (5.25, 62, 100), # D (resolves)
    (5.5, 67, 100), # A (final note)
    (5.75, 65, 100), # G
    (6.0, 64, 100), # F
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
