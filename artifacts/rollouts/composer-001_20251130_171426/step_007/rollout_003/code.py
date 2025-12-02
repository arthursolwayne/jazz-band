
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
    (0.75, 42, 100), # Hihat on 2
    (1.0, 38, 100),  # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 64, 100),  # F
    (1.875, 65, 100), # Gb
    (2.25, 65, 100),  # Gb
    (2.625, 64, 100), # F
    (3.0, 64, 100),   # F
    (3.375, 65, 100), # Gb
    (3.75, 66, 100),  # Ab
    (4.125, 65, 100), # Gb
    (4.5, 64, 100),   # F
    (4.875, 63, 100), # Eb
    (5.25, 63, 100),  # Eb
    (5.625, 64, 100)  # F
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (2.25, 64, 100),  # F
    (2.25, 69, 100),  # Bb
    (2.25, 71, 100),  # D
    (2.25, 72, 100),  # Eb
    # Bar 3: Bb7 on beat 2
    (3.75, 71, 100),  # Bb
    (3.75, 74, 100),  # D
    (3.75, 76, 100),  # F
    (3.75, 77, 100),  # G
    # Bar 4: Eb7 on beat 2
    (5.25, 69, 100),  # Eb
    (5.25, 72, 100),  # G
    (5.25, 74, 100),  # Bb
    (5.25, 76, 100)   # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, bar_start, bar_start + 0.375))
    # Hihat on 1 & 2
    drums.notes.append(pretty_midi.Note(100, 42, bar_start, bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(100, 38, bar_start + 0.75, bar_start + 0.75 + 0.375))
    # Hihat on 2 & 3
    drums.notes.append(pretty_midi.Note(100, 42, bar_start + 0.75, bar_start + 0.75 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(100, 36, bar_start + 1.5, bar_start + 1.5 + 0.375))
    # Hihat on 3 & 4
    drums.notes.append(pretty_midi.Note(100, 42, bar_start + 1.5, bar_start + 1.5 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(100, 38, bar_start + 2.25, bar_start + 2.25 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(100, 42, bar_start + 2.25, bar_start + 2.25 + 0.375))

# Sax: Motif - start it, leave it hanging, come back and finish it
# Bar 2
sax_notes = [
    (1.5, 69, 100),  # F
    (1.875, 71, 100), # Ab
    (2.25, 69, 100),  # F
    (2.625, 71, 100), # Ab
    (3.0, 69, 100),   # F
    (3.375, 71, 100), # Ab
    (3.75, 74, 100),  # Bb
    (4.125, 71, 100), # Ab
    (4.5, 74, 100),   # Bb
    (4.875, 69, 100), # F
    (5.25, 71, 100),  # Ab
    (5.625, 69, 100)  # F
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('fm_intro.mid')
