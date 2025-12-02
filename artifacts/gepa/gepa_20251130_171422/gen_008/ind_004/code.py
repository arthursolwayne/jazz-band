
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Map drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray on drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5

# Kick on 1 and 3
kick_notes = [
    (bar_1_start + 0.0, KICK),
    (bar_1_start + 0.75, KICK)
]

# Snare on 2 and 4
snare_notes = [
    (bar_1_start + 0.375, SNARE),
    (bar_1_start + 1.125, SNARE)
]

# Hi-hat on every eighth
hihat_notes = [
    (bar_1_start + 0.0, HIHAT),
    (bar_1_start + 0.375, HIHAT),
    (bar_1_start + 0.75, HIHAT),
    (bar_1_start + 1.125, HIHAT)
]

# Add to drum instrument
for time, note in kick_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

for time, note in snare_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

for time, note in hihat_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

# Bar 2: Full quartet (1.5 - 3.0s)

bar_2_start = 1.5

# Bass line: walking line in F minor with chromatic approaches
# F - Gb - G - Ab - A - Bb - B - C (chromatic)
# Then back to F on beat 4
# Notes in F minor: F, Gb, A, Bb, C, Db, Eb

bass_notes = [
    (bar_2_start + 0.0, 71),  # F
    (bar_2_start + 0.375, 70),  # Gb
    (bar_2_start + 0.75, 72),  # G
    (bar_2_start + 1.125, 71),  # F (chromatic approach)
    (bar_2_start + 1.5, 74),  # A
    (bar_2_start + 1.875, 73),  # Bb
    (bar_2_start + 2.25, 76),  # C
    (bar_2_start + 2.625, 75),  # Db
    (bar_2_start + 3.0, 71)   # F
]

# Add bass line
for time, pitch in bass_notes:
    note_obj = pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 & 4
# Bar 2: F7 on beat 2, Bb7 on beat 4
# F7 = F A C Eb
# Bb7 = Bb D F Ab

piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_2_start + 0.375, end=bar_2_start + 0.75))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=bar_2_start + 0.375, end=bar_2_start + 0.75))  # A
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_2_start + 0.375, end=bar_2_start + 0.75))  # C
piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_2_start + 0.375, end=bar_2_start + 0.75))  # Eb

# Bb7 on beat 4
piano_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_2_start + 1.125, end=bar_2_start + 1.5))  # Bb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_2_start + 1.125, end=bar_2_start + 1.5))  # D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=bar_2_start + 1.125, end=bar_2_start + 1.5))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=77, start=bar_2_start + 1.125, end=bar_2_start + 1.5))  # Ab

for note in piano_notes:
    piano.notes.append(note)

# Sax: Define a motif in F minor
# Start with a motif: F - Eb - D - C (melodic minor)
# Then a rest, then repeat the motif ending on Bb

motif = [
    (bar_2_start + 0.0, 71),  # F
    (bar_2_start + 0.375, 70),  # Eb
    (bar_2_start + 0.75, 69),  # D
    (bar_2_start + 1.125, 67),  # C
    (bar_2_start + 1.5, 69),  # D (rest for half a beat)
    (bar_2_start + 1.875, 71),  # F
    (bar_2_start + 2.25, 70),  # Eb
    (bar_2_start + 2.625, 71)  # F
]

# Add sax notes
for time, pitch in motif:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

bar_3_start = 3.0

# Bass line: walking line in F minor with chromatic approaches
# F - Gb - G - Ab - A - Bb - B - C (chromatic)
# Then back to F on beat 4

bass_notes = [
    (bar_3_start + 0.0, 71),  # F
    (bar_3_start + 0.375, 70),  # Gb
    (bar_3_start + 0.75, 72),  # G
    (bar_3_start + 1.125, 71),  # F (chromatic approach)
    (bar_3_start + 1.5, 74),  # A
    (bar_3_start + 1.875, 73),  # Bb
    (bar_3_start + 2.25, 76),  # C
    (bar_3_start + 2.625, 75),  # Db
    (bar_3_start + 3.0, 71)   # F
]

# Add bass line
for time, pitch in bass_notes:
    note_obj = pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 & 4
# Bar 3: F7 on beat 2, Bb7 on beat 4

piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_3_start + 0.375, end=bar_3_start + 0.75))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=bar_3_start + 0.375, end=bar_3_start + 0.75))  # A
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_3_start + 0.375, end=bar_3_start + 0.75))  # C
piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_3_start + 0.375, end=bar_3_start + 0.75))  # Eb

# Bb7 on beat 4
piano_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_3_start + 1.125, end=bar_3_start + 1.5))  # Bb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_3_start + 1.125, end=bar_3_start + 1.5))  # D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=bar_3_start + 1.125, end=bar_3_start + 1.5))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=77, start=bar_3_start + 1.125, end=bar_3_start + 1.5))  # Ab

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [
    (bar_3_start + 0.0, KICK),
    (bar_3_start + 0.75, KICK)
]

snare_notes = [
    (bar_3_start + 0.375, SNARE),
    (bar_3_start + 1.125, SNARE)
]

hihat_notes = [
    (bar_3_start + 0.0, HIHAT),
    (bar_3_start + 0.375, HIHAT),
    (bar_3_start + 0.75, HIHAT),
    (bar_3_start + 1.125, HIHAT)
]

# Add to drum instrument
for time, note in kick_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

for time, note in snare_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

for time, note in hihat_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

bar_4_start = 4.5

# Bass line: walking line in F minor with chromatic approaches
# F - Gb - G - Ab - A - Bb - B - C (chromatic)
# Then back to F on beat 4

bass_notes = [
    (bar_4_start + 0.0, 71),  # F
    (bar_4_start + 0.375, 70),  # Gb
    (bar_4_start + 0.75, 72),  # G
    (bar_4_start + 1.125, 71),  # F (chromatic approach)
    (bar_4_start + 1.5, 74),  # A
    (bar_4_start + 1.875, 73),  # Bb
    (bar_4_start + 2.25, 76),  # C
    (bar_4_start + 2.625, 75),  # Db
    (bar_4_start + 3.0, 71)   # F
]

# Add bass line
for time, pitch in bass_notes:
    note_obj = pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 & 4
# Bar 4: F7 on beat 2, Bb7 on beat 4

piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_4_start + 0.375, end=bar_4_start + 0.75))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=bar_4_start + 0.375, end=bar_4_start + 0.75))  # A
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_4_start + 0.375, end=bar_4_start + 0.75))  # C
piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_4_start + 0.375, end=bar_4_start + 0.75))  # Eb

# Bb7 on beat 4
piano_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_4_start + 1.125, end=bar_4_start + 1.5))  # Bb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_4_start + 1.125, end=bar_4_start + 1.5))  # D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=bar_4_start + 1.125, end=bar_4_start + 1.5))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=77, start=bar_4_start + 1.125, end=bar_4_start + 1.5))  # Ab

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [
    (bar_4_start + 0.0, KICK),
    (bar_4_start + 0.75, KICK)
]

snare_notes = [
    (bar_4_start + 0.375, SNARE),
    (bar_4_start + 1.125, SNARE)
]

hihat_notes = [
    (bar_4_start + 0.0, HIHAT),
    (bar_4_start + 0.375, HIHAT),
    (bar_4_start + 0.75, HIHAT),
    (bar_4_start + 1.125, HIHAT)
]

# Add to drum instrument
for time, note in kick_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

for time, note in snare_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

for time, note in hihat_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note_obj)

# Sax: Finish the motif and resolve on Bb
# Motif: F - Eb - D - C (melodic minor) -> rest -> F - Eb - F

motif = [
    (bar_4_start + 0.0, 71),  # F
    (bar_4_start + 0.375, 70),  # Eb
    (bar_4_start + 0.75, 69),  # D
    (bar_4_start + 1.125, 67),  # C
    (bar_4_start + 1.5, 69),  # D (rest for half a beat)
    (bar_4_start + 1.875, 71),  # F
    (bar_4_start + 2.25, 70),  # Eb
    (bar_4_start + 2.625, 69),  # Bb
]

# Add sax notes
for time, pitch in motif:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
