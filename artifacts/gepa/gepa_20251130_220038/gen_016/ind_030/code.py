
import pretty_midi

# Create the MIDI file with a tempo of 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# ---------------------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only

# Kick on beats 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=1.125, end=1.5),
]

# Snare on beats 2 and 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=snare, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.25),
]

# Hihat on every eighth note
for i in range(0, 6, 1):
    drum_notes += [
        pretty_midi.Note(velocity=80, pitch=hihat, start=i * 0.375, end=(i + 1) * 0.375)
    ]

drums.notes.extend(drum_notes)

# ---------------------------
# Bar 2: Full Quartet (1.5 - 3.0s)

# Marcus - Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # Eb
]

bass.notes.extend(bass_notes)

# Diane - Piano comping with 7th chords on 2 and 4
# Dm7 on beat 2 (1.875 - 2.25)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # C
]

# Dm7 on beat 4 (2.625 - 3.0)
piano_notes += [
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),   # C
]

piano.notes.extend(piano_notes)

# Dante - Tenor Sax Melody
# Short motif in Dm: D - E - F - D (Dorian mode)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]

sax.notes.extend(sax_notes)

# ---------------------------
# Bar 3: Full Quartet (3.0 - 4.5s)

# Marcus - Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),   # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),   # D
]

bass.notes.extend(bass_notes)

# Diane - Piano comping with 7th chords on 2 and 4
# Dm7 on beat 2 (3.375 - 3.75)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # C
]

# Dm7 on beat 4 (4.125 - 4.5)
piano_notes += [
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),   # C
]

piano.notes.extend(piano_notes)

# Dante - Tenor Sax Melody
# Follow-up to the motif: D - Eb - D - E
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # E
]

sax.notes.extend(sax_notes)

# ---------------------------
# Bar 4: Full Quartet (4.5 - 6.0s)

# Marcus - Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # Eb
]

bass.notes.extend(bass_notes)

# Diane - Piano comping with 7th chords on 2 and 4
# Dm7 on beat 2 (4.875 - 5.25)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # C
]

# Dm7 on beat 4 (5.625 - 6.0)
piano_notes += [
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # C
]

piano.notes.extend(piano_notes)

# Dante - Tenor Sax Melody
# Resolving the motif: E - F - D - Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # Eb
]

sax.notes.extend(sax_notes)

# ---------------------------
# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
