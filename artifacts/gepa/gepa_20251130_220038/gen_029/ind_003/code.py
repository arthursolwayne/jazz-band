
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.key_signature_changes = [pretty_midi.KeySignature(-1, 0)]  # F minor
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]  # 160 BPM

# Create instruments
drums = Instrument(program=Program(0), is_drum=True, name='Drums')
bass = Instrument(program=Program(33), name='Bass')
piano = Instrument(program=Program(0), name='Piano')
sax = Instrument(program=Program(64), name='Saxophone')

pm.instruments = [drums, bass, piano, sax]

# Bar 1: Little Ray - Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Start at time 0.0
bar1_start = 0.0
bar1_end = 1.5  # 6 seconds for 4 bars = 1.5 seconds per bar

# Kick on 1 and 3 (beats 0 and 2 in 4/4)
kick1 = Note(36, 100, bar1_start, bar1_start + 0.375)
kick2 = Note(36, 100, bar1_start + 0.75, bar1_start + 0.75 + 0.375)
drums.notes.append(kick1)
drums.notes.append(kick2)

# Snare on 2 and 4 (beats 1 and 3)
snare1 = Note(38, 100, bar1_start + 0.375, bar1_start + 0.375 + 0.125)
snare2 = Note(38, 100, bar1_start + 0.75 + 0.375, bar1_start + 0.75 + 0.375 + 0.125)
drums.notes.append(snare1)
drums.notes.append(snare2)

# Hi-hat on every eighth
for i in range(8):
    note_start = bar1_start + i * 0.1875
    hihat = Note(42, 90, note_start, note_start + 0.0625)
    drums.notes.append(hihat)

# Bar 2: Bass (Marcus) - Walking line in F minor
# F - Gb - Ab - Bb - C - Db - Eb - F
# Chromatic approach, no repeated notes
bass_notes = [
    Note(41, 80, 1.5, 1.5 + 0.25),  # F (41)
    Note(40, 80, 1.75, 1.75 + 0.25),  # Gb (40)
    Note(39, 80, 2.0, 2.0 + 0.25),  # Ab (39)
    Note(38, 80, 2.25, 2.25 + 0.25),  # Bb (38)
    Note(43, 80, 2.5, 2.5 + 0.25),  # C (43)
    Note(42, 80, 2.75, 2.75 + 0.25),  # Db (42)
    Note(41, 80, 3.0, 3.0 + 0.25),  # Eb (41)
    Note(41, 80, 3.25, 3.25 + 0.25),  # F again (41)
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 2: Piano (Diane) - 7th chords on 2 and 4
# Fm7 (F, Ab, C, Eb) on beat 2 (1.75) and beat 4 (3.25)
# Use dynamic variation
# Fm7 = 41 (F), 39 (Ab), 43 (C), 40 (Eb)
# Play chords on beat 2 and 4

# Fm7 on beat 2 (1.75)
piano_notes = [
    Note(41, 80, 1.75, 1.75 + 0.25),  # F
    Note(39, 80, 1.75, 1.75 + 0.25),  # Ab
    Note(43, 80, 1.75, 1.75 + 0.25),  # C
    Note(40, 80, 1.75, 1.75 + 0.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Fm7 on beat 4 (3.25)
piano_notes = [
    Note(41, 80, 3.25, 3.25 + 0.25),  # F
    Note(39, 80, 3.25, 3.25 + 0.25),  # Ab
    Note(43, 80, 3.25, 3.25 + 0.25),  # C
    Note(40, 80, 3.25, 3.25 + 0.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 2: Sax (Dante) - Start the motif
# F (41), Ab (39), Bb (38), rest
sax_notes = [
    Note(41, 105, 1.5, 1.5 + 0.375),  # F
    Note(39, 105, 1.875, 1.875 + 0.375),  # Ab
    Note(38, 105, 2.25, 2.25 + 0.375),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Bass (Marcus) - Walking line, chromatic approaches, no repetition
# F - Gb - A - Bb - B - C - C# - D
bass_notes = [
    Note(41, 80, 3.5, 3.5 + 0.25),  # F
    Note(40, 80, 3.75, 3.75 + 0.25),  # Gb
    Note(42, 80, 4.0, 4.0 + 0.25),  # A
    Note(38, 80, 4.25, 4.25 + 0.25),  # Bb
    Note(43, 80, 4.5, 4.5 + 0.25),  # B
    Note(44, 80, 4.75, 4.75 + 0.25),  # C
    Note(45, 80, 5.0, 5.0 + 0.25),  # C#
    Note(46, 80, 5.25, 5.25 + 0.25),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 3: Piano (Diane) - 7th chords on 2 and 4
# Abm7 (Ab, Bb, Db, Eb) on beat 2 (3.75) and beat 4 (5.25)
piano_notes = [
    Note(39, 80, 3.75, 3.75 + 0.25),  # Ab
    Note(38, 80, 3.75, 3.75 + 0.25),  # Bb
    Note(42, 80, 3.75, 3.75 + 0.25),  # Db
    Note(40, 80, 3.75, 3.75 + 0.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

piano_notes = [
    Note(39, 80, 5.25, 5.25 + 0.25),  # Ab
    Note(38, 80, 5.25, 5.25 + 0.25),  # Bb
    Note(42, 80, 5.25, 5.25 + 0.25),  # Db
    Note(40, 80, 5.25, 5.25 + 0.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Sax (Dante) - Continue the motif with variation
# F (41), Ab (39), Bb (38), Eb (40), rest
sax_notes = [
    Note(39, 105, 3.5, 3.5 + 0.375),  # Ab
    Note(38, 105, 3.875, 3.875 + 0.375),  # Bb
    Note(40, 105, 4.25, 4.25 + 0.375),  # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Bass (Marcus) - Walking line with resolution
# D - Eb - F - Gb - G - Ab - A - Bb
bass_notes = [
    Note(46, 80, 5.5, 5.5 + 0.25),  # D
    Note(41, 80, 5.75, 5.75 + 0.25),  # Eb
    Note(41, 80, 6.0, 6.0 + 0.25),  # F
    Note(40, 80, 6.25, 6.25 + 0.25),  # Gb
    Note(43, 80, 6.5, 6.5 + 0.25),  # G
    Note(39, 80, 6.75, 6.75 + 0.25),  # Ab
    Note(42, 80, 7.0, 7.0 + 0.25),  # A
    Note(38, 80, 7.25, 7.25 + 0.25),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Piano (Diane) - 7th chords on 2 and 4
# Bb7 (Bb, D, F, Ab) on beat 2 (5.75) and beat 4 (7.25)
piano_notes = [
    Note(38, 80, 5.75, 5.75 + 0.25),  # Bb
    Note(43, 80, 5.75, 5.75 + 0.25),  # D
    Note(41, 80, 5.75, 5.75 + 0.25),  # F
    Note(39, 80, 5.75, 5.75 + 0.25),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

piano_notes = [
    Note(38, 80, 7.25, 7.25 + 0.25),  # Bb
    Note(43, 80, 7.25, 7.25 + 0.25),  # D
    Note(41, 80, 7.25, 7.25 + 0.25),  # F
    Note(39, 80, 7.25, 7.25 + 0.25),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Sax (Dante) - Finish the motif
# F (41), Ab (39), Bb (38), rest
sax_notes = [
    Note(41, 105, 5.5, 5.5 + 0.375),  # F
    Note(39, 105, 5.875, 5.875 + 0.375),  # Ab
    Note(38, 105, 6.25, 6.25 + 0.375),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Write the MIDI file
pm.write("4_bar_intro.mid")
print("MIDI file written as '4_bar_intro.mid'")
