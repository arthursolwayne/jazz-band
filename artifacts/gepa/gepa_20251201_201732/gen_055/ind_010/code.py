
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38),     # D2
    (1.875, 40),   # Eb2 (chromatic approach)
    (2.25, 43),    # G2
    (2.625, 38),   # D2
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 76),  # F4, A4, D5, G5
    (1.875, 62), (1.875, 67), (1.875, 72), (1.875, 76),
    (2.25, 62), (2.25, 67), (2.25, 72), (2.25, 76),
    (2.625, 62), (2.625, 67), (2.625, 72), (2.625, 76),
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65), (1.5, 67), (1.5, 69), (1.5, 71),  # D4, E4, F4, G4
    (1.875, 65), (1.875, 67), (1.875, 69), (1.875, 71),
    (2.25, 65), (2.25, 67), (2.25, 69), (2.25, 71),
    (2.625, 65), (2.625, 67), (2.625, 69), (2.625, 71),
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes_bar3 = [
    (3.0, 38),     # D2
    (3.375, 40),   # Eb2 (chromatic approach)
    (3.75, 43),    # G2
    (4.125, 38),   # D2
]
for start, note in bass_notes_bar3:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Cm7 (Eb, G, C, E)
piano_notes_bar3 = [
    (3.0, 64), (3.0, 67), (3.0, 72), (3.0, 76),  # Eb4, G4, C5, E5
    (3.375, 64), (3.375, 67), (3.375, 72), (3.375, 76),
    (3.75, 64), (3.75, 67), (3.75, 72), (3.75, 76),
    (4.125, 64), (4.125, 67), (4.125, 72), (4.125, 76),
]
for start, note in piano_notes_bar3:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes_bar3 = [
    (3.0, 62), (3.0, 64), (3.0, 66), (3.0, 68),  # B3, C4, D4, E4
    (3.375, 62), (3.375, 64), (3.375, 66), (3.375, 68),
    (3.75, 62), (3.75, 64), (3.75, 66), (3.75, 68),
    (4.125, 62), (4.125, 64), (4.125, 66), (4.125, 68),
]
for start, note in sax_notes_bar3:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes_bar4 = [
    (4.5, 38),     # D2
    (4.875, 40),   # Eb2 (chromatic approach)
    (5.25, 43),    # G2
    (5.625, 38),   # D2
]
for start, note in bass_notes_bar4:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Gm7 (Bb, D, G, B)
piano_notes_bar4 = [
    (4.5, 62), (4.5, 67), (4.5, 72), (4.5, 76),  # Bb4, D4, G4, B4
    (4.875, 62), (4.875, 67), (4.875, 72), (4.875, 76),
    (5.25, 62), (5.25, 67), (5.25, 72), (5.25, 76),
    (5.625, 62), (5.625, 67), (5.625, 72), (5.625, 76),
]
for start, note in piano_notes_bar4:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes_bar4 = [
    (4.5, 65), (4.5, 67), (4.5, 69), (4.5, 71),  # D4, E4, F4, G4
    (4.875, 65), (4.875, 67), (4.875, 69), (4.875, 71),
    (5.25, 65), (5.25, 67), (5.25, 69), (5.25, 71),
    (5.625, 65), (5.625, 67), (5.625, 69), (5.625, 71),
]
for start, note in sax_notes_bar4:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
]
for start, note in drum_notes_bar3:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
