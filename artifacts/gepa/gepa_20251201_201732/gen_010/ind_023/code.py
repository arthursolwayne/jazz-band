
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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm7
bass_notes = [38, 42, 37, 43]
for i, note in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(note_obj)

# Bar 3: G7
bass_notes = [43, 47, 46, 49]
for i, note in enumerate(bass_notes):
    time = 1.5 + 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(note_obj)

# Bar 4: Cm7
bass_notes = [40, 44, 43, 47]
for i, note in enumerate(bass_notes):
    time = 1.5 + 3.0 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(note_obj)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
notes = [50, 53, 57, 60]
for i, note in enumerate(notes):
    time = 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Bar 3: G7 (G B D F)
notes = [55, 59, 62, 57]
for i, note in enumerate(notes):
    time = 1.5 + 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Bar 4: Cm7 (C Eb G Bb)
notes = [60, 63, 67, 65]
for i, note in enumerate(notes):
    time = 1.5 + 3.0 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - Eb - F - D (MIDI 62, 63, 65, 62)
# Play first note on beat 1 of bar 2, then leave it hanging, come back on beat 3 of bar 2

# Bar 2: D (62)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.125)
sax.notes.append(note)

# Bar 2: Eb (63)
note = pretty_midi.Note(velocity=110, pitch=63, start=1.5 + 0.75, end=1.5 + 0.75 + 0.125)
sax.notes.append(note)

# Bar 3: D (62)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 1.5, end=1.5 + 1.5 + 0.125)
sax.notes.append(note)

# Bar 3: F (65)
note = pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 1.5 + 0.75, end=1.5 + 1.5 + 0.75 + 0.125)
sax.notes.append(note)

# Bar 4: D (62)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 3.0, end=1.5 + 3.0 + 0.125)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_moment.mid")
