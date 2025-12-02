
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes (MIDI note numbers)
kick = 36
snare = 38
hihat = 42

# -- Bar 1 (0.0 - 1.5s): Little Ray on drums alone
# Syncopated, tense, with dynamic velocity

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=85, pitch=snare, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=snare, start=1.875, end=2.0))  # off the bar

# Hi-hat on every eighth note with dynamic variation
hi_hat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
hi_hat_velocities = [95, 90, 97, 88, 95, 90, 97, 88]

for t, v in zip(hi_hat_times, hi_hat_velocities):
    drums.notes.append(pretty_midi.Note(velocity=v, pitch=hihat, start=t, end=t + 0.125))

# -- Bar 2 (1.5 - 3.0s): Full quartet enters

# Bass line - walking with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.625)),  # F (43)
    (pretty_midi.Note(velocity=80, pitch=44, start=1.625, end=1.75)),  # F#
    (pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=1.875)),  # G
    (pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.0)),  # G#
    (pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.125)),  # F#
    (pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.25)),  # F
    (pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375)),  # E
    (pretty_midi.Note(velocity=80, pitch=41, start=2.375, end=2.5)),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2 - chord on beat 2 (F7), beat 4 (Bb7)
piano_notes = [
    (pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875)),  # F (64)
    (pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=1.875)),  # A
    (pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=1.875)),  # Bb
    (pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=1.875)),  # D

    (pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5)),  # Bb (71)
    (pretty_midi.Note(velocity=95, pitch=74, start=2.375, end=2.5)),  # D
    (pretty_midi.Note(velocity=95, pitch=76, start=2.375, end=2.5)),  # F
    (pretty_midi.Note(velocity=95, pitch=78, start=2.375, end=2.5)),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: Simple, haunting motif
# Start on E (60), then D (59), leave it hanging at the end
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75)),  # E
    (pretty_midi.Note(velocity=110, pitch=59, start=1.75, end=2.0)),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# -- Bar 3 (3.0 - 4.5s): Continue the same pattern, but with slight variations

# Bass line: walking with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.125)),  # C
    (pretty_midi.Note(velocity=80, pitch=41, start=3.125, end=3.25)),  # D
    (pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375)),  # E
    (pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.5)),  # F
    (pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=3.625)),  # D
    (pretty_midi.Note(velocity=80, pitch=40, start=3.625, end=3.75)),  # C
    (pretty_midi.Note(velocity=80, pitch=39, start=3.75, end=3.875)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=38, start=3.875, end=4.0)),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875)),  # F
    (pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=3.875)),  # A
    (pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=3.875)),  # Bb
    (pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=3.875)),  # D

    (pretty_midi.Note(velocity=100, pitch=71, start=4.375, end=4.5)),  # Bb
    (pretty_midi.Note(velocity=95, pitch=74, start=4.375, end=4.5)),  # D
    (pretty_midi.Note(velocity=95, pitch=76, start=4.375, end=4.5)),  # F
    (pretty_midi.Note(velocity=95, pitch=78, start=4.375, end=4.5)),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: Repeat motif but with a subtle variation
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25)),  # E
    (pretty_midi.Note(velocity=110, pitch=59, start=3.25, end=3.5)),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# -- Bar 4 (4.5 - 6.0s): End with a resolution, but leave space

# Bass line: walking with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.625)),  # F
    (pretty_midi.Note(velocity=80, pitch=44, start=4.625, end=4.75)),  # F#
    (pretty_midi.Note(velocity=80, pitch=45, start=4.75, end=4.875)),  # G
    (pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.0)),  # G#
    (pretty_midi.Note(velocity=80, pitch=44, start=5.0, end=5.125)),  # F#
    (pretty_midi.Note(velocity=80, pitch=43, start=5.125, end=5.25)),  # F
    (pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375)),  # E
    (pretty_midi.Note(velocity=80, pitch=41, start=5.375, end=5.5)),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875)),  # F
    (pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=4.875)),  # A
    (pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=4.875)),  # Bb
    (pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=4.875)),  # D

    (pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.5)),  # Bb
    (pretty_midi.Note(velocity=95, pitch=74, start=5.375, end=5.5)),  # D
    (pretty_midi.Note(velocity=95, pitch=76, start=5.375, end=5.5)),  # F
    (pretty_midi.Note(velocity=95, pitch=78, start=5.375, end=5.5)),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: End with a held note, leaving space
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=59, start=4.5, end=5.0)),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Same rhythm, but slightly more subdued in the final bar
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=85, pitch=kick, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=kick, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=snare, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=snare, start=6.0, end=6.125))  # off the bar

# Hi-hat on every eighth note with dynamic variation
hi_hat_times = [4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]
hi_hat_velocities = [90, 85, 92, 83, 90, 85, 92, 83]

for t, v in zip(hi_hat_times, hi_hat_velocities):
    drums.notes.append(pretty_midi.Note(velocity=v, pitch=hihat, start=t, end=t + 0.125))

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
