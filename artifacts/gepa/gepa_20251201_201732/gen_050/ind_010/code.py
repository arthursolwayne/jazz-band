
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
drum_notes = [
    (0.0, 36, 100), (0.375, 42, 100), (0.75, 36, 100), (1.125, 42, 100),
    (1.5, 38, 100), (1.875, 42, 100), (2.25, 38, 100), (2.625, 42, 100)
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 53, 80), (1.75, 55, 80), (2.0, 52, 80), (2.25, 53, 80),
    (2.5, 55, 80), (2.75, 57, 80), (3.0, 55, 80), (3.25, 53, 80)
]
for time, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (1.5, 57, 100), (1.5, 62, 100), (1.5, 67, 100), (1.5, 72, 100),  # Fmaj7
    (1.75, 62, 100), (1.75, 67, 100), (1.75, 72, 100), (1.75, 74, 100),  # E7
    (2.0, 57, 100), (2.0, 62, 100), (2.0, 67, 100), (2.0, 72, 100),  # Fmaj7
    (2.5, 65, 100), (2.5, 69, 100), (2.5, 74, 100), (2.5, 78, 100),  # D7
    (2.75, 65, 100), (2.75, 69, 100), (2.75, 74, 100), (2.75, 78, 100)
]
for time, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62, 100), (1.75, 66, 100), (2.0, 62, 100),
    (2.5, 66, 100), (2.75, 71, 100), (3.0, 66, 100)
]
for time, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 53, 80), (3.25, 55, 80), (3.5, 52, 80), (3.75, 53, 80),
    (4.0, 55, 80), (4.25, 57, 80), (4.5, 55, 80), (4.75, 53, 80)
]
for time, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (3.0, 62, 100), (3.0, 67, 100), (3.0, 72, 100), (3.0, 76, 100),  # E7
    (3.25, 62, 100), (3.25, 67, 100), (3.25, 72, 100), (3.25, 76, 100),
    (3.5, 57, 100), (3.5, 62, 100), (3.5, 67, 100), (3.5, 72, 100),  # Fmaj7
    (4.0, 64, 100), (4.0, 68, 100), (4.0, 72, 100), (4.0, 76, 100),  # C7
    (4.25, 64, 100), (4.25, 68, 100), (4.25, 72, 100), (4.25, 76, 100)
]
for time, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: Continue the motif, vary dynamics, leave space
sax_notes = [
    (3.0, 66, 100), (3.25, 69, 100), (3.5, 66, 100), (3.75, 62, 100),
    (4.0, 66, 100), (4.25, 71, 100), (4.5, 66, 100)
]
for time, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100), (4.875, 42, 100), (5.25, 36, 100), (5.625, 42, 100),
    (6.0, 38, 100), (6.375, 42, 100), (6.75, 38, 100), (7.125, 42, 100)
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 53, 80), (4.75, 55, 80), (5.0, 52, 80), (5.25, 53, 80),
    (5.5, 55, 80), (5.75, 57, 80), (6.0, 55, 80), (6.25, 53, 80)
]
for time, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (4.5, 62, 100), (4.5, 67, 100), (4.5, 72, 100), (4.5, 76, 100),  # E7
    (4.75, 62, 100), (4.75, 67, 100), (4.75, 72, 100), (4.75, 76, 100),
    (5.0, 57, 100), (5.0, 62, 100), (5.0, 67, 100), (5.0, 72, 100),  # Fmaj7
    (5.5, 64, 100), (5.5, 68, 100), (5.5, 72, 100), (5.5, 76, 100),  # C7
    (5.75, 64, 100), (5.75, 68, 100), (5.75, 72, 100), (5.75, 76, 100)
]
for time, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: Finish the motif, leave it hanging
sax_notes = [
    (4.5, 66, 100), (4.75, 69, 100), (5.0, 66, 100), (5.25, 62, 100),
    (5.5, 66, 100), (5.75, 71, 100), (6.0, 66, 100)
]
for time, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
