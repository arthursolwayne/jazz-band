
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),     # Kick on 1
    (0.375, 42, 100),   # Hihat on 2
    (0.75, 38, 100),    # Snare on 3
    (1.125, 42, 100),   # Hihat on 4
    (1.5, 36, 100)      # Kick on 1 of next bar
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),     # F
    (1.875, 39, 100),   # F#
    (2.25, 40, 100),    # G
    (2.625, 39, 100),   # F#
    (3.0, 41, 100),     # A
    (3.375, 42, 100),   # Bb
    (3.75, 43, 100),    # B
    (4.125, 42, 100),   # Bb
    (4.5, 40, 100),     # G
    (4.875, 39, 100),   # F#
    (5.25, 38, 100),    # F
    (5.625, 39, 100)    # F#
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    (1.5, 62, 100),     # F
    (1.5, 67, 100),     # C
    (1.5, 72, 100),     # F
    (1.5, 77, 100),     # A
    (1.5, 79, 100),     # Bb
    (2.0, 75, 100),     # G
    (2.0, 77, 100),     # A
    (2.0, 79, 100),     # Bb
    (2.0, 81, 100),     # C
    (2.0, 84, 100),     # D
    (2.0, 86, 100),     # E
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.5))

# Bar 3: Bbmaj7
piano_notes = [
    (2.5, 60, 100),     # Bb
    (2.5, 65, 100),     # F
    (2.5, 70, 100),     # Bb
    (2.5, 75, 100),     # D
    (2.5, 77, 100),     # E
    (3.0, 72, 100),     # G
    (3.0, 75, 100),     # D
    (3.0, 77, 100),     # E
    (3.0, 79, 100),     # F
    (3.0, 82, 100),     # A
    (3.0, 84, 100),     # B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.5))

# Bar 4: Dm7
piano_notes = [
    (4.0, 62, 100),     # D
    (4.0, 67, 100),     # F
    (4.0, 72, 100),     # A
    (4.0, 77, 100),     # C
    (4.0, 79, 100),     # D
    (4.5, 65, 100),     # F
    (4.5, 67, 100),     # F
    (4.5, 72, 100),     # A
    (4.5, 77, 100),     # C
    (4.5, 79, 100),     # D
    (4.5, 82, 100),     # E
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.5))

# Sax: One short motif, sing it, leave it hanging
# F (62), Bb (67), G (67), F (62) — the motif
sax_notes = [
    (1.5, 62, 100),     # F
    (1.625, 67, 100),   # Bb
    (1.75, 67, 100),    # G
    (1.875, 62, 100),   # F
    (2.0, 67, 100),     # Leave it hanging
    (2.0, 72, 100),     # Resuming on G
    (2.125, 67, 100),   # Bb
    (2.25, 67, 100),    # G
    (2.375, 62, 100),   # F
    (2.5, 67, 100),     # Leave it hanging
    (2.5, 72, 100),     # Resuming on G
    (2.625, 67, 100),   # Bb
    (2.75, 67, 100),    # G
    (2.875, 62, 100)    # F
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Drums: Fill the bar
drum_notes = [
    (1.5, 36, 100),     # Kick on 1
    (1.875, 42, 100),   # Hihat on 2
    (2.25, 38, 100),    # Snare on 3
    (2.625, 42, 100),   # Hihat on 4
    (3.0, 36, 100),     # Kick on 1
    (3.375, 42, 100),   # Hihat on 2
    (3.75, 38, 100),    # Snare on 3
    (4.125, 42, 100),   # Hihat on 4
    (4.5, 36, 100),     # Kick on 1
    (4.875, 42, 100),   # Hihat on 2
    (5.25, 38, 100),    # Snare on 3
    (5.625, 42, 100)    # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
