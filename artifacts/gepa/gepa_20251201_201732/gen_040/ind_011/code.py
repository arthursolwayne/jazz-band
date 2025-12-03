
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
drum_notes = [
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    # Time in seconds
    (0.0, 36), (0.1875, 42), (0.375, 36), (0.5625, 42),
    (0.75, 38), (0.9375, 42), (1.125, 38), (1.3125, 42)
]
for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1875)
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 40),
    (3.0, 43), (3.375, 41), (3.75, 43)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    # Bar 2: F7
    (1.5, 65), (1.5, 72), (1.5, 67), (1.5, 69)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 72), (1.75, 76), (1.9375, 72), (2.125, 76)
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.1875)
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 43), (3.375, 41), (3.75, 43), (4.125, 41),
    (4.5, 38), (4.875, 40), (5.25, 38)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: Bar 3: Bm7b5 (B, D, F, A)
piano_notes = [
    # Bar 3: Bm7b5
    (3.0, 71), (3.0, 69), (3.0, 64), (3.0, 67)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    (3.0, 76), (3.25, 72), (3.4375, 76), (3.625, 72)
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.1875)
    sax.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 38), (4.875, 40), (5.25, 38), (5.625, 40),
    (6.0, 43), (6.375, 41), (6.75, 43)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: Bar 4: G7 (G, B, D, F)
piano_notes = [
    # Bar 4: G7
    (4.5, 71), (4.5, 76), (4.5, 69), (4.5, 67)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    (4.5, 72), (4.75, 76), (5.0, 72), (5.25, 76)
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.1875)
    sax.notes.append(note)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (1.5, 36), (1.75, 42), (1.875, 38), (2.0625, 42),
    (2.25, 36), (2.4375, 42), (2.625, 38), (2.8125, 42),

    # Bar 3
    (3.0, 36), (3.25, 42), (3.375, 38), (3.5625, 42),
    (3.75, 36), (3.9375, 42), (4.125, 38), (4.3125, 42),

    # Bar 4
    (4.5, 36), (4.75, 42), (4.875, 38), (5.0625, 42),
    (5.25, 36), (5.4375, 42), (5.625, 38), (5.8125, 42)
]
for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1875)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
