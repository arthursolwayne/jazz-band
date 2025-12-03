
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

# Bar 1
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bar 2: Full band enters (1.5 - 3.0s)

# Marcus: Walking bass line in D, roots and fifths with chromatic approaches
# D2 (D), F#2 (fifth), E2 (chromatic), F#2, G2 (root), A2 (fifth), G#2 (chromatic), A2
bass_notes = [
    (1.5, 38), (1.875, 43), (2.25, 42), (2.625, 43),
    (3.0, 40), (3.375, 45), (3.75, 44), (4.125, 45)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Diane: Open voicings, each bar a different chord, resolving on the last
# Bar 2: D7 (D-F#-A-C#)
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 74),
    # Bar 3: Gm7 (G-Bb-D-F)
    (3.0, 71), (3.0, 76), (3.0, 80), (3.0, 83),
    # Bar 4: C#m7 (C#-E-G-B)
    (4.5, 73), (4.5, 78), (4.5, 82), (4.5, 87)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Dante: One short motif, start it, leave it hanging, come back and finish it
# Starting motif: D (D4), F# (F#4), A (A4), rest on the 4th beat
sax_notes = [
    (1.5, 62), (1.875, 67), (2.25, 72), (2.625, 62),
    # Repeat the motif later in the bar to leave it hanging
    (3.375, 62), (3.75, 67), (4.125, 72), (4.5, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Bar 3: Full band (3.0 - 4.5s)

# Marcus: Walking bass line again
bass_notes = [
    (3.0, 40), (3.375, 45), (3.75, 44), (4.125, 45),
    (4.5, 40), (4.875, 45), (5.25, 44), (5.625, 45)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Diane: Open voicings, each bar a different chord, resolving on the last
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes = [
    (3.0, 71), (3.0, 76), (3.0, 80), (3.0, 83),
    # Bar 4: C#m7 (C#-E-G-B)
    (4.5, 73), (4.5, 78), (4.5, 82), (4.5, 87)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Dante: Continue the motif, leave it hanging, then finish
sax_notes = [
    (3.375, 62), (3.75, 67), (4.125, 72), (4.5, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Bar 4: Full band (4.5 - 6.0s)

# Marcus: Walking bass line again
bass_notes = [
    (4.5, 40), (4.875, 45), (5.25, 44), (5.625, 45)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Diane: Open voicings, each bar a different chord, resolving on the last
# Bar 4: C#m7 (C#-E-G-B)
piano_notes = [
    (4.5, 73), (4.5, 78), (4.5, 82), (4.5, 87)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Dante: Finish the motif
sax_notes = [
    (4.5, 62), (4.875, 67), (5.25, 72), (5.625, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Drums: Bar 4
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
