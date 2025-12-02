
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
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8
kick_times = [0.0, 0.75]
snare_times = [0.375, 1.125]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]

for note, time in zip(kick_notes, kick_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

for note, time in zip(snare_notes, snare_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

for note, time in zip(hihat_notes, hihat_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm
bass_notes = [57, 59, 60, 58, 57, 59, 60, 58]  # Fm walk
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (53, 2.25), (57, 2.25), (60, 2.25), (62, 2.25),
    # Bar 3: Bbm7 on beat 4
    (57, 3.75), (60, 3.75), (62, 3.75), (64, 3.75),
    # Bar 4: Eb7 on beat 2
    (58, 4.375), (61, 4.375), (64, 4.375), (66, 4.375)
]
for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax - motif: F (53), Ab (55), Bb (57), Eb (60)
# Play first three notes at 1.5s, leave the last hanging until 4.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 16
kick_times = [1.5, 2.25, 3.0, 3.75]
snare_times = [1.875, 2.625, 3.375, 4.125]
hihat_times = [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125]

for note, time in zip(kick_notes, kick_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

for note, time in zip(snare_notes, snare_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

for note, time in zip(hihat_notes, hihat_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wm_intro.mid")
