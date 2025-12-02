
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
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
# Fm: F, Ab, Bb, Db, Eb
# Walking bass line in Fm
bass_notes = [
    64,  # F
    62,  # Eb
    60,  # Db
    59,  # Bb
    57,  # Ab
    55,  # F
    53,  # Eb
    52,  # Db
    50,  # Bb
    48,  # Ab
    47,  # F
    45,  # Eb
    44,  # Db
    42,  # Bb
    40,  # Ab
    38   # F
]
bass_times = [1.5 + i * 0.375 for i in range(len(bass_notes))]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, C
# Comp on beats 2 and 4
piano_notes = [
    # Bar 2: 2 and 4
    64, 69, 71, 72,  # F7 on beat 2
    64, 69, 71, 72,  # F7 on beat 4
    # Bar 3: 2 and 4
    64, 69, 71, 72,  # F7 on beat 2
    64, 69, 71, 72,  # F7 on beat 4
    # Bar 4: 2 and 4
    64, 69, 71, 72,  # F7 on beat 2
    64, 69, 71, 72   # F7 on beat 4
]
piano_times = [
    1.5 + 0.375, 1.5 + 0.375 + 0.375, 1.5 + 0.375 + 0.75, 1.5 + 0.375 + 0.75 + 0.375,  # Bar 2 beat 2
    1.5 + 0.375 * 3, 1.5 + 0.375 * 3 + 0.375, 1.5 + 0.375 * 3 + 0.75, 1.5 + 0.375 * 3 + 0.75 + 0.375,  # Bar 2 beat 4
    1.5 + 0.375 * 5, 1.5 + 0.375 * 5 + 0.375, 1.5 + 0.375 * 5 + 0.75, 1.5 + 0.375 * 5 + 0.75 + 0.375,  # Bar 3 beat 2
    1.5 + 0.375 * 7, 1.5 + 0.375 * 7 + 0.375, 1.5 + 0.375 * 7 + 0.75, 1.5 + 0.375 * 7 + 0.75 + 0.375,  # Bar 3 beat 4
    1.5 + 0.375 * 9, 1.5 + 0.375 * 9 + 0.375, 1.5 + 0.375 * 9 + 0.75, 1.5 + 0.375 * 9 + 0.75 + 0.375   # Bar 4 beat 2
]
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, B (half step above Bb), then repeat starting from Ab
sax_notes = [
    64,  # F
    62,  # Eb
    60,  # Db
    61,  # B
    62,  # Eb
    60,  # Db
    61,  # B
    64   # F
]
sax_times = [1.5 + i * 0.375 for i in range(len(sax_notes))]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)
# Leave it hanging at the end of bar 2
note_obj = pretty_midi.Note(velocity=110, pitch=60, start=1.5 + 2.25, end=1.5 + 2.5)
sax.notes.append(note_obj)
# Come back and finish it in bar 4
note_obj = pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 5.25, end=1.5 + 5.5)
sax.notes.append(note_obj)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = 1.5 + bar * 1.5
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
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
