
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_notes = [36, 36]
    kick_times = [start + 0.0, start + 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Snare on 2 and 4
    snare_notes = [38, 38]
    snare_times = [start + 0.375, start + 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Hihat on every eighth
    hihat_notes = [42, 42, 42, 42]
    hihat_times = [start + 0.0, start + 0.375, start + 0.75, start + 1.125]
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches, no repeated notes
bass_notes = [
    60, 61, 62, 64,  # Bar 2
    64, 62, 61, 60,  # Bar 3
    60, 61, 62, 64,  # Bar 4
    64, 62, 61, 60,  # Bar 4
]
bass_times = [1.5 + i * 0.375 for i in range(16)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    64, 67, 71, 72,  # Bar 2 - C7
    64, 67, 71, 72,  # Bar 3 - C7
    64, 67, 71, 72,  # Bar 4 - C7
    64, 67, 71, 72,  # Bar 4 - C7
]
piano_times = [1.5 + i * 0.375 for i in range(16)]
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_notes = [36, 36]
    kick_times = [start + 0.0, start + 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Snare on 2 and 4
    snare_notes = [38, 38]
    snare_times = [start + 0.375, start + 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Hihat on every eighth
    hihat_notes = [42, 42, 42, 42]
    hihat_times = [start + 0.0, start + 0.375, start + 0.75, start + 1.125]
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [62, 64, 62, 60, 62, 64, 62, 60]
sax_times = [1.5 + 0.0, 1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125, 3.0 + 0.0, 3.0 + 0.375, 3.0 + 0.75, 3.0 + 1.125]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
