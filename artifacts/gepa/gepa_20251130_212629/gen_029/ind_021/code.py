
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Time in seconds
bar_length = 1.5
total_time = 6.0

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, kick),
    (0.375, hihat),
    (0.75, kick),
    (1.125, hihat),
    (1.5, snare),
    (1.875, hihat),
    (2.25, kick),
    (2.625, hihat),
    (3.0, snare),
    (3.375, hihat),
    (3.75, kick),
    (4.125, hihat),
    (4.5, snare),
    (4.875, hihat),
    (5.25, kick),
    (5.625, hihat),
    (6.0, snare)
]

for time, note in drum_notes:
    if time <= total_time:
        drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (1.5, 62),  # D
    (1.75, 61),  # C#
    (2.0, 63),   # Eb
    (2.25, 62),  # D
    (2.5, 64),   # F
    (2.75, 63),  # Eb
    (3.0, 62),   # D
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (1.75, 62), (1.75, 67), (1.75, 69), (1.75, 71),  # D7
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),  # D7
    (2.75, 59), (2.75, 64), (2.75, 67), (2.75, 69),  # B7 (subdominant)
    (3.25, 62), (3.25, 67), (3.25, 69), (3.25, 71)   # D7
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax (Dante) - motif that starts, leaves it hanging
sax_notes = [
    (1.5, 65),  # E
    (1.6, 67),  # G
    (1.7, 65),  # E
    (1.75, 62), # D
    (1.9, 64),  # F
    (2.0, 62),  # D
    (2.2, 65),  # E
    (2.25, 67), # G
    (2.3, 65),  # E
    (2.35, 62), # D
    (2.5, 64),  # F
    (2.6, 62)   # D
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line
bass_notes = [
    (3.0, 62),  # D
    (3.25, 61), # C#
    (3.5, 63),  # Eb
    (3.75, 62), # D
    (4.0, 64),  # F
    (4.25, 63), # Eb
    (4.5, 62),  # D
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano (Diane)
piano_notes = [
    (3.25, 62), (3.25, 67), (3.25, 69), (3.25, 71),  # D7
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),  # D7
    (4.25, 60), (4.25, 65), (4.25, 67), (4.25, 69),  # C7 (subdominant)
    (4.75, 62), (4.75, 67), (4.75, 69), (4.75, 71)   # D7
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax (Dante) - continuation of motif, ends on a question
sax_notes = [
    (3.0, 67),  # G
    (3.1, 65),  # E
    (3.15, 67), # G
    (3.2, 65),  # E
    (3.25, 62), # D
    (3.4, 64),  # F
    (3.5, 62),  # D
    (3.7, 65),  # E
    (3.8, 67),  # G
    (3.85, 65), # E
    (3.9, 62),  # D
    (3.95, 64), # F
    (4.0, 62)   # D
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line
bass_notes = [
    (4.5, 62),  # D
    (4.75, 61), # C#
    (5.0, 63),  # Eb
    (5.25, 62), # D
    (5.5, 64),  # F
    (5.75, 63), # Eb
    (6.0, 62)   # D
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano (Diane)
piano_notes = [
    (4.75, 62), (4.75, 67), (4.75, 69), (4.75, 71),  # D7
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71),  # D7
    (5.75, 59), (5.75, 64), (5.75, 67), (5.75, 69),  # B7 (subdominant)
    (6.25, 62), (6.25, 67), (6.25, 69), (6.25, 71)   # D7
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax (Dante) - end on a question, not a statement
sax_notes = [
    (4.5, 67),  # G
    (4.6, 65),  # E
    (4.65, 67), # G
    (4.7, 65),  # E
    (4.75, 62), # D
    (4.9, 64),  # F
    (5.0, 62),  # D
    (5.2, 65),  # E
    (5.3, 67),  # G
    (5.35, 65), # E
    (5.4, 62),  # D
    (5.45, 64), # F
    (5.5, 62)   # D
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(sax_note)

# Add drum fills in bar 4
drum_notes = [
    (4.5, kick),
    (4.875, hihat),
    (5.25, kick),
    (5.625, hihat),
    (6.0, snare)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
