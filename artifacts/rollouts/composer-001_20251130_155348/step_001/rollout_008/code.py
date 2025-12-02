
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# F7 - F7 - F7 - F7
# F, G, Ab, A, Bb, B, C, Db, D, Eb, E, F
bass_notes = [77, 79, 78, 81, 80, 82, 84, 83, 85, 87, 86, 77]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4
# F7, B7, F7, B7
chords = [
    [77, 82, 84, 87],  # F7
    [79, 84, 87, 91],  # B7
    [77, 82, 84, 87],  # F7
    [79, 84, 87, 91]   # B7
]
for i, chord in enumerate(chords):
    start = 1.5 + (i * 0.75)
    for pitch in chord:
        note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
        piano.notes.append(note_obj)

# Sax: Motif - Start with a short phrase, leave it hanging
# F7 (77, 82, 84, 87) - play F, Ab, Bb, B, end on B (82)
sax_notes = [77, 82, 84, 82]
for i, note in enumerate(sax_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(note_obj)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    for beat in range(4):
        time = 1.5 + (bar * 1.5) + (beat * 0.375)
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
