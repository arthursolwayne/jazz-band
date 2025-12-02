
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75, end=bar1_start + i * 0.75 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(snare_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75 + 0.1875, end=bar1_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(hihat_notes):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.1875)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [62, 63, 65, 67, 69, 71, 72, 71, 69, 67, 65, 63, 62, 60, 58, 57]
bass_durations = [0.375] * len(bass_notes)
for i, pitch in enumerate(bass_notes):
    note_obj = pretty_midi.Note(velocity=80, pitch=pitch, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + bass_durations[i])
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 67, 69, 71),  # D7
    # Bar 3
    (64, 67, 69, 71),  # D7
    # Bar 4
    (64, 67, 69, 71),  # D7
]
for i, chord in enumerate(piano_notes):
    for note in chord:
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=1.5 + i * 1.5 + 0.75, end=1.5 + i * 1.5 + 0.75 + 0.375)
        piano.notes.append(note_obj)

# Sax: One short motif, make it sing
sax_notes = [62, 64, 65, 62]  # D, E, F, D
sax_durations = [0.375, 0.375, 0.375, 0.375]
for i, pitch in enumerate(sax_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + sax_durations[i])
    sax.notes.append(note_obj)

# Drums: Full bar
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar2_start + i * 0.75, end=bar2_start + i * 0.75 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(snare_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar2_start + i * 0.75 + 0.1875, end=bar2_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(hihat_notes):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.1875)
    drums.notes.append(note_obj)

# Bar 3
for i, note in enumerate(kick_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar3_start + i * 0.75, end=bar3_start + i * 0.75 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(snare_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar3_start + i * 0.75 + 0.1875, end=bar3_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(hihat_notes):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.1875)
    drums.notes.append(note_obj)

# Bar 4
for i, note in enumerate(kick_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar4_start + i * 0.75, end=bar4_start + i * 0.75 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(snare_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar4_start + i * 0.75 + 0.1875, end=bar4_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(hihat_notes):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.1875)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
