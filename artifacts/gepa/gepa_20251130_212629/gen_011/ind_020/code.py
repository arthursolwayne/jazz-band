
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
# Note numbers: Kick = 36, Snare = 38, Hi-hat = 42
kick = 36
snare = 38
hihat = 42

# Bar structure: 4 bars = 6.0 seconds, 160 BPM = 0.375s per beat
bar_length = 1.5  # Seconds per bar
beat_length = 0.375  # Seconds per beat

# Bar 1: Drums only
# Kick on 1 & 3, Snare on 2 & 4, Hihat on every eighth
for i in range(0, 4):
    time = i * beat_length
    # Kick on beat 1 and 3
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + beat_length))
    # Snare on beat 2 and 4
    if i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + beat_length))
    # Hi-hat on every eighth
    for j in range(2):
        hihat_time = time + j * beat_length / 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=hihat_time, end=hihat_time + beat_length / 2))

# Bar 2: Sax melody (starts on & of 2)
# Motif: E - G - Bb - D
# Start at 1.5s (bar 2, beat 1)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5 + beat_length / 2, end=1.5 + beat_length / 2 + 0.1),
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + beat_length / 2 + 0.1, end=1.5 + beat_length / 2 + 0.2),
    pretty_midi.Note(velocity=110, pitch=62, start=1.5 + beat_length / 2 + 0.2, end=1.5 + beat_length / 2 + 0.3),
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + beat_length / 2 + 0.3, end=1.5 + beat_length / 2 + 0.4),
]
sax.notes.extend(sax_notes)

# Bar 2: Bass line (D - D# - E - F)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.5 + beat_length),
    pretty_midi.Note(velocity=80, pitch=63, start=1.5 + beat_length, end=1.5 + 2 * beat_length),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5 + 2 * beat_length, end=1.5 + 3 * beat_length),
    pretty_midi.Note(velocity=80, pitch=65, start=1.5 + 3 * beat_length, end=1.5 + 4 * beat_length),
]
bass.notes.extend(bass_notes)

# Bar 2: Piano (Dm7)
# Cmaj7 (C E G B) - but in Dm7, it's D F A C
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + beat_length),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + beat_length),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + beat_length),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + beat_length),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Bass (F - G - G# - A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5 + beat_length, end=1.5 + 2 * beat_length),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 2 * beat_length, end=1.5 + 3 * beat_length),
    pretty_midi.Note(velocity=80, pitch=68, start=1.5 + 3 * beat_length, end=1.5 + 4 * beat_length),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5 + 4 * beat_length, end=1.5 + 5 * beat_length),
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (F7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5 + beat_length, end=1.5 + 2 * beat_length),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.5 + beat_length, end=1.5 + 2 * beat_length),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5 + beat_length, end=1.5 + 2 * beat_length),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=1.5 + beat_length, end=1.5 + 2 * beat_length),  # E
]
piano.notes.extend(piano_notes)

# Bar 4: Bass (A - Bb - B - C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.5 + 2 * beat_length, end=1.5 + 3 * beat_length),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 3 * beat_length, end=1.5 + 4 * beat_length),
    pretty_midi.Note(velocity=80, pitch=68, start=1.5 + 4 * beat_length, end=1.5 + 5 * beat_length),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5 + 5 * beat_length, end=1.5 + 6 * beat_length),
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (Gm7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 2 * beat_length, end=1.5 + 3 * beat_length),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=1.5 + 2 * beat_length, end=1.5 + 3 * beat_length),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.5 + 2 * beat_length, end=1.5 + 3 * beat_length),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=1.5 + 2 * beat_length, end=1.5 + 3 * beat_length),  # F
]
piano.notes.extend(piano_notes)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
