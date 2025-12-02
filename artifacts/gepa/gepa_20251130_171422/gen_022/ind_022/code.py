
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds
BAR_DURATION = 1.5
BEAT_DURATION = 0.375

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time grid for bar 1 (1.5s)
for i in range(8):
    time = i * BEAT_DURATION
    if i % 2 == 0:  # Kick on 1 and 3 (0, 2, 4, 6)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1))
    if i % 2 == 1:  # Snare on 2 and 4 (1, 3, 5, 7)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1))
    # Hi-hat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.1))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.5 + 0.375), # Dm7 root
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=1.875 + 0.375), # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.25 + 0.375), # Fm7 root
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=2.625 + 0.375),
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.0 + 0.375), # Dm7 root
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.375 + 0.375), # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=3.75 + 0.375), # Fm7 root
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.125 + 0.375),
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.5 + 0.375), # Dm7 root
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=4.875 + 0.375), # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.25 + 0.375), # Fm7 root
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=5.625 + 0.375),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Dm7 (D F A C), Fm7 (F Ab C Eb), G7 (G B D F), Cm7 (C Eb G Bb)
# 7th chords on 2nd and 4th beats of each bar
piano_notes = []
# Bar 2: Dm7 on beat 2, Fm7 on beat 4
for beat, chord in [(2, [62, 65, 69, 71]), (4, [65, 67, 69, 71])]:
    time = 1.5 + (beat * BEAT_DURATION)
    piano_notes.extend([pretty_midi.Note(velocity=90, pitch=p, start=time, end=time + 0.1) for p in chord])

# Bar 3: G7 on beat 2, Cm7 on beat 4
for beat, chord in [(2, [67, 71, 69, 71]), (4, [60, 64, 67, 69])]:
    time = 1.5 + (beat * BEAT_DURATION) + BAR_DURATION
    piano_notes.extend([pretty_midi.Note(velocity=90, pitch=p, start=time, end=time + 0.1) for p in chord])

# Bar 4: Dm7 on beat 2, Fm7 on beat 4 (reprise)
for beat, chord in [(2, [62, 65, 69, 71]), (4, [65, 67, 69, 71])]:
    time = 1.5 + (beat * BEAT_DURATION) + 2 * BAR_DURATION
    piano_notes.extend([pretty_midi.Note(velocity=90, pitch=p, start=time, end=time + 0.1) for p in chord])

piano.notes.extend(piano_notes)

# Saxophone: motif in Dm
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62) -> G (67) -> A (69) -> D (62)
# Then a rest, then repeat with a slight variation (add a grace note on G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),    # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + 0.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.625 + 0.375), # D
    # Rest until 3.0
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.1),       # Grace note on G
    pretty_midi.Note(velocity=100, pitch=62, start=3.1, end=3.1 + 0.375),     # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.475, end=3.475 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.85, end=3.85 + 0.375),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.225, end=4.225 + 0.375), # D
    # Then rest until the end
]

sax.notes.extend(sax_notes)

# Drums continue in bar 2-4: Same rhythm as bar 1
for i in range(8):
    time = 1.5 + i * BEAT_DURATION
    if i % 2 == 0:  # Kick on 1 and 3 (0, 2, 4, 6)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1))
    if i % 2 == 1:  # Snare on 2 and 4 (1, 3, 5, 7)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1))
    # Hi-hat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.1))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
