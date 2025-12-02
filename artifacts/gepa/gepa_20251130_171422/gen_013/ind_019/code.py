
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on & of 1
    (1.125, 42, 100), # Hihat on & of 2
    (1.5, 38, 100),  # Snare on beat 3
    (1.75, 42, 100), # Hihat on & of 3
    (2.125, 42, 100), # Hihat on & of 4
    (2.5, 36, 100),  # Kick on beat 4
    (2.75, 42, 100), # Hihat on & of 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 64, 100),  # F
    (1.75, 65, 100),  # Gb
    (2.0, 62, 100),  # Eb
    (2.25, 60, 100),  # D
    (2.5, 62, 100),  # Eb
    (2.75, 64, 100),  # F
    (3.0, 62, 100),  # Eb
    (3.25, 64, 100),  # F
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 64, 100),  # F7 - F
    (1.75, 71, 100),  # A
    (1.75, 69, 100),  # Bb
    (1.75, 76, 100),  # D
    (2.25, 64, 100),  # F7 - F
    (2.25, 71, 100),  # A
    (2.25, 69, 100),  # Bb
    (2.25, 76, 100),  # D
    # Bar 3
    (2.75, 64, 100),  # F7 - F
    (2.75, 71, 100),  # A
    (2.75, 69, 100),  # Bb
    (2.75, 76, 100),  # D
    (3.25, 64, 100),  # F7 - F
    (3.25, 71, 100),  # A
    (3.25, 69, 100),  # Bb
    (3.25, 76, 100),  # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - Eb (Fm7)
sax_notes = [
    # Bar 2
    (1.5, 84, 100),  # F
    (1.75, 87, 100),  # Ab
    (2.0, 86, 100),  # Bb
    (2.25, 81, 100),  # Eb
    # Bar 3
    (2.5, 84, 100),  # F
    (2.75, 87, 100),  # Ab
    (3.0, 86, 100),  # Bb
    (3.25, 81, 100),  # Eb
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (3.0, 62, 100),  # Eb
    (3.25, 64, 100),  # F
    (3.5, 60, 100),  # D
    (3.75, 62, 100),  # Eb
    (4.0, 60, 100),  # D
    (4.25, 62, 100),  # Eb
    (4.5, 64, 100),  # F
    (4.75, 62, 100),  # Eb
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 3
    (3.25, 64, 100),  # F7 - F
    (3.25, 71, 100),  # A
    (3.25, 69, 100),  # Bb
    (3.25, 76, 100),  # D
    (3.75, 64, 100),  # F7 - F
    (3.75, 71, 100),  # A
    (3.75, 69, 100),  # Bb
    (3.75, 76, 100),  # D
    # Bar 4
    (4.25, 64, 100),  # F7 - F
    (4.25, 71, 100),  # A
    (4.25, 69, 100),  # Bb
    (4.25, 76, 100),  # D
    (4.75, 64, 100),  # F7 - F
    (4.75, 71, 100),  # A
    (4.75, 69, 100),  # Bb
    (4.75, 76, 100),  # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.25, 42, 100), # Hihat on & of 1
    (3.5, 42, 100),  # Hihat on & of 2
    (3.75, 38, 100), # Snare on beat 3
    (4.0, 42, 100),  # Hihat on & of 3
    (4.25, 42, 100), # Hihat on & of 4
    (4.5, 36, 100),  # Kick on beat 4
    (4.75, 42, 100), # Hihat on & of 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (4.5, 62, 100),  # Eb
    (4.75, 64, 100),  # F
    (5.0, 60, 100),  # D
    (5.25, 62, 100),  # Eb
    (5.5, 60, 100),  # D
    (5.75, 62, 100),  # Eb
    (6.0, 64, 100),  # F
    (6.25, 62, 100),  # Eb
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 4
    (4.75, 64, 100),  # F7 - F
    (4.75, 71, 100),  # A
    (4.75, 69, 100),  # Bb
    (4.75, 76, 100),  # D
    (5.25, 64, 100),  # F7 - F
    (5.25, 71, 100),  # A
    (5.25, 69, 100),  # Bb
    (5.25, 76, 100),  # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Sax: End the motif, resolve it
sax_notes = [
    # Bar 4
    (4.5, 84, 100),  # F
    (4.75, 87, 100),  # Ab
    (5.0, 86, 100),  # Bb
    (5.25, 81, 100),  # Eb
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on beat 1
    (4.75, 42, 100), # Hihat on & of 1
    (5.0, 42, 100),  # Hihat on & of 2
    (5.25, 38, 100), # Snare on beat 3
    (5.5, 42, 100),  # Hihat on & of 3
    (5.75, 42, 100), # Hihat on & of 4
    (6.0, 36, 100),  # Kick on beat 4
    (6.25, 42, 100), # Hihat on & of 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
