
import pretty_midi

# Initialize the MIDI file with 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Initialize the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes (MIDI note numbers)
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1 (0.0 - 1.5s): Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar at 160 BPM

# Drums: Bar 1
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=KICK, start=1.125, end=1.5)
])

# Bar 2 (1.5 - 3.0s): Full quartet
# Sax: Start of the motif (D - F# - B - D)
# Note durations: 0.375s (quarter note), 0.375s (quarter), 0.375s (quarter), 0.375s (quarter)

# D (D4) = MIDI 62
# F# (F#4) = MIDI 66
# B (B4) = MIDI 71
# D (D5) = MIDI 74

sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0)
])

# Bass: Walking chromatic line (D - D# - E - F)
# MIDI: 62 (D), 63 (D#), 64 (E), 65 (F)

bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0)
])

# Piano: 7th chords on offbeats
# Chord: D7 = D, F#, A, C
# Play in 7th chords on beats 2 and 4 (offbeats)

# Offbeat 2 (1.875s)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # C
])

# Offbeat 4 (2.625s)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # C
])

# Drums: Bar 2
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=KICK, start=2.625, end=3.0)
])

# Bar 3 (3.0 - 4.5s): Full quartet
# Sax: Repeat the motif (D - F# - B - D)

sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5)
])

# Bass: Walking chromatic line (D - D# - E - F)

bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5)
])

# Piano: Same chords on offbeats

# Offbeat 2 (3.375s)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # C
])

# Offbeat 4 (4.125s)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # C
])

# Drums: Bar 3
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=KICK, start=4.125, end=4.5)
])

# Bar 4 (4.5 - 6.0s): Full quartet
# Sax: Repeat the motif (D - F# - B - D)

sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0)
])

# Bass: Walking chromatic line (D - D# - E - F)

bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0)
])

# Piano: Same chords on offbeats

# Offbeat 2 (4.875s)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C
])

# Offbeat 4 (5.625s)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # C
])

# Drums: Bar 4
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=KICK, start=5.625, end=6.0)
])

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
