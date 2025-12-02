
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
    (0.0, 36, 100),   # Kick on beat 1
    (0.75, 42, 100),  # Hihat on & of 1
    (1.125, 42, 100), # Hihat on & of 2
    (1.5, 38, 100),   # Snare on beat 3
    (1.75, 42, 100),  # Hihat on & of 3
    (2.125, 42, 100), # Hihat on & of 4
    (2.5, 36, 100),   # Kick on beat 4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 62, 100),  # D
    (1.75, 61, 100), # C
    (2.0, 63, 100),  # Eb
    (2.25, 64, 100), # F
    (2.5, 62, 100),  # D
    (2.75, 61, 100), # C
    (3.0, 63, 100),  # Eb
    (3.25, 64, 100), # F
    (3.5, 62, 100),  # D
    (3.75, 61, 100), # C
    (4.0, 63, 100),  # Eb
    (4.25, 64, 100), # F
    (4.5, 62, 100),  # D
    (4.75, 61, 100), # C
    (5.0, 63, 100),  # Eb
    (5.25, 64, 100), # F
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62, 100),  # D7 (D, F#, A, C)
    (1.75, 64, 100), # F#
    (2.0, 69, 100),  # A
    (2.25, 67, 100), # C
    (2.5, 64, 100),  # F#
    (2.75, 69, 100), # A
    (3.0, 67, 100),  # C
    (3.25, 62, 100), # D
    (3.5, 64, 100),  # F#
    (3.75, 69, 100), # A
    (4.0, 67, 100),  # C
    (4.25, 64, 100), # F#
    (4.5, 69, 100),  # A
    (4.75, 67, 100), # C
    (5.0, 64, 100),  # F#
    (5.25, 69, 100), # A
    (5.5, 67, 100),  # C
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),   # Kick on beat 1
    (1.75, 42, 100),  # Hihat on & of 1
    (2.0, 38, 100),   # Snare on beat 2
    (2.25, 42, 100),  # Hihat on & of 2
    (2.5, 36, 100),   # Kick on beat 3
    (2.75, 42, 100),  # Hihat on & of 3
    (3.0, 38, 100),   # Snare on beat 4
    (3.25, 42, 100),  # Hihat on & of 4
    (3.5, 36, 100),   # Kick on beat 1
    (3.75, 42, 100),  # Hihat on & of 1
    (4.0, 38, 100),   # Snare on beat 2
    (4.25, 42, 100),  # Hihat on & of 2
    (4.5, 36, 100),   # Kick on beat 3
    (4.75, 42, 100),  # Hihat on & of 3
    (5.0, 38, 100),   # Snare on beat 4
    (5.25, 42, 100),  # Hihat on & of 4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 71, 100),  # F (Dm7 chord tone)
    (1.75, 69, 100), # Eb (Dm7 chord tone)
    (2.0, 71, 100),  # F (Dm7 chord tone)
    (2.25, 72, 100), # G (extension)
    (2.5, 71, 100),  # F (Dm7 chord tone)
    (2.75, 69, 100), # Eb (Dm7 chord tone)
    (3.0, 71, 100),  # F (Dm7 chord tone)
    (3.25, 72, 100), # G (extension)
    (3.5, 69, 100),  # Eb (Dm7 chord tone)
    (3.75, 67, 100), # D (tonic)
    (4.0, 69, 100),  # Eb (Dm7 chord tone)
    (4.25, 71, 100), # F (Dm7 chord tone)
    (4.5, 69, 100),  # Eb (Dm7 chord tone)
    (4.75, 67, 100), # D (tonic)
    (5.0, 69, 100),  # Eb (Dm7 chord tone)
    (5.25, 71, 100), # F (Dm7 chord tone)
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_moment.mid")
