
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
]

for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm motif starting at 1.5s
sax_notes = [
    (1.5, 62), (1.75, 67), (2.0, 62), (2.25, 65)
]
for start, pitch in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    (1.5, 38), (1.75, 41), (2.0, 43), (2.25, 40),
    (2.5, 38), (2.75, 41), (3.0, 43), (3.25, 40)
]
for start, pitch in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62), (1.5, 64), (1.5, 67), (1.5, 69),
    # Bar 3: Gm7 (G, Bb, D, F) - 2nd bar
    (2.5, 67), (2.5, 69), (2.5, 71), (2.5, 64),
    # Bar 4: Cm7 (C, Eb, G, Bb) - 3rd bar
    (3.5, 60), (3.5, 62), (3.5, 67), (3.5, 69)
]
for start, pitch in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif, leave it hanging
sax_notes = [
    (3.0, 65), (3.25, 62), (3.5, 67), (3.75, 65)
]
for start, pitch in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    (3.0, 38), (3.25, 41), (3.5, 43), (3.75, 40),
    (4.0, 38), (4.25, 41), (4.5, 43), (4.75, 40)
]
for start, pitch in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Cm7 (C, Eb, G, Bb)
    (3.0, 60), (3.0, 62), (3.0, 67), (3.0, 69),
    # Bar 4: Fm7 (F, Ab, C, Eb)
    (4.0, 65), (4.0, 67), (4.0, 69), (4.0, 71)
]
for start, pitch in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    (4.5, 67), (4.75, 62)
]
for start, pitch in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    (4.5, 38), (4.75, 41), (5.0, 43), (5.25, 40),
    (5.5, 38), (5.75, 41), (6.0, 43), (6.25, 40)
]
for start, pitch in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano: Final chord - Bm7 (B, D, F#, A)
piano_notes = [
    (4.5, 62), (4.5, 64), (4.5, 67), (4.5, 69)
]
for start, pitch in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
