
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
    (1.75, 42, 100), # Hihat on &2
    (2.0, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.75, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in D minor
bass_notes = [
    (1.5, 62, 100),  # D
    (1.75, 60, 100), # Bb
    (2.0, 63, 100),  # Eb
    (2.25, 62, 100), # D
    (2.5, 65, 100),  # F
    (2.75, 63, 100), # Eb
    (3.0, 60, 100),  # Bb
    (3.25, 62, 100), # D
    (3.5, 64, 100),  # G
    (3.75, 62, 100), # D
    (4.0, 60, 100),  # Bb
    (4.25, 63, 100), # Eb
    (4.5, 62, 100),  # D
    (4.75, 65, 100), # F
    (5.0, 63, 100),  # Eb
    (5.25, 60, 100), # Bb
    (5.5, 62, 100),  # D
    (5.75, 64, 100), # G
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 62, 100),  # D7 (D, F#, A, C)
    (1.75, 67, 100),
    (1.75, 71, 100),
    (1.75, 64, 100),
    # Bar 3
    (3.25, 62, 100),  # D7
    (3.25, 67, 100),
    (3.25, 71, 100),
    (3.25, 64, 100),
    # Bar 4
    (4.75, 62, 100),  # D7
    (4.75, 67, 100),
    (4.75, 71, 100),
    (4.75, 64, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Dante - Tenor sax - Whisper then cry (D minor)
sax_notes = [
    # Bar 2
    (1.5, 62, 100),  # D
    (1.75, 64, 100), # F
    (2.0, 62, 100),  # D
    (2.25, 69, 100), # A
    # Bar 3
    (2.5, 67, 100),  # Bb
    (2.75, 64, 100), # F
    (3.0, 62, 100),  # D
    (3.25, 69, 100), # A
    # Bar 4
    (3.5, 67, 100),  # Bb
    (3.75, 64, 100), # F
    (4.0, 62, 100),  # D
    (4.25, 69, 100), # A
    (4.5, 67, 100),  # Bb
    (4.75, 64, 100), # F
    (5.0, 62, 100),  # D
    (5.25, 69, 100), # A
    (5.5, 67, 100),  # Bb
    (5.75, 64, 100), # F
    (6.0, 62, 100)   # D
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
