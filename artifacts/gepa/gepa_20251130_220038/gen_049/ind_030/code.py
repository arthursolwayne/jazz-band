
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
    (0.75, 42, 100),  # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100),  # Hihat on & of 2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100),  # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)   # Hihat on & of 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bars 2–4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62, 80),  # D (root)
    (1.75, 60, 80),  # C (chromatic approach)
    (2.0, 64, 80),  # F (3rd)
    (2.25, 62, 80),  # D (root)
    (2.5, 65, 80),  # G (5th)
    (2.75, 64, 80),  # F (3rd)
    (3.0, 67, 80),  # Bb (7th)
    (3.25, 65, 80),  # G (5th)
    (3.5, 69, 80),  # C (chromatic approach)
    (3.75, 67, 80),  # Bb (7th)
    (4.0, 62, 80),  # D (root)
    (4.25, 60, 80),  # C (chromatic approach)
    (4.5, 64, 80),  # F (3rd)
    (4.75, 62, 80),  # D (root)
    (5.0, 65, 80),  # G (5th)
    (5.25, 64, 80),  # F (3rd)
    (5.5, 67, 80),  # Bb (7th)
    (5.75, 65, 80)   # G (5th)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62, 100),  # D
    (1.5, 67, 100),  # Bb
    (1.5, 69, 100),  # C
    (1.5, 71, 100),  # D
    (1.75, 62, 100),  # D
    (1.75, 67, 100),  # Bb
    (1.75, 69, 100),  # C
    (1.75, 71, 100),  # D
    (2.0, 62, 100),  # D
    (2.0, 67, 100),  # Bb
    (2.0, 69, 100),  # C
    (2.0, 71, 100),  # D
    (2.25, 62, 100),  # D
    (2.25, 67, 100),  # Bb
    (2.25, 69, 100),  # C
    (2.25, 71, 100),  # D
    (2.5, 62, 100),  # D
    (2.5, 67, 100),  # Bb
    (2.5, 69, 100),  # C
    (2.5, 71, 100),  # D
    (2.75, 62, 100),  # D
    (2.75, 67, 100),  # Bb
    (2.75, 69, 100),  # C
    (2.75, 71, 100),  # D
    (3.0, 62, 100),  # D
    (3.0, 67, 100),  # Bb
    (3.0, 69, 100),  # C
    (3.0, 71, 100),  # D
    (3.25, 62, 100),  # D
    (3.25, 67, 100),  # Bb
    (3.25, 69, 100),  # C
    (3.25, 71, 100),  # D
    (3.5, 62, 100),  # D
    (3.5, 67, 100),  # Bb
    (3.5, 69, 100),  # C
    (3.5, 71, 100),  # D
    (3.75, 62, 100),  # D
    (3.75, 67, 100),  # Bb
    (3.75, 69, 100),  # C
    (3.75, 71, 100),  # D
    (4.0, 62, 100),  # D
    (4.0, 67, 100),  # Bb
    (4.0, 69, 100),  # C
    (4.0, 71, 100),  # D
    (4.25, 62, 100),  # D
    (4.25, 67, 100),  # Bb
    (4.25, 69, 100),  # C
    (4.25, 71, 100),  # D
    (4.5, 62, 100),  # D
    (4.5, 67, 100),  # Bb
    (4.5, 69, 100),  # C
    (4.5, 71, 100),  # D
    (4.75, 62, 100),  # D
    (4.75, 67, 100),  # Bb
    (4.75, 69, 100),  # C
    (4.75, 71, 100),  # D
    (5.0, 62, 100),  # D
    (5.0, 67, 100),  # Bb
    (5.0, 69, 100),  # C
    (5.0, 71, 100),  # D
    (5.25, 62, 100),  # D
    (5.25, 67, 100),  # Bb
    (5.25, 69, 100),  # C
    (5.25, 71, 100),  # D
    (5.5, 62, 100),  # D
    (5.5, 67, 100),  # Bb
    (5.5, 69, 100),  # C
    (5.5, 71, 100),  # D
    (5.75, 62, 100),  # D
    (5.75, 67, 100),  # Bb
    (5.75, 69, 100),  # C
    (5.75, 71, 100),  # D
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Sax: Tenor solo, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62, 100),  # D
    (1.75, 64, 100),  # F
    (2.0, 62, 100),  # D
    (2.0, 71, 100),  # D (rest on beat 2)
    (2.5, 62, 100),  # D
    (2.75, 64, 100),  # F
    (3.0, 62, 100),  # D
    (3.0, 69, 100),  # C
    (3.25, 67, 100),  # Bb
    (3.5, 62, 100),  # D
    (3.75, 64, 100),  # F
    (4.0, 62, 100),  # D
    (4.0, 69, 100),  # C
    (4.25, 67, 100),  # Bb
    (4.5, 62, 100),  # D
    (4.75, 64, 100),  # F
    (5.0, 62, 100),  # D
    (5.25, 69, 100),  # C
    (5.5, 67, 100),  # Bb
    (5.75, 62, 100)   # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums for bars 2–4
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 100),  # Hihat on & of 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.25, 42, 100),  # Hihat on & of 2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 100),  # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 100),  # Hihat on & of 4
    (3.5, 36, 100),  # Kick on beat 1
    (3.75, 42, 100),  # Hihat on & of 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.25, 42, 100),  # Hihat on & of 2
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100),  # Hihat on & of 3
    (5.0, 38, 100),  # Snare on beat 4
    (5.25, 42, 100),  # Hihat on & of 4
    (5.5, 36, 100),  # Kick on beat 1
    (5.75, 42, 100)   # Hihat on & of 1
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
