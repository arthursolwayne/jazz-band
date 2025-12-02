
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
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 72), (1.875, 71), (2.25, 73), (2.625, 76),
    (3.0, 77), (3.375, 76), (3.75, 74), (4.125, 72),
    (4.5, 71), (4.875, 73), (5.25, 76), (5.625, 77)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    (1.875, 65), (1.875, 69), (1.875, 72), (1.875, 76),  # F7
    # Bar 3 (3.0s)
    (3.375, 65), (3.375, 69), (3.375, 72), (3.375, 76),  # F7
    # Bar 4 (4.5s)
    (4.875, 65), (4.875, 69), (4.875, 72), (4.875, 76)   # F7
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66), (1.875, 69), (2.25, 66), (2.625, 69),
    (3.0, 66), (3.375, 69), (3.75, 66), (4.125, 69),
    (4.5, 66), (4.875, 69), (5.25, 66), (5.625, 69)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    drum_notes = [
        (start_time, 36), (start_time + 0.375, 42), (start_time + 0.75, 38), (start_time + 1.125, 42),
        (start_time + 1.5, 36), (start_time + 1.875, 42), (start_time + 2.25, 38), (start_time + 2.625, 42)
    ]
    for time, note in drum_notes:
        drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
        drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("f_jazz_intro.mid")
