
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
    (1.5, 36, 100),  # Kick on beat 3
    (2.25, 42, 100), # Hihat on & of 3
    (2.5, 38, 100),  # Snare on beat 4
    (3.0, 36, 100),  # Kick on beat 1 of next bar
    (3.75, 42, 100), # Hihat on & of 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.5, 36, 100),  # Kick on beat 3
    (5.25, 42, 100), # Hihat on & of 3
    (5.5, 38, 100),  # Snare on beat 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62, 100), # D
    (1.75, 61, 100), # C
    (2.0, 63, 100), # Eb
    (2.25, 64, 100), # F
    (2.5, 62, 100), # D
    (2.75, 61, 100), # C
    (3.0, 63, 100), # Eb
    (3.25, 64, 100), # F
    (3.5, 62, 100), # D
    (3.75, 61, 100), # C
    (4.0, 63, 100), # Eb
    (4.25, 64, 100), # F
    (4.5, 62, 100), # D
    (4.75, 61, 100), # C
    (5.0, 63, 100), # Eb
    (5.25, 64, 100), # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 62, 100), # D7: D, F, A, C
    (1.75, 64, 100),
    (1.75, 69, 100),
    (1.75, 67, 100),
    (2.25, 62, 100),
    (2.25, 64, 100),
    (2.25, 69, 100),
    (2.25, 67, 100),
    (3.0, 62, 100),
    (3.0, 64, 100),
    (3.0, 69, 100),
    (3.0, 67, 100),
    (3.75, 62, 100),
    (3.75, 64, 100),
    (3.75, 69, 100),
    (3.75, 67, 100),
    (4.5, 62, 100),
    (4.5, 64, 100),
    (4.5, 69, 100),
    (4.5, 67, 100),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Sax: Motif
sax_notes = [
    (1.5, 62, 100), # D
    (1.75, 64, 100), # F
    (2.0, 62, 100), # D
    (2.25, 64, 100), # F
    (2.5, 62, 100), # D
    (2.75, 65, 100), # G
    (3.0, 62, 100), # D
    (3.25, 64, 100), # F
    (3.5, 65, 100), # G
    (3.75, 67, 100), # Bb
    (4.0, 65, 100), # G
    (4.25, 62, 100), # D
    (4.5, 64, 100), # F
    (4.75, 67, 100), # Bb
    (5.0, 65, 100), # G
    (5.25, 62, 100), # D
    (5.5, 64, 100), # F
    (5.75, 62, 100), # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums in bar 2-4
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (2.25, 42, 100), # Hihat on & of 1
    (2.5, 38, 100),  # Snare on beat 2
    (3.0, 36, 100),  # Kick on beat 3
    (3.75, 42, 100), # Hihat on & of 3
    (4.0, 38, 100),  # Snare on beat 4
    (4.5, 36, 100),  # Kick on beat 1
    (5.25, 42, 100), # Hihat on & of 1
    (5.5, 38, 100),  # Snare on beat 2
    (6.0, 36, 100),  # Kick on beat 3
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
