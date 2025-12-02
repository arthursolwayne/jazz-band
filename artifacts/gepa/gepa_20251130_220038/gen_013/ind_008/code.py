
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
    (1.5, 36, 100),  # Kick on 3
    (2.25, 42, 100), # Hihat on &3
    (2.5, 38, 100),  # Snare on 4
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 62, 100), (1.75, 63, 100), (2.0, 60, 100), (2.25, 62, 100),
    # Bar 3
    (2.5, 64, 100), (2.75, 65, 100), (3.0, 62, 100), (3.25, 64, 100),
    # Bar 4
    (3.5, 65, 100), (3.75, 67, 100), (4.0, 64, 100), (4.25, 65, 100),
    # Final bar wrap
    (4.5, 62, 100), (4.75, 60, 100), (5.0, 62, 100), (5.25, 60, 100)
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    (2.0, 64, 100), (2.0, 67, 100), (2.0, 69, 100), (2.0, 71, 100),
    # Bar 2, beat 4
    (2.5, 64, 100), (2.5, 67, 100), (2.5, 69, 100), (2.5, 71, 100),
    # Bar 3, beat 2
    (3.0, 64, 100), (3.0, 67, 100), (3.0, 69, 100), (3.0, 71, 100),
    # Bar 3, beat 4
    (3.5, 64, 100), (3.5, 67, 100), (3.5, 69, 100), (3.5, 71, 100),
    # Bar 4, beat 2
    (4.0, 64, 100), (4.0, 67, 100), (4.0, 69, 100), (4.0, 71, 100),
    # Bar 4, beat 4
    (4.5, 64, 100), (4.5, 67, 100), (4.5, 69, 100), (4.5, 71, 100),
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick_start = bar_start + 0.0
    snare_start = bar_start + 0.75
    kick_start2 = bar_start + 1.5
    snare_start2 = bar_start + 2.25
    hihat_start = bar_start + 0.0
    hihat_start2 = bar_start + 0.375
    hihat_start3 = bar_start + 0.75
    hihat_start4 = bar_start + 1.125
    hihat_start5 = bar_start + 1.5
    hihat_start6 = bar_start + 1.875
    hihat_start7 = bar_start + 2.25
    hihat_start8 = bar_start + 2.625

    # Kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start2, end=kick_start2 + 0.375))
    # Snare
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start2, end=snare_start2 + 0.375))
    # Hihat
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start2, end=hihat_start2 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start3, end=hihat_start3 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start4, end=hihat_start4 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start5, end=hihat_start5 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start6, end=hihat_start6 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start7, end=hihat_start7 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start8, end=hihat_start8 + 0.1875))

# Dante on sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note of motif (bar 2, beat 1)
    (1.5, 65, 100),  # B
    # Second note (bar 2, beat 2)
    (2.0, 67, 100),  # D
    # Third note (bar 2, beat 3)
    (2.5, 64, 100),  # Bb
    # Fourth note (bar 2, beat 4)
    (3.0, 62, 100),  # G
    # Fifth note (bar 3, beat 1)
    (3.5, 65, 100),  # B
    # Sixth note (bar 3, beat 2)
    (4.0, 67, 100),  # D
    # Seventh note (bar 3, beat 3)
    (4.5, 64, 100),  # Bb
    # Eighth note (bar 3, beat 4)
    (5.0, 62, 100),  # G
    # Ninth note (bar 4, beat 1)
    (5.5, 65, 100),  # B
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
