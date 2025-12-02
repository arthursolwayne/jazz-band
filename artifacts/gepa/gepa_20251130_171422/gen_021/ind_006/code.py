
import pretty_midi

# Initialize the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum sounds
KICK = 36
SNARE = 38
HIHAT = 42

# Time divisions
beat = 0.375  # seconds per beat (at 160 BPM, 60/160 = 0.375)
bar = beat * 4  # 1.5 seconds per bar
time = 0.0

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# BAR 1: DRUMS ONLY (0.0 to 1.5s)
# A question in rhythm. Kick on 1 and 3, snare on 2 and 4.
# Hihat on every eighth, but with slight variation and dynamics.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=0.0, end=0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=beat * 2, end=beat * 2 + 0.1))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=beat, end=beat + 0.1))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=beat * 3, end=beat * 3 + 0.1))

# Hi-hat on every eighth, with a slight dynamic variation to keep it alive
hihat_notes = [HIHAT, HIHAT, HIHAT, HIHAT, HIHAT, HIHAT, HIHAT, HIHAT]
hihat_velocities = [100, 95, 100, 95, 100, 95, 100, 95]

for i, vel in enumerate(hihat_velocities):
    hihat_start = i * beat / 2
    hihat_end = hihat_start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=vel, pitch=HIHAT, start=hihat_start, end=hihat_end))

# End of Bar 1
time = bar

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# BAR 2: Full ensemble in Fm (1.5 to 3.0s)

# Trombone-like motif for sax in Fm
# Fm – F, Ab, Bb, Db
# Motif: F (1/4), Ab (1/4), Bb (1/8), rest (1/8)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125), # Bb4
]
sax.notes.extend(sax_notes)

# Marcus on bass: walking line in Fm
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Chromatic approach on the Ab and Bb
bass_notes = [
    # Bar 2: F (1/4), Gb (1/4), Ab (1/4), Bb (1/4)
    pretty_midi.Note(velocity=70, pitch=47, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=70, pitch=48, start=1.75, end=2.0),  # Gb3
    pretty_midi.Note(velocity=70, pitch=50, start=2.0, end=2.25),  # Ab3
    pretty_midi.Note(velocity=70, pitch=51, start=2.25, end=2.5),  # Bb3
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# F7: F, A, C, Eb
# Comp on 2 and 4 (start=1.75, 2.5)
piano_notes = [
    pretty_midi.Note(velocity=75, pitch=53, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=75, pitch=55, start=1.75, end=2.0),  # C5
    pretty_midi.Note(velocity=75, pitch=50, start=1.75, end=2.0),  # Eb4
    pretty_midi.Note(velocity=75, pitch=53, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=75, pitch=55, start=2.5, end=2.75),  # C5
    pretty_midi.Note(velocity=75, pitch=50, start=2.5, end=2.75),  # Eb4
]
piano.notes.extend(piano_notes)

# Drums continue: kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=1.5, end=1.6))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=2.0, end=2.1))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=1.75, end=1.85))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=2.25, end=2.35))

# Hi-hat continues on every eighth
for i in range(8):
    hihat_start = (1.5 + (i * beat / 2))
    hihat_end = hihat_start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=HIHAT, start=hihat_start, end=hihat_end))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# BAR 3: Full ensemble, continue the story (3.0 to 4.5s)

# Sax continues the motif, but now with a twist – space and rest
# F (1/4), Ab (1/4), rest (1/2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5),  # Ab4
]
sax.notes.extend(sax_notes)

# Bass continues with walking line: Bb (1/4), B (1/4), Db (1/4), Eb (1/4)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=51, start=3.0, end=3.25),  # Bb3
    pretty_midi.Note(velocity=70, pitch=52, start=3.25, end=3.5),  # B3
    pretty_midi.Note(velocity=70, pitch=49, start=3.5, end=3.75),  # Db3
    pretty_midi.Note(velocity=70, pitch=50, start=3.75, end=4.0),  # Eb3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (start=3.25, 3.75)
piano_notes = [
    pretty_midi.Note(velocity=75, pitch=53, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=75, pitch=55, start=3.25, end=3.5),  # C5
    pretty_midi.Note(velocity=75, pitch=50, start=3.25, end=3.5),  # Eb4
    pretty_midi.Note(velocity=75, pitch=53, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=75, pitch=55, start=3.75, end=4.0),  # C5
    pretty_midi.Note(velocity=75, pitch=50, start=3.75, end=4.0),  # Eb4
]
piano.notes.extend(piano_notes)

# Drums continue: kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=3.0, end=3.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=3.5, end=3.6))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=3.25, end=3.35))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=3.75, end=3.85))

# Hi-hat continues on every eighth
for i in range(8):
    hihat_start = (3.0 + (i * beat / 2))
    hihat_end = hihat_start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=HIHAT, start=hihat_start, end=hihat_end))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# BAR 4: Full ensemble, resolve the motif (4.5 to 6.0s)

# Sax returns with the motif, now completed – F, Ab, Bb, F
# F (1/4), Ab (1/4), Bb (1/4), F (1/4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F4
]
sax.notes.extend(sax_notes)

# Bass continues walking line: F (1/4), Gb (1/4), Ab (1/4), Bb (1/4)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=47, start=4.5, end=4.75),  # F3
    pretty_midi.Note(velocity=70, pitch=48, start=4.75, end=5.0),  # Gb3
    pretty_midi.Note(velocity=70, pitch=50, start=5.0, end=5.25),  # Ab3
    pretty_midi.Note(velocity=70, pitch=51, start=5.25, end=5.5),  # Bb3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (start=4.75, 5.25)
piano_notes = [
    pretty_midi.Note(velocity=75, pitch=53, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=75, pitch=55, start=4.75, end=5.0),  # C5
    pretty_midi.Note(velocity=75, pitch=50, start=4.75, end=5.0),  # Eb4
    pretty_midi.Note(velocity=75, pitch=53, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=75, pitch=55, start=5.25, end=5.5),  # C5
    pretty_midi.Note(velocity=75, pitch=50, start=5.25, end=5.5),  # Eb4
]
piano.notes.extend(piano_notes)

# Drums continue: kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=4.5, end=4.6))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=5.0, end=5.1))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=4.75, end=4.85))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=5.25, end=5.35))

# Hi-hat continues on every eighth
for i in range(8):
    hihat_start = (4.5 + (i * beat / 2))
    hihat_end = hihat_start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=HIHAT, start=hihat_start, end=hihat_end))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
