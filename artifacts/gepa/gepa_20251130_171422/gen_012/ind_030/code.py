
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Dm7 chord: D - F - A - C
# Dm scale: D, Eb, F, G, A, Bb, C, D
# We'll use D, F, A, and C as anchor notes

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
bar_duration = 1.5
bar_1_start = 0.0
bar_1_end = bar_1_start + bar_duration

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_1_start, end=bar_1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_1_start + 0.75, end=bar_1_start + 1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_1_start + 0.375, end=bar_1_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_1_start + 1.125, end=bar_1_start + 1.5))

# Hi-hat on every eighth
for i in range(0, 8):
    hihat_start = bar_1_start + i * 0.375
    hihat_end = hihat_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=hihat_start, end=hihat_end))

# Bar 2-4: Full Quartet (1.5 - 6.0s)
bar_2_start = 1.5
bar_3_start = 3.0
bar_4_start = 4.5

# Bass line (Marcus) - walking line, chromatic approaches, Dm7 chord
# Dm7: D, F, A, C
# Walking line: D → Eb → F → G → A → Bb → C → D
# Each note on the downbeat (1, 2, 3, 4), chromatic motion
bass_notes = [
    (bar_2_start, 50, 62),     # D
    (bar_2_start + 0.375, 50, 63),  # Eb
    (bar_2_start + 0.75, 50, 65),   # F
    (bar_2_start + 1.125, 50, 67),  # G
    (bar_2_start + 1.5, 50, 69),    # A
    (bar_2_start + 1.875, 50, 70),  # Bb
    (bar_2_start + 2.25, 50, 71),   # C
    (bar_2_start + 2.625, 50, 69),  # A (chromatic back)
    (bar_2_start + 3.0, 50, 67),    # G
    (bar_2_start + 3.375, 50, 65),  # F
    (bar_2_start + 3.75, 50, 64),   # Eb
    (bar_2_start + 4.125, 50, 62),  # D
    (bar_2_start + 4.5, 50, 60),    # C
    (bar_2_start + 4.875, 50, 62),  # D
    (bar_2_start + 5.25, 50, 64),   # Eb
    (bar_2_start + 5.625, 50, 65),  # F
    (bar_2_start + 6.0, 50, 65),    # F (end of bar 4)
]

for start, vel, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Piano (Diane) - 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# Comp on 2 and 4 with some tension (e.g., Bb or C)
chord_2 = [62, 65, 69, 71]  # Dm7
chord_4 = [62, 65, 69, 70]  # Dm7 with Bb instead of C

# Bar 2: Chord on beat 2
for note in chord_2:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_2_start + 0.375, end=bar_2_start + 0.75))

# Bar 3: Chord on beat 2
for note in chord_2:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_3_start + 0.375, end=bar_3_start + 0.75))

# Bar 4: Chord on beat 2
for note in chord_2:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_4_start + 0.375, end=bar_4_start + 0.75))

# Bar 4: Chord on beat 4 (Dm7 with Bb)
for note in chord_4:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_4_start + 1.125, end=bar_4_start + 1.5))

# Sax (Dante) - Melody: One short motif, make it sing
# Melody in Dm: D → F → A → rest → C → Bb → A → D

sax_notes = [
    (bar_2_start, 96, 62),     # D
    (bar_2_start + 0.375, 96, 65),  # F
    (bar_2_start + 0.75, 96, 69),   # A
    (bar_2_start + 1.125, 96, 69),  # rest (same as A, but sustained)
    (bar_2_start + 1.5, 96, 71),    # C
    (bar_2_start + 1.875, 96, 70),  # Bb
    (bar_2_start + 2.25, 96, 69),   # A
    (bar_2_start + 2.625, 96, 62),  # D
]

for start, vel, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
