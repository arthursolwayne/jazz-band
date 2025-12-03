
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 43), (2.625, 41),
    (3.0, 38), (3.375, 40), (3.75, 43), (4.125, 41)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G) - open voicing
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 76),  # Dm7 (F, A, D, G)
    (2.0, 67), (2.0, 72), (2.0, 76)              # comp on 2
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: C7 (E, G, C, E) - open voicing
piano_notes = [
    (2.5, 60), (2.5, 64), (2.5, 69), (2.5, 72),  # C7 (E, G, C, E)
    (3.0, 64), (3.0, 69), (3.0, 72)              # comp on 2
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Bb7 (D, F, Bb, D) - open voicing
piano_notes = [
    (3.5, 57), (3.5, 62), (3.5, 67), (3.5, 72),  # Bb7 (D, F, Bb, D)
    (4.0, 62), (4.0, 67), (4.0, 72)              # comp on 2
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Motif in Dm, one short phrase, sing it, leave it hanging
# Dm motif: D - F - G - D (MIDI 62, 67, 69, 62)
sax_notes = [
    (1.5, 62), (1.75, 67), (2.0, 69), (2.25, 62),
    (3.0, 62), (3.25, 67), (3.5, 69), (3.75, 62),
    (4.5, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
