
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
    (1.0, 38, 100),   # Snare on beat 2
    (1.5, 36, 100),   # Kick on beat 3
    (1.75, 42, 100),  # Hihat on & of 3
    (2.0, 38, 100),   # Snare on beat 4
    (2.25, 42, 100),  # Hihat on & of 4
    (2.5, 42, 100)    # Hihat on beat 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    (1.5, 70, 100),  # D
    (1.75, 69, 100), # C
    (2.0, 68, 100),  # Bb
    (2.25, 70, 100), # D
    (2.5, 71, 100),  # Eb
    (2.75, 70, 100), # D
    (3.0, 69, 100),  # C
    (3.25, 68, 100)  # Bb
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    (2.0, 62, 100),  # D
    (2.0, 65, 100),  # G
    (2.0, 67, 100),  # Bb
    (2.0, 71, 100),  # F
    # Bar 2: Dm7 on beat 4
    (3.0, 62, 100),  # D
    (3.0, 65, 100),  # G
    (3.0, 67, 100),  # Bb
    (3.0, 71, 100),  # F
    # Bar 3: Dm7 on beat 2
    (3.5, 62, 100),  # D
    (3.5, 65, 100),  # G
    (3.5, 67, 100),  # Bb
    (3.5, 71, 100),  # F
    # Bar 3: Dm7 on beat 4
    (4.5, 62, 100),  # D
    (4.5, 65, 100),  # G
    (4.5, 67, 100),  # Bb
    (4.5, 71, 100),  # F
    # Bar 4: Dm7 on beat 2
    (5.0, 62, 100),  # D
    (5.0, 65, 100),  # G
    (5.0, 67, 100),  # Bb
    (5.0, 71, 100),  # F
    # Bar 4: Dm7 on beat 4
    (6.0, 62, 100),  # D
    (6.0, 65, 100),  # G
    (6.0, 67, 100),  # Bb
    (6.0, 71, 100)   # F
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

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
    (5.5, 36, 100),   # Kick on beat 1
    (5.75, 42, 100),  # Hihat on & of 1
    (6.0, 38, 100),   # Snare on beat 2
    (6.25, 42, 100),  # Hihat on & of 2
    (6.5, 36, 100),   # Kick on beat 3
    (6.75, 42, 100),  # Hihat on & of 3
    (7.0, 38, 100),   # Snare on beat 4
    (7.25, 42, 100)   # Hihat on & of 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Dante: Tenor sax motif (1.5 - 3.0s)
# Motif: D (62) -> F (65) -> Bb (67) -> D (62)
# Start on beat 2, leave it hanging on beat 3
sax_notes = [
    (2.0, 62, 100),  # D
    (2.25, 65, 100), # F
    (2.5, 67, 100),  # Bb
    (2.75, 62, 100)  # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Repeat the motif on bar 4 with a twist
sax_notes = [
    (5.0, 62, 100),  # D
    (5.25, 65, 100), # F
    (5.5, 67, 100),  # Bb
    (5.75, 64, 100)  # C
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_introduction.mid")
