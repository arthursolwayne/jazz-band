
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
    start = bar * 1.5
    kick_notes = [36, 36]
    kick_times = [start + 0.0, start + 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)

    snare_notes = [38, 38]
    snare_times = [start + 0.375, start + 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)

    hihat_notes = [42] * 8
    hihat_times = [start + i * 0.375 for i in range(8)]
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    65, 66, 67, 68,  # Bar 2
    68, 69, 70, 69,  # Bar 3
    69, 70, 71, 68,  # Bar 4
]
bass_times = [1.5 + i * 0.375 for i in range(12)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano (Diane) - 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    64, 67, 69, 71,  # F7 (F, A, C, E)
]
piano_times = [1.5 + 0.375] * 4
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Bar 3: Bb7 on beat 2
piano_notes = [
    62, 65, 67, 69,  # Bb7 (Bb, D, F, Ab)
]
piano_times = [1.5 + 0.375 + 1.5] * 4
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Bar 4: E7 on beat 2
piano_notes = [
    60, 64, 65, 69,  # E7 (E, G#, B, D)
]
piano_times = [1.5 + 0.375 + 3.0] * 4
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Drums continue
for bar in range(2, 4):
    start = bar * 1.5
    kick_notes = [36, 36]
    kick_times = [start + 0.0, start + 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)

    snare_notes = [38, 38]
    snare_times = [start + 0.375, start + 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)

    hihat_notes = [42] * 8
    hihat_times = [start + i * 0.375 for i in range(8)]
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

# Saxophone (Dante) - motif in F
# Bar 2: Start the motif
sax_notes = [66, 68, 69, 67]  # F, G, G#, F#
sax_times = [1.5 + 0.0, 1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Repeat the motif
sax_notes = [66, 68, 69, 67]
sax_times = [1.5 + 1.5 + 0.0, 1.5 + 1.5 + 0.375, 1.5 + 1.5 + 0.75, 1.5 + 1.5 + 1.125]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 4: Finish the motif
sax_notes = [66, 68]
sax_times = [1.5 + 3.0 + 0.0, 1.5 + 3.0 + 0.375]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
