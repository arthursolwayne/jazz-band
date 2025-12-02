
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
        note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Hihat on every eighth
    hihat_notes = [42] * 8
    hihat_times = [start + i * 0.375 for i in range(8)]
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2: 1.5 - 3.0s
# Marcus: Walking bass line, chromatic approach to C
bass_notes = [60, 61, 62, 63, 62, 61, 60, 59]
bass_times = [1.5 + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4
# C7 on beat 2, F7 on beat 4
piano_notes = [60, 64, 67, 71,  # C7
               65, 69, 72, 76]  # F7
piano_times = [1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125, 1.5 + 1.5,  # C7
               1.5 + 2.375, 1.5 + 2.75, 1.5 + 3.125, 1.5 + 3.5]  # F7
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
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
        note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Hihat on every eighth
    hihat_notes = [42] * 8
    hihat_times = [start + i * 0.375 for i in range(8)]
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

# Dante: Tenor sax melody (start at bar 2, 1.5s)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C E D Bb (meantone tuning, but notated as C E D Bb)
sax_notes = [60, 64, 62, 60]
sax_times = [1.5 + 0.0, 1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Repeat motif at bar 3 (3.0s)
sax_notes = [60, 64, 62, 60]
sax_times = [3.0 + 0.0, 3.0 + 0.375, 3.0 + 0.75, 3.0 + 1.125]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Final bar (4.5s) - finish the motif
sax_notes = [60]
sax_times = [4.5 + 0.0]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.5)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
