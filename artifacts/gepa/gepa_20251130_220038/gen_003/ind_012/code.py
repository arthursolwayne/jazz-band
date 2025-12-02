
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches, no repeated notes

# Fm7 chord: F, Ab, C, Eb
# Bass line: F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> F
bass_notes = [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 76]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4, Fm7 -> Bb7 -> Eb7 -> Am7
# Bar 2: Fm7 (2 and 4)
piano_notes = [76, 88, 80, 83]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.875, end=2.0))

# Bar 3: Bb7 (2 and 4)
piano_notes = [78, 90, 82, 85]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.375, end=3.5))

# Bar 4: Eb7 (2 and 4)
piano_notes = [73, 85, 77, 80]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.875, end=5.0))

# Bar 2: Sax motif starts (1.5 - 3.0s)
# Melody: F, Ab, Bb, C (Fm7), then rest
sax_notes = [76, 88, 80, 83]
for i, note in enumerate(sax_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Bar 3: Sax continues with implied harmony
# Melody: Eb, F, Ab, Bb (Eb7)
sax_notes = [73, 76, 88, 80]
for i, note in enumerate(sax_notes):
    start = 3.0 + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Bar 4: Sax completes motif
# Melody: C, D, Eb, F (Am7 -> Fm7)
sax_notes = [83, 84, 73, 76]
for i, note in enumerate(sax_notes):
    start = 4.5 + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = 1.5 + bar * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))

# Snare on 2 and 4
for bar in range(2, 4):
    start = 1.5 + bar * 1.5
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0))

# Hi-hat on every eighth note
for bar in range(2, 4):
    start = 1.5 + bar * 1.5
    for i in range(0, 4):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
