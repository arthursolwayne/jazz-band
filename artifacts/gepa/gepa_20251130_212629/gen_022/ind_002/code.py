
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum sounds
KICK = 36
SNARE = 38
HIHAT = 42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add some syncopation and velocity variation to make it feel alive

# Bar 1 (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=KICK, start=1.125, end=1.5),

    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=SNARE, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=1.5, end=1.625),

    # Hi-hats on every eighth
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.125, end=1.5),
]

# Add the drum notes to the drum instrument
for note in drum_notes:
    drums.notes.append(note)

# BAR 2 - 4: Full quartet (1.5 - 6.0s)

# ----------------------------
# BASS LINE (Marcus)
# Walking bass in F minor: F, Gb, Ab, A, Bb, B, C, Db, etc.
# Chromatic approach to F and A, no repeats, always moving

# Time in seconds: 1.5 - 6.0 = 4.5 seconds for 3 bars (3 * 1.5 = 4.5)
# Each beat = 0.375s, each bar = 1.5s

# Bar 2: Fm7 walk (F, Gb, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=65, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=65, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=65, pitch=68, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=65, pitch=69, start=2.625, end=3.0),  # A
]

# Bar 3: Bb7 walk (Bb, B, C, Db)
bass_notes.extend([
    pretty_midi.Note(velocity=65, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=65, pitch=68, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=65, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=65, pitch=70, start=4.125, end=4.5),  # Db
])

# Bar 4: Fm7 again (F, Gb, Ab, A), but with a chromatic approach to F
bass_notes.extend([
    pretty_midi.Note(velocity=65, pitch=69, start=4.5, end=4.875),  # A (approach)
    pretty_midi.Note(velocity=65, pitch=68, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=65, pitch=70, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=65, pitch=71, start=5.625, end=6.0),  # F
])

# Add bass notes to the bass instrument
for note in bass_notes:
    bass.notes.append(note)

# ----------------------------
# PIANO (Diane) - 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, Db) on beat 2 and 4 of bars 2-4

# Bar 2, beat 2 (1.875s)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25),  # Db
]

# Bar 2, beat 4 (3.0s)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),  # Db
])

# Bar 3, beat 2 (3.375s)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),  # Db
])

# Bar 3, beat 4 (4.5s)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),  # Db
])

# Bar 4, beat 2 (4.875s)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),  # Db
])

# Bar 4, beat 4 (6.0s)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=67, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),  # Db
])

# Add piano notes to the piano instrument
for note in piano_notes:
    piano.notes.append(note)

# ----------------------------
# SAX (Dante) - Haunting, simple motif with space and tension

# Motif: F -> Ab -> Bb -> A (half note on F, eighth on Ab, eighth on Bb, half on A)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (half note)
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.375),  # Ab (eighth)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # Bb (eighth)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=5.25), # A (half note)
]

# Add sax notes to the sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
