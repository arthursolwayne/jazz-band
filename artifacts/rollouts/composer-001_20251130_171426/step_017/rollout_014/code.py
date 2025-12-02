
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
for i in range(4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    for j in range(2):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + j * 0.1875, end=time + j * 0.1875 + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 64), (2.0, 65), (2.25, 67),
    (2.5, 69), (2.75, 71), (3.0, 72), (3.25, 74),
    (3.5, 76), (3.75, 77), (4.0, 79), (4.25, 81),
    (4.5, 83), (4.75, 84), (5.0, 86), (5.25, 88)
]
for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 72), (1.5, 76), (1.5, 74), (1.5, 79),  # D7
    (2.0, 72), (2.0, 76), (2.0, 74), (2.0, 79),  # D7
    (2.5, 72), (2.5, 76), (2.5, 74), (2.5, 79),  # D7
    (3.0, 72), (3.0, 76), (3.0, 74), (3.0, 79),  # D7
    (3.5, 72), (3.5, 76), (3.5, 74), (3.5, 79),  # D7
    (4.0, 72), (4.0, 76), (4.0, 74), (4.0, 79),  # D7
    (4.5, 72), (4.5, 76), (4.5, 74), (4.5, 79),  # D7
    (5.0, 72), (5.0, 76), (5.0, 74), (5.0, 79)   # D7
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62, 0.25), (1.75, 67, 0.25), (2.0, 69, 0.25),  # First phrase
    (2.5, 67, 0.25), (2.75, 62, 0.25), (3.0, 69, 0.25),  # Second phrase
    (3.5, 67, 0.25), (3.75, 62, 0.25), (4.0, 69, 0.25),  # Third phrase
    (4.5, 67, 0.25), (4.75, 62, 0.25), (5.0, 69, 0.25)   # Final phrase
]
for time, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    for j in range(2):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + j * 0.1875, end=time + j * 0.1875 + 0.0625))

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("dante_introduction.mid")
