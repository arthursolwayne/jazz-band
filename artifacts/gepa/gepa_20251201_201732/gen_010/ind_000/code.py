
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 43), (2.625, 41), (3.0, 38)  # D2, F2, A2, G2, D2
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 60),
    (1.875, 62), (1.875, 65), (1.875, 67), (1.875, 60),
    (2.25, 62), (2.25, 65), (2.25, 67), (2.25, 60),
    (2.625, 62), (2.625, 65), (2.625, 67), (2.625, 60)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 62), (2.25, 65), (2.5, 62), (2.75, 65), (3.0, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 38), (3.375, 40), (3.75, 43), (4.125, 41), (4.5, 38)  # D2, F2, A2, G2, D2
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: Different chord (Am7)
piano_notes = [
    (3.0, 69), (3.0, 71), (3.0, 74), (3.0, 67),
    (3.375, 69), (3.375, 71), (3.375, 74), (3.375, 67),
    (3.75, 69), (3.75, 71), (3.75, 74), (3.75, 67),
    (4.125, 69), (4.125, 71), (4.125, 74), (4.125, 67)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: Continue motif, resolve
sax_notes = [
    (3.0, 65), (3.25, 62), (3.5, 65), (3.75, 62), (4.0, 65), (4.25, 62), (4.5, 65)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 38), (4.875, 40), (5.25, 43), (5.625, 41), (6.0, 38)  # D2, F2, A2, G2, D2
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: Different chord (Gm7)
piano_notes = [
    (4.5, 67), (4.5, 69), (4.5, 72), (4.5, 65),
    (4.875, 67), (4.875, 69), (4.875, 72), (4.875, 65),
    (5.25, 67), (5.25, 69), (5.25, 72), (5.25, 65),
    (5.625, 67), (5.625, 69), (5.625, 72), (5.625, 65)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: Finish motif, resolve
sax_notes = [
    (4.5, 62), (4.75, 65), (5.0, 62), (5.25, 65), (5.5, 62), (5.75, 65), (6.0, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (3.0, 42), (3.375, 42), (3.75, 42), (4.125, 42), (4.5, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (4.5, 42), (4.875, 42), (5.25, 42), (5.625, 42), (6.0, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
