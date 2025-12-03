
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Acoustic Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, Snare on 2 and 4, Hi-Hat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5

# Kicks on 1 and 3
kick_1 = pretty_midi.Note(velocity=90, pitch=KICK, start=bar_1_start, end=bar_1_start + 0.375)
kick_3 = pretty_midi.Note(velocity=90, pitch=KICK, start=bar_1_start + 0.75, end=bar_1_start + 0.75 + 0.375)

# Snare on 2 and 4
snare_2 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_1_start + 0.375, end=bar_1_start + 0.375 + 0.375)
snare_4 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_1_start + 1.125, end=bar_1_start + 1.125 + 0.375)

# Hi-Hat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=bar_1_start + i * 0.375, end=bar_1_start + i * 0.375 + 0.125)
    for i in range(4)
]

# Add to drum instrument
drums.notes.extend([kick_1, kick_3, snare_2, snare_4] + hihat_notes)
midi.instruments.append(drums)

# Bar 2: Full quartet (1.5 - 3.0s)
bar_2_start = 1.5
bar_2_end = 3.0

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, C, Ab, D, Bb, E, Db
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=53, start=bar_2_start, end=bar_2_start + 0.375),  # F (F3)
    pretty_midi.Note(velocity=70, pitch=58, start=bar_2_start + 0.375, end=bar_2_start + 0.75),  # C (C4)
    pretty_midi.Note(velocity=70, pitch=60, start=bar_2_start + 0.75, end=bar_2_start + 1.125),  # Db (Db4)
    pretty_midi.Note(velocity=70, pitch=57, start=bar_2_start + 1.125, end=bar_2_start + 1.5),  # Bb (Bb4)
]
bass.notes.extend(bass_notes)
midi.instruments.append(bass)

# Piano: Open voicings, resolving on the last bar
# Bar 2: Fm7 (F, Ab, C, Eb) - open voicing
piano_notes_bar2 = [65, 61, 68, 64]  # F4, Ab4, C5, Eb4
for note in piano_notes_bar2:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_2_start, end=bar_2_start + 0.375))

# Bar 3: Bb7 (Bb, D, F, Ab) - open voicing
piano_notes_bar3 = [62, 67, 65, 61]  # Bb4, D4, F4, Ab4
for note in piano_notes_bar3:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_2_start + 0.75, end=bar_2_start + 1.125))

# Bar 4: Eb7 (Eb, G, Bb, Db) - open voicing
piano_notes_bar4 = [64, 69, 62, 60]  # Eb4, G4, Bb4, Db4
for note in piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_2_start + 1.125, end=bar_2_start + 1.5))

midi.instruments.append(piano)

# Sax: Melody in Fm - one short motif, leave it hanging
# Motif: F (F4), Ab (Ab4), Bb (Bb4), G (G4) - played on 1, 2, 3, 4 of bar 2
# Repeat the first note on bar 4 to create a lingering effect
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar_2_start, end=bar_2_start + 0.375),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=bar_2_start + 0.375, end=bar_2_start + 0.75),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=bar_2_start + 0.75, end=bar_2_start + 1.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_2_start + 1.125, end=bar_2_start + 1.5),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=bar_2_start + 1.5, end=bar_2_start + 1.75),  # F4 (repeat)
]
sax.notes.extend(sax_notes)
midi.instruments.append(sax)

# Write MIDI to file
# midi.write disabled
