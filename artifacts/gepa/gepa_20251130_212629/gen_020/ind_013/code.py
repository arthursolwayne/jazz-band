
import pretty_midi

# Initialize MIDI file with tempo and instruments
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds for 4 bars (160 BPM, 4/4 time)
BAR_DURATION = 1.5
TOTAL_DURATION = BAR_DURATION * 4

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, but with subtle rhythmic tension
# Snare on 2 and 4, with a little syncopation
# Hi-hat on every eighth note, with small timing variations

# Kick: 1 and 3 (with slight tension in the third)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=1.1, end=1.2))

# Snare: 2 and 4, with syncopation
drums.notes.append(pretty_midi.Note(velocity=110, pitch=SNARE, start=0.55, end=0.65))  # Syncopated on beat 2
drums.notes.append(pretty_midi.Note(velocity=110, pitch=SNARE, start=1.95, end=2.05)) # Syncopated on beat 4

# Hi-hat: every eighth note, with slight variations
for i in range(0, 8):
    start = i * 0.125 + 0.01 * (i % 2)  # Add subtle offset on 1st and 3rd eighth notes
    duration = 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5s to 4.5s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
# Walk in Dm7: D F A C E♭ G B♭ D
bass_notes = [62, 64, 67, 69, 67, 69, 71, 69]  # D F A C E♭ G B♭ D
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    duration = 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 & 4, comping with space
# Dm7 = D F A C
# Comping on 2 and 4, with some space and motion
piano_notes = [
    # Bar 2: Dm7 on beat 2
    (62, 1.5 + 0.5, 0.25),  # D
    (64, 1.5 + 0.5, 0.25),  # F
    (67, 1.5 + 0.5, 0.25),  # A
    (69, 1.5 + 0.5, 0.25),  # C
    # Bar 3: Dm7 on beat 2
    (62, 3.0 + 0.5, 0.25),  # D
    (64, 3.0 + 0.5, 0.25),  # F
    (67, 3.0 + 0.5, 0.25),  # A
    (69, 3.0 + 0.5, 0.25),  # C
    # Bar 4: Dm7 on beat 4
    (62, 4.5 + 0.75, 0.25), # D
    (64, 4.5 + 0.75, 0.25), # F
    (67, 4.5 + 0.75, 0.25), # A
    (69, 4.5 + 0.75, 0.25)  # C
]
for pitch, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Sax: Motif — one short, singing motif. Start it, leave it hanging, come back and finish it
# Motif: D - F - A - rest (question mark)
# Repeat, but with a slight variation

# First motif (beat 1 and 2)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.6, end=1.7))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.7, end=1.8))

# Rest for a beat
# Second motif (beat 3 and 4), with variation
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.1, end=2.2))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.2, end=2.3))  # A instead of F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.3, end=2.4))  # C instead of A

# Add the final note on beat 4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.1, end=3.2))  # A again, as a resolution

# Add the quartet to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write("dante_intro.mid")
