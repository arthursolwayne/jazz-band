
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (Bass) - Walking line, chromatic approaches, never the same note twice.
# C minor key, walking bass line
bass_notes = [
    (1.5, 62),  # C3
    (1.875, 61),  # Bb3 (chromatic approach)
    (2.25, 60),  # Bb3
    (2.625, 59),  # A3
    (3.0, 60),  # Bb3
    (3.375, 62),  # C3
    (3.75, 63),  # C#3 (chromatic approach)
    (4.125, 62),  # C3
    (4.5, 60),  # Bb3
    (4.875, 59),  # A3
    (5.25, 60),  # Bb3
    (5.625, 62),  # C3
    (6.0, 64),  # D3
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Diane (Piano) - 7th chords, comp on 2 and 4
# Cm7 on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (1.875, 60), (1.875, 67), (1.875, 71), (1.875, 72),  # Cm7
    # Bar 3 (2.25 - 3.0s)
    (2.625, 60), (2.625, 67), (2.625, 71), (2.625, 72),  # Cm7
    # Bar 4 (3.0 - 3.75s)
    (3.375, 60), (3.375, 67), (3.375, 71), (3.375, 72),  # Cm7
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# Dante (Sax) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - Eb - D - Bb (Cm scale, but not a scale run)
sax_notes = [
    (1.5, 60), (1.5, 62), (1.5, 61), (1.5, 59),  # C - Eb - D - Bb
    (2.25, 60), (2.25, 62), (2.25, 61), (2.25, 59),  # Repeat
    (3.0, 60), (3.0, 62), (3.0, 61), (3.0, 59),  # Repeat
    (3.75, 60), (3.75, 62), (3.75, 61), (3.75, 59),  # Repeat
    (4.5, 60), (4.5, 62), (4.5, 61), (4.5, 59),  # Repeat
    (5.25, 60), (5.25, 62), (5.25, 61), (5.25, 59),  # Repeat
    (6.0, 60), (6.0, 62), (6.0, 61), (6.0, 59)  # Final resolution
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
