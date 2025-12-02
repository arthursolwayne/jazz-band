
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
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on & of 2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, Fm7 -> Bb7 -> Eb7 -> Ab7
bass_notes = [
    (1.5, 60, 100),  # F
    (1.75, 61, 100), # Gb
    (2.0, 59, 100),  # E
    (2.25, 60, 100), # F
    (2.5, 57, 100),  # D
    (2.75, 58, 100), # Eb
    (3.0, 56, 100),  # C
    (3.25, 57, 100), # D
    (3.5, 62, 100),  # G
    (3.75, 63, 100), # Ab
    (4.0, 60, 100),  # F
    (4.25, 61, 100), # Gb
    (4.5, 59, 100),  # E
    (4.75, 60, 100), # F
    (5.0, 57, 100),  # D
    (5.25, 58, 100), # Eb
    (5.5, 56, 100),  # C
    (5.75, 57, 100)  # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (2.0, 60, 100),  # F7
    (2.0, 64, 100),  # Bb
    (2.0, 67, 100),  # D
    (2.0, 71, 100),  # F
    (3.0, 60, 100),  # F7
    (3.0, 64, 100),  # Bb
    (3.0, 67, 100),  # D
    (3.0, 71, 100),  # F
    (4.0, 65, 100),  # Bb7
    (4.0, 69, 100),  # D
    (4.0, 72, 100),  # F
    (4.0, 76, 100),  # Ab
    (5.0, 65, 100),  # Bb7
    (5.0, 69, 100),  # D
    (5.0, 72, 100),  # F
    (5.0, 76, 100)   # Ab
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 100), # Hihat on & of 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.25, 42, 100), # Hihat on & of 2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 100), # Hihat on & of 4
    (3.5, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on & of 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.25, 42, 100), # Hihat on & of 2
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100), # Hihat on & of 3
    (5.0, 38, 100),  # Snare on beat 4
    (5.25, 42, 100)  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
sax_notes = [
    (1.5, 60, 100),  # F
    (1.75, 61, 100), # Gb
    (2.0, 69, 100),  # A
    (2.25, 62, 100), # Bb
    (2.5, 60, 100),  # F
    (2.75, 61, 100), # Gb
    (3.0, 69, 100),  # A
    (3.25, 62, 100), # Bb
    (3.5, 60, 100),  # F
    (3.75, 61, 100), # Gb
    (4.0, 69, 100),  # A
    (4.25, 62, 100), # Bb
    (4.5, 60, 100),  # F
    (4.75, 61, 100), # Gb
    (5.0, 69, 100),  # A
    (5.25, 62, 100)  # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
