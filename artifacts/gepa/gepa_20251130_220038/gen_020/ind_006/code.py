
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
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 62), (1.875, 63), (2.25, 60), (2.625, 62),
    # Bar 3
    (3.0, 63), (3.375, 64), (3.75, 62), (4.125, 63),
    # Bar 4
    (4.5, 64), (4.875, 62), (5.25, 63), (5.625, 64)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 70), (1.875, 74), (1.875, 72), (1.875, 77),  # D7
    # Bar 3
    (3.375, 70), (3.375, 74), (3.375, 72), (3.375, 77),  # D7
    # Bar 4
    (4.875, 70), (4.875, 74), (4.875, 72), (4.875, 77)   # D7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Saxophone - motif
sax_notes = [
    # Bar 2 - motif
    (1.5, 65), (1.75, 67), (2.0, 65), (2.25, 64),
    # Bar 4 - return and finish the motif
    (4.5, 65), (4.75, 67), (5.0, 65), (5.25, 64)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_4bar.mid")
