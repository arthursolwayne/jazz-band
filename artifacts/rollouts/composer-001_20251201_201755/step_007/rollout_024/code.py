
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
    # Bar 1 (0.0 - 1.5s)
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38)
]

for note_time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_time, end=note_time + 0.125)
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches

# Bar 2: Dm7 -> G7 -> Cmaj7 -> F7
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 38), (1.875, 40), (2.25, 43), (2.625, 41),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 43), (3.375, 45), (3.75, 40), (4.125, 38),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 38), (4.875, 40), (5.25, 43), (5.625, 41)
]

for note_time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_time, end=note_time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Dm7: D, F, A, C
    (1.5, 62), (1.5, 64), (1.5, 67), (1.5, 69),
    # Bar 3 (3.0 - 4.5s) - G7: G, B, D, F
    (3.0, 67), (3.0, 71), (3.0, 69), (3.0, 64),
    # Bar 4 (4.5 - 6.0s) - Cmaj7: C, E, G, B
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71)
]

for note_time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_time, end=note_time + 0.5)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (64), G (67), D (62) -> repeats on bar 4
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62), (1.625, 64), (1.75, 67), (1.875, 62),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62), (4.625, 64), (4.75, 67), (4.875, 62)
]

for note_time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_time, end=note_time + 0.125)
    sax.notes.append(note)

# Drums: Full bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    drum_notes = [
        (bar_start + 0.0, 36), (bar_start + 0.375, 42), (bar_start + 0.75, 36), (bar_start + 1.125, 42),
        (bar_start + 1.5, 38)
    ]
    for note_time, note_number in drum_notes:
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_time, end=note_time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
