
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
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 59, 100),  # Fm root (F)
    (1.75, 60, 100), # Bb
    (2.0, 61, 100),  # B
    (2.25, 62, 100), # C
    (2.5, 60, 100),  # Bb
    (2.75, 59, 100), # F
    (3.0, 60, 100),  # Bb
    (3.25, 61, 100), # B
    (3.5, 62, 100),  # C
    (3.75, 63, 100), # Db
    (4.0, 62, 100),  # C
    (4.25, 61, 100), # B
    (4.5, 60, 100),  # Bb
    (4.75, 59, 100), # F
    (5.0, 60, 100),  # Bb
    (5.25, 61, 100), # B
    (5.5, 62, 100),  # C
    (5.75, 63, 100)  # Db
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64, 100),  # F7 (F, A, C, Eb)
    (1.5, 69, 100),
    (1.5, 71, 100),
    (1.5, 67, 100),
    (2.0, 64, 100),
    (2.0, 69, 100),
    (2.0, 71, 100),
    (2.0, 67, 100),
    (3.0, 64, 100),
    (3.0, 69, 100),
    (3.0, 71, 100),
    (3.0, 67, 100),
    (4.0, 64, 100),
    (4.0, 69, 100),
    (4.0, 71, 100),
    (4.0, 67, 100)
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    for beat in [0.0, 1.5]:
        drums.notes.append(pretty_midi.Note(100, 36, start + beat, start + beat + 0.25))
    # Snare on 2 and 4
    for beat in [0.75, 2.25]:
        drums.notes.append(pretty_midi.Note(100, 38, start + beat, start + beat + 0.25))
    # Hihat on every eighth
    for beat in [0.0, 0.75, 1.5, 2.25]:
        drums.notes.append(pretty_midi.Note(100, 42, start + beat, start + beat + 0.25))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65, 100),  # F
    (1.75, 67, 100), # G
    (2.0, 64, 100),  # E
    (2.25, 62, 100), # D
    (2.5, 64, 100),  # E
    (2.75, 66, 100), # F#
    (3.0, 65, 100),  # F
    (3.25, 67, 100), # G
    (3.5, 64, 100),  # E
    (3.75, 62, 100), # D
    (4.0, 64, 100),  # E
    (4.25, 62, 100), # D
    (4.5, 64, 100),  # E
    (4.75, 67, 100), # G
    (5.0, 65, 100),  # F
    (5.25, 67, 100), # G
    (5.5, 64, 100),  # E
    (5.75, 62, 100)  # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
