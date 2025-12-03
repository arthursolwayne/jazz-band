
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Everyone in
# Drums continue
drum_notes = [
    # Bar 2
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (3.0, 38), (3.25, 40), (3.5, 43), (3.75, 42),
    # Bar 3
    (4.0, 43), (4.25, 41), (4.5, 38), (4.75, 40),
    # Bar 4
    (5.0, 42), (5.25, 43), (5.5, 41), (5.75, 38)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (3.0, 62), (3.0, 65), (3.0, 67), (3.0, 72),
    # Bar 3: G7 (G B D F)
    (4.0, 67), (4.0, 71), (4.0, 72), (4.0, 76),
    # Bar 4: Cm7 (C Eb G Bb)
    (5.0, 60), (5.0, 63), (5.0, 67), (5.0, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F (65) - A (67) - D (62) - C (60) - D (62)
sax_notes = [
    (3.0, 62), (3.25, 65), (3.5, 67), (3.75, 62),
    (4.25, 60), (4.5, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
# midi.write disabled
