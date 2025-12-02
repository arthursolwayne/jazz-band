
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0.0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        note = pretty_midi.Note(velocity=90, pitch=bass_notes[(bar - 2) * 4 + beat], start=time, end=time + 0.25)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    [60, 64, 67, 71],  # C7
    [62, 66, 69, 73],  # D7
    [64, 68, 71, 75],  # E7
    [65, 69, 72, 76],  # F7
    [67, 71, 74, 78],  # G7
    [69, 73, 76, 80],  # A7
    [71, 75, 78, 82],  # B7
    [72, 76, 79, 83],  # C7
]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            for pitch in piano_notes[(bar - 2) * 4 + beat]:
                note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
                piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C - E - G - Bb (C7 arpeggio), then rest on Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Bb (return)
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0)   # Bb
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
