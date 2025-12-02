
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
bass_program = pretty_midi.instrument_name_to_program("Electric Bass (Fingerstyle)")
piano_program = pretty_midi.instrument_name_to_program("Electric Piano")
sax_program = pretty_midi.instrument_name_to_program("Soprano Sax")

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Define time in seconds per quarter note
quarter_note = 60.0 / 160  # 60 seconds per minute / 160 BPM = 0.375 seconds per beat

# Bar 1: Drums only – tension setup
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth

# Bar 1 – 4 beats
for beat in range(4):
    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=beat * quarter_note, end=(beat + 1) * quarter_note)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=90, pitch=62, start=beat * quarter_note, end=(beat + 1) * quarter_note)
        drums.notes.append(note)
    # Hi-hats on every eighth note
    for eighth in range(2):
        note = pretty_midi.Note(velocity=60, pitch=42, start=(beat * 2 + eighth) * quarter_note / 2, 
                               end=(beat * 2 + eighth + 1) * quarter_note / 2)
        drums.notes.append(note)

# Bar 2: All instruments in — sax introduces a motif
# Fm key: F, Ab, Bb, C, Eb

# Bass (walking line)
bass_notes = [64, 62, 60, 59, 57, 55, 53, 52, 50, 48, 47, 45, 43, 42, 40, 39]  # Fm walking line
for i, note in enumerate(bass_notes):
    start = (i % 4) * quarter_note
    end = start + quarter_note
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano (7th chords: F7, Bb7, Eb7, Ab7) on 2 and 4
chords = [
    # Bar 2, beat 1: rest
    # Bar 2, beat 2: F7 (F, A, C, E)
    [64, 68, 69, 71],  # F7
    # Bar 2, beat 3: rest
    # Bar 2, beat 4: Bb7 (Bb, D, F, Ab)
    [61, 64, 66, 68]  # Bb7
]
for i, chord in enumerate(chords):
    for note in chord:
        start = (i + 1) * quarter_note
        end = start + quarter_note
        piano_note = pretty_midi.Note(velocity=85, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)

# Sax: Melodic motif – F, Ab, Bb (question), then resolves in bar 4
motif_notes = [64, 67, 69]  # F, Ab, Bb
for i, note in enumerate(motif_notes):
    start = i * quarter_note
    end = start + quarter_note
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# Bar 3: All instruments continue, sax rests
# Bass continues walking
# Piano continues comping
# No sax in bar 3, leaves the question hanging

# Bar 4: Resolution
# Sax answers the question – Cm7 (C, Eb, G, Bb)
resolution_notes = [72, 74, 76, 77]  # Cm7
for i, note in enumerate(resolution_notes):
    start = i * quarter_note
    end = start + quarter_note
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# Bass continues walking
bass_notes = [72, 70, 68, 67, 65, 63, 61, 60, 58, 56, 55, 53, 51, 50, 48, 47]
for i, note in enumerate(bass_notes):
    start = (i % 4) * quarter_note
    end = start + quarter_note
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: Cm7 chord
piano_notes = [72, 74, 76, 77]  # Cm7
for i, note in enumerate(piano_notes):
    start = i * quarter_note
    end = start + quarter_note
    piano_note = pretty_midi.Note(velocity=85, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

# Drums continue with same pattern
# Bar 3 and 4: same as bar 1
for beat in range(4):
    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(beat + 4) * quarter_note, end=(beat + 5) * quarter_note)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=90, pitch=62, start=(beat + 4) * quarter_note, end=(beat + 5) * quarter_note)
        drums.notes.append(note)
    # Hi-hats on every eighth note
    for eighth in range(2):
        note = pretty_midi.Note(velocity=60, pitch=42, start=(beat * 2 + eighth + 8) * quarter_note / 2, 
                               end=(beat * 2 + eighth + 9) * quarter_note / 2)
        drums.notes.append(note)

# Save MIDI file
pm.write("jazz_intro_fm.mid")
