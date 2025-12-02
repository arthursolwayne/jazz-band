
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 62), (1.75, 64), (2.0, 65), (2.25, 62),
    (2.5, 60), (2.75, 62), (3.0, 64), (3.25, 65),
    (3.5, 67), (3.75, 69), (4.0, 71), (4.25, 69),
    (4.5, 67), (4.75, 69), (5.0, 71), (5.25, 69)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67), (1.5, 71), (1.5, 69), (1.5, 62),
    (2.0, 67), (2.0, 71), (2.0, 69), (2.0, 62),
    (2.5, 67), (2.5, 71), (2.5, 69), (2.5, 62),
    (3.0, 67), (3.0, 71), (3.0, 69), (3.0, 62),
    (3.5, 67), (3.5, 71), (3.5, 69), (3.5, 62),
    (4.0, 67), (4.0, 71), (4.0, 69), (4.0, 62),
    (4.5, 67), (4.5, 71), (4.5, 69), (4.5, 62),
    (5.0, 67), (5.0, 71), (5.0, 69), (5.0, 62)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.625, 65), (1.75, 62), (1.875, 65),
    (2.0, 62), (2.125, 65), (2.25, 62), (2.375, 65),
    (2.5, 62), (2.625, 65), (2.75, 62), (2.875, 65),
    (3.0, 62)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
