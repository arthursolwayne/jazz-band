
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # E
    # Bar 2, beat 4: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # E
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),   # C#
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # E
    # Bar 3, beat 4: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),   # E
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # E
    # Bar 4, beat 4: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),   # E
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Bar 3
for i in range(3):
    kick_start = 3.0 + i * 1.5
    kick_end = kick_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    snare_start = 3.75 + i * 1.5
    snare_end = snare_start + 0.375
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)

# Bar 4
for i in range(3):
    kick_start = 4.5 + i * 1.5
    kick_end = kick_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    snare_start = 5.25 + i * 1.5
    snare_end = snare_start + 0.375
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)

# Add hi-hats for bars 3 and 4
for i in range(3):
    for j in range(4):
        hihat_start = 3.0 + i * 1.5 + j * 0.375
        hihat_end = hihat_start + 0.375
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end)

for i in range(3):
    for j in range(4):
        hihat_start = 4.5 + i * 1.5 + j * 0.375
        hihat_end = hihat_start + 0.375
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
