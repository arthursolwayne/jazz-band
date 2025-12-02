
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

# Marcus: Walking line, chromatic approaches, no repeated notes
# D minor scale: D, Eb, F, G, Ab, Bb, C
# Walking bass line in D minor: D, Eb, F, G, Ab, Bb, C, Db
bass_notes = [62, 63, 65, 67, 68, 70, 72, 71]
for bar in range(2, 5):
    for i, note in enumerate(bass_notes):
        time = bar * 1.5 + i * 0.375
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
        bass.notes.append(note_obj)

# Diane: 7th chords, comp on 2 and 4
# Dm7: D, F, Ab, C
# Dm7 in root position: D, F, Ab, C
# Comp on 2 and 4
chords = [
    [62, 65, 68, 72],  # Dm7
    [62, 65, 68, 72],  # Dm7
    [62, 65, 68, 72],  # Dm7
    [62, 65, 68, 72],  # Dm7
]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            for pitch in chords[bar - 2]:
                note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
                piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, Ab, Bb, C
# Motif: D, Eb, F, G (first bar), then Ab, Bb, C, D (second bar), with a space in between
sax_notes = [
    [62, 63, 65, 67],     # Bar 2
    [68, 70, 72, 62],     # Bar 3
    [63, 65, 67, 68],     # Bar 4
    [70, 72, 62, 63]      # Bar 5 (only first three notes)
]

for bar in range(2, 5):
    for i, note in enumerate(sax_notes[bar - 2]):
        time = bar * 1.5 + i * 0.375
        note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
        sax.notes.append(note_obj)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
