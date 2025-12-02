
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
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [71, 72, 74, 73, 71, 72, 74, 73, 71, 72, 74, 73, 71, 72, 74, 73]
bass_velocities = [90, 85, 80, 85, 90, 85, 80, 85, 90, 85, 80, 85, 90, 85, 80, 85]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i % 4) * 0.375
    start = time
    end = time + 0.25
    if i % 2 == 0:
        end = time + 0.375
    note_obj = pretty_midi.Note(velocity=bass_velocities[i], pitch=note, start=start, end=end)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    [64, 67, 71, 72],  # F7
    [63, 67, 71, 72],  # E7
    [64, 67, 71, 72],  # F7
    [63, 67, 71, 72],  # E7
]
for bar in range(2, 5):
    for i, chord in enumerate(piano_notes):
        if i % 2 == 0:
            time = 1.5 + (bar - 2) * 1.5 + (i * 0.375)
            for pitch in chord:
                note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
                piano.notes.append(note)

# Sax: One short motif that sings, sparse, expressive
sax_notes = [
    [64, 67, 71, 72],  # F7
    [63, 67, 71, 72],  # E7
    [64, 67, 71],      # Fmaj
    [62, 67, 72, 76],  # D7
]
sax_velocities = [100, 100, 100, 100]
for i, note in enumerate(sax_notes):
    time = 1.5 + (i * 1.5)
    for j, pitch in enumerate(note):
        start = time + (j * 0.25)
        end = start + 0.25
        if i == 0:
            end = start + 0.125
        note_obj = pretty_midi.Note(velocity=sax_velocities[i], pitch=pitch, start=start, end=end)
        sax.notes.append(note_obj)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
