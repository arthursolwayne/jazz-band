
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 62), (1.875, 63), (2.25, 60), (2.625, 62),
    (3.0, 62), (3.375, 63), (3.75, 60), (4.125, 62),
    (4.5, 62), (4.875, 63), (5.25, 60), (5.625, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 70), (1.5, 72),  # Dm7
    (2.25, 62), (2.25, 67), (2.25, 70), (2.25, 72),  # Dm7
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 72),  # F7
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 72),  # F7
    (4.5, 62), (4.5, 67), (4.5, 70), (4.5, 72),  # Dm7
    (5.25, 62), (5.25, 67), (5.25, 70), (5.25, 72)   # Dm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Sax: Melody - a whisper that becomes a cry
# Dm scale: D, Eb, F, G, A, Bb, C
# Start with restraint, build tension, resolve emotionally

sax_notes = [
    (1.5, 62), (1.875, 65), (2.25, 64), (2.625, 62),  # D -> G -> F -> D
    (3.0, 62), (3.375, 67), (3.75, 69), (4.125, 67),  # D -> Bb -> C -> Bb
    (4.5, 67), (4.875, 65), (5.25, 64), (5.625, 62)   # Bb -> G -> F -> D
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
