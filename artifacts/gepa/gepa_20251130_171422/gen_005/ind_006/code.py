
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_duration = 1.5  # 4/4 at 160 BPM = 1.5s per bar
beat_duration = 0.375  # 160 BPM = 60/160 = 0.375s per beat

# Bar 1: Drums only
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))

# Hi-hat on every eighth
for i in range(8):
    start = i * beat_duration
    end = start + beat_duration
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2 (1.5 - 3.0s): Full ensemble
# SAX: Simple motif starting on Dm (D F A C) - D, F, A, C in 16th notes but spaced
# D (D4), F (F4), A (A4), C (C5) - 16th note values, spaced across the bar

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=2.375, end=2.5),  # C5
]

sax.notes.extend(sax_notes)

# BASS: Chromatic walking line, starting on Dm
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.625),  # D3
    pretty_midi.Note(velocity=85, pitch=63, start=1.625, end=1.75),  # Eb3
    pretty_midi.Note(velocity=85, pitch=64, start=1.75, end=1.875),  # E3
    pretty_midi.Note(velocity=85, pitch=65, start=1.875, end=2.0),  # F3
    pretty_midi.Note(velocity=85, pitch=67, start=2.0, end=2.125),  # G3
    pretty_midi.Note(velocity=85, pitch=69, start=2.125, end=2.25),  # A3
    pretty_midi.Note(velocity=85, pitch=70, start=2.25, end=2.375),  # Bb3
    pretty_midi.Note(velocity=85, pitch=72, start=2.375, end=2.5),  # B3
]

bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4, Dm7 = D F A C
# Comp on beat 2 (1.875s) and 4 (2.5s)
# Use Dm7 (D F A C) and then maybe a G7 or Bb7 on the next bar

# Bar 2, beat 2 (1.875s): Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # C
]

# Bar 2, beat 4 (2.5s): G7 (G B D F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.625),  # F#
])

piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s): Continue the ensemble
# SAX: Repeat the motif, but with variation or a slight shift in rhythm

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=3.875, end=4.0),  # C5
]

sax.notes.extend(sax_notes)

# BASS: Chromatic walking line again, continuing from bar 2
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.125),  # C4
    pretty_midi.Note(velocity=85, pitch=75, start=3.125, end=3.25),  # C#4
    pretty_midi.Note(velocity=85, pitch=76, start=3.25, end=3.375),  # D4
    pretty_midi.Note(velocity=85, pitch=77, start=3.375, end=3.5),  # Eb4
    pretty_midi.Note(velocity=85, pitch=79, start=3.5, end=3.625),  # F4
    pretty_midi.Note(velocity=85, pitch=81, start=3.625, end=3.75),  # G4
    pretty_midi.Note(velocity=85, pitch=82, start=3.75, end=3.875),  # Ab4
    pretty_midi.Note(velocity=85, pitch=84, start=3.875, end=4.0),  # Bb4
]

bass.notes.extend(bass_notes)

# PIANO: Comp on beat 2 and 4 of bar 3 (3.875 and 4.5)
# Use a Bb7 (Bb D F Ab) on beat 4

piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.875, end=4.0),  # F#
]

# Bar 3, beat 4: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.625),  # Bb3
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),  # D3
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # F3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # Ab3
])

piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s): Final bar, resolution and tension
# SAX: End on C (C5) with a slight hold
# BASS: Chromatic line again
# PIANO: Comp on beat 2 (5.375) and 4 (6.0)

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.5),  # C5 (held)
]

sax.notes.extend(sax_notes)

# BASS: Chromatic line
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=86, start=4.5, end=4.625),  # C#4
    pretty_midi.Note(velocity=85, pitch=87, start=4.625, end=4.75),  # D4
    pretty_midi.Note(velocity=85, pitch=88, start=4.75, end=4.875),  # Eb4
    pretty_midi.Note(velocity=85, pitch=89, start=4.875, end=5.0),  # E4
    pretty_midi.Note(velocity=85, pitch=91, start=5.0, end=5.125),  # F#4
    pretty_midi.Note(velocity=85, pitch=93, start=5.125, end=5.25),  # G#4
    pretty_midi.Note(velocity=85, pitch=94, start=5.25, end=5.375),  # A#4
    pretty_midi.Note(velocity=85, pitch=96, start=5.375, end=5.5),  # C5
]

bass.notes.extend(bass_notes)

# PIANO: Comp on beat 2 (5.375) and 4 (6.0)
# Use Dm7 on beat 2 and Cmaj7 on beat 4

piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.375, end=5.5),  # C
]

# Bar 4, beat 4: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.125),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.125),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=6.0, end=6.125),  # G
    pretty_midi.Note(velocity=100, pitch=83, start=6.0, end=6.125),  # B
])

piano.notes.extend(piano_notes)

# Bar 4: Drums again
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))  # Snare on 4

# Add hi-hat on every eighth
for i in range(8):
    start = 4.5 + i * beat_duration
    end = start + beat_duration
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
