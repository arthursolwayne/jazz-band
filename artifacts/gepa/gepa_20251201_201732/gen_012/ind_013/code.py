
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

kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

# Kick on 1 and 3
kick_times = [0.0, 0.75]
# Snare on 2 and 4
snare_times = [0.375, 1.125]
# Hihat on every eighth note
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5]

for note, time in zip(kick_notes * len(kick_times), kick_times):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

for note, time in zip(snare_notes * len(snare_times), snare_times):
    note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

for note, time in zip(hihat_notes * len(hihat_times), hihat_times):
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Root and fifth with chromatic approach
# Fm: F, C, Bb, Ab

# Bar 2: Fm7 (F, Ab, Bb, D)
bass_notes = [53, 51, 50, 48]  # F, Ab, Bb, D
bass_times = [1.5, 1.625, 1.75, 1.875]
for note, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: Open voicing on Fm7, resolving on the last chord
piano_notes = [[53, 61, 64, 67],  # Fm7
               [53, 61, 64, 68],  # F7
               [53, 61, 64, 67],  # Fm7
               [53, 61, 64, 68]]  # F7
piano_times = [1.5, 2.0, 2.5, 3.0]
for i, notes in enumerate(piano_notes):
    for note in notes:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=piano_times[i], end=piano_times[i] + 0.5)
        piano.notes.append(note_obj)

# Sax: Motif (F, Ab, Bb, G)
sax_notes = [53, 51, 50, 55]
sax_times = [1.5, 1.875, 2.25, 2.625]
for note, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb7 (Bb, D, F, Ab)
bass_notes = [50, 53, 52, 51]
bass_times = [3.0, 3.125, 3.25, 3.375]
for note, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: Open voicings
piano_notes = [[50, 58, 62, 65],  # Bb7
               [50, 58, 62, 66],  # Bb7sus4
               [50, 58, 62, 65],  # Bb7
               [50, 58, 62, 66]]  # Bb7sus4
piano_times = [3.0, 3.5, 4.0, 4.5]
for i, notes in enumerate(piano_notes):
    for note in notes:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=piano_times[i], end=piano_times[i] + 0.5)
        piano.notes.append(note_obj)

# Sax: Motif variation (Bb, D, F, Eb)
sax_notes = [50, 53, 52, 50]
sax_times = [3.0, 3.375, 3.75, 4.125]
for note, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F7 (F, A, C, Eb)
bass_notes = [53, 55, 52, 50]
bass_times = [4.5, 4.625, 4.75, 4.875]
for note, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: Open voicings
piano_notes = [[53, 61, 64, 67],  # F7
               [53, 61, 64, 68],  # F7sus4
               [53, 61, 64, 67],  # F7
               [53, 61, 64, 68]]  # F7sus4
piano_times = [4.5, 5.0, 5.5, 6.0]
for i, notes in enumerate(piano_notes):
    for note in notes:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=piano_times[i], end=piano_times[i] + 0.5)
        piano.notes.append(note_obj)

# Sax: Motif resolution (F, Ab, Bb, G)
sax_notes = [53, 51, 50, 55]
sax_times = [4.5, 4.875, 5.25, 5.625]
for note, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Bar 2, 3, and 4
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_times = [bar_start, bar_start + 0.75]
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    hihat_times = [bar_start + i * 0.375 for i in range(4)]

    for note, time in zip(kick_notes * len(kick_times), kick_times):
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)

    for note, time in zip(snare_notes * len(snare_times), snare_times):
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)

    for note, time in zip(hihat_notes * len(hihat_times), hihat_times):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
