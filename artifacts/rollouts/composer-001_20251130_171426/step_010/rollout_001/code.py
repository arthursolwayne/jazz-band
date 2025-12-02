
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

# Add drum notes
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approach
bass_notes = [
    (1.5, 62),  # D
    (1.75, 61),  # C
    (2.0, 63),  # Eb
    (2.25, 62),  # D
    (2.5, 64),  # F
    (2.75, 63),  # Eb
    (3.0, 62),  # D
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (1.75 and 2.75)
# Dm7 = D, F, A, C
d7 = [50, 52, 55, 57]
for pitch in d7:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=1.75, end=2.0)
    piano.notes.append(note)

# F7 = F, A, C, Eb
f7 = [53, 55, 57, 59]
for pitch in f7:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=2.75, end=3.0)
    piano.notes.append(note)

# Sax: Motif
motif = [
    (1.5, 62),  # D
    (1.75, 64),  # F
    (2.0, 62),  # D
    (2.25, 67),  # A
    (2.5, 62),  # D
    (2.75, 64),  # F
    (3.0, 62),  # D
]

for start, pitch in motif:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approach
bass_notes = [
    (3.0, 62),  # D
    (3.25, 61),  # C
    (3.5, 63),  # Eb
    (3.75, 62),  # D
    (4.0, 64),  # F
    (4.25, 63),  # Eb
    (4.5, 62),  # D
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (3.25 and 4.25)
# Dm7 = D, F, A, C
for pitch in d7:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=3.25, end=3.5)
    piano.notes.append(note)

# F7 = F, A, C, Eb
for pitch in f7:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=4.25, end=4.5)
    piano.notes.append(note)

# Sax: Motif repeat
for start, pitch in motif:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + 1.5, end=start + 1.75)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line with chromatic approach
bass_notes = [
    (4.5, 62),  # D
    (4.75, 61),  # C
    (5.0, 63),  # Eb
    (5.25, 62),  # D
    (5.5, 64),  # F
    (5.75, 63),  # Eb
    (6.0, 62),  # D
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (4.75 and 5.75)
# Dm7 = D, F, A, C
for pitch in d7:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=4.75, end=5.0)
    piano.notes.append(note)

# F7 = F, A, C, Eb
for pitch in f7:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=5.75, end=6.0)
    piano.notes.append(note)

# Sax: Motif repeat
for start, pitch in motif:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + 3.0, end=start + 3.25)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
