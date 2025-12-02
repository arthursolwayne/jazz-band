
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
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bar 2: Full quartet starts
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 43), (1.875, 42), (2.25, 44), (2.625, 45),
    (3.0, 47), (3.375, 45), (3.75, 44), (4.125, 43),
    (4.5, 42), (4.875, 43), (5.25, 44), (5.625, 45)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (2.25, 44), (2.25, 50), (2.25, 52), (2.25, 56),
    # Bar 3: Bbm7 on beat 4
    (4.125, 46), (4.125, 53), (4.125, 55), (4.125, 59),
    # Bar 4: Dm7 on beat 2
    (5.25, 45), (5.25, 52), (5.25, 54), (5.25, 57)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Sax: Motif
sax_notes = [
    # Bar 2: Start motif
    (1.5, 62), (1.875, 60), (2.25, 58), (2.625, 60),
    # Bar 3: Leave it hanging
    (3.0, 62), (3.375, 60), (3.75, 57), (4.125, 60),
    # Bar 4: Come back and finish it
    (4.5, 62), (4.875, 60), (5.25, 58), (5.625, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (start + 0.0, 36), (start + 0.375, 42), (start + 0.75, 38), (start + 1.125, 42),
        (start + 1.5, 36), (start + 1.875, 42), (start + 2.25, 38), (start + 2.625, 42)
    ]
    for note_start, note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=note_start, end=note_start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("dante_intro.mid")
