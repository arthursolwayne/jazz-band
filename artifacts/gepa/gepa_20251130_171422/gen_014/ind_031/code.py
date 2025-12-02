
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create a mysterious, sparse groove with space
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

# Add to drum instrument
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Start of sax melody (1.5 - 3.0s)
# Fm7 -> Bb7 -> Eb7 -> Am7 - no modulation, just tension
# Sax melody: a fragment that feels like a memory, not a complete phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5), # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875), # F#
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0), # Eb
]

# Add to sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line in Fm with chromatic approaches
# Fm: F, Ab, Bb, Db
# Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=64, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=70, pitch=62, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=70, pitch=60, start=1.75, end=1.875), # Db
    pretty_midi.Note(velocity=70, pitch=62, start=1.875, end=2.0), # Eb
    pretty_midi.Note(velocity=70, pitch=64, start=2.0, end=2.125), # F
    pretty_midi.Note(velocity=70, pitch=67, start=2.125, end=2.25), # Ab
    pretty_midi.Note(velocity=70, pitch=69, start=2.25, end=2.375), # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=2.375, end=2.5), # Ab
    pretty_midi.Note(velocity=70, pitch=64, start=2.5, end=2.625), # F
    pretty_midi.Note(velocity=70, pitch=62, start=2.625, end=2.75), # Eb
    pretty_midi.Note(velocity=70, pitch=60, start=2.75, end=2.875), # Db
    pretty_midi.Note(velocity=70, pitch=62, start=2.875, end=3.0), # Eb
]

# Add to bass instrument
for note in bass_notes:
    bass.notes.append(note)

# Piano comping: 7th chords on 2 and 4
# Fm7 (F, Ab, Bb, Db) on beat 2 and 4
piano_notes = [
    # Bar 2, beat 2: Fm7
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=1.875), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=1.875), # Db
    # Bar 2, beat 4: Fm7
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.375), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.375), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.375), # Db
]

# Add to piano instrument
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: continuation of sax melody (3.0 - 4.5s)
# Keep the momentum, but leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.375, end=4.5), # A
]

# Add to sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Bass line continues, same pattern
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=3.0, end=3.125), # Eb
    pretty_midi.Note(velocity=70, pitch=60, start=3.125, end=3.25), # Db
    pretty_midi.Note(velocity=70, pitch=62, start=3.25, end=3.375), # Eb
    pretty_midi.Note(velocity=70, pitch=64, start=3.375, end=3.5), # F
    pretty_midi.Note(velocity=70, pitch=67, start=3.5, end=3.625), # Ab
    pretty_midi.Note(velocity=70, pitch=69, start=3.625, end=3.75), # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=3.875), # Ab
    pretty_midi.Note(velocity=70, pitch=64, start=3.875, end=4.0), # F
    pretty_midi.Note(velocity=70, pitch=62, start=4.0, end=4.125), # Eb
    pretty_midi.Note(velocity=70, pitch=60, start=4.125, end=4.25), # Db
    pretty_midi.Note(velocity=70, pitch=62, start=4.25, end=4.375), # Eb
    pretty_midi.Note(velocity=70, pitch=64, start=4.375, end=4.5), # F
]

# Add to bass instrument
for note in bass_notes:
    bass.notes.append(note)

# Piano continues comping with Fm7 on beat 2 and 4
piano_notes = [
    # Bar 3, beat 2: Fm7
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.375), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375), # Db
    # Bar 3, beat 4: Fm7
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.875), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.875), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.875), # Db
]

# Add to piano instrument
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: continuation and end of sax melody (4.5 - 6.0s)
# Leave it hanging, unresolved
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0), # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=5.875), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0), # F#
]

# Add to sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Bass line continues
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=70, pitch=62, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=70, pitch=60, start=4.75, end=4.875), # Db
    pretty_midi.Note(velocity=70, pitch=62, start=4.875, end=5.0), # Eb
    pretty_midi.Note(velocity=70, pitch=64, start=5.0, end=5.125), # F
    pretty_midi.Note(velocity=70, pitch=67, start=5.125, end=5.25), # Ab
    pretty_midi.Note(velocity=70, pitch=69, start=5.25, end=5.375), # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=5.375, end=5.5), # Ab
    pretty_midi.Note(velocity=70, pitch=64, start=5.5, end=5.625), # F
    pretty_midi.Note(velocity=70, pitch=62, start=5.625, end=5.75), # Eb
    pretty_midi.Note(velocity=70, pitch=60, start=5.75, end=5.875), # Db
    pretty_midi.Note(velocity=70, pitch=62, start=5.875, end=6.0), # Eb
]

# Add to bass instrument
for note in bass_notes:
    bass.notes.append(note)

# Piano continues comping with Fm7 on beat 2 and 4
piano_notes = [
    # Bar 4, beat 2: Fm7
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=4.875), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=4.875), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=4.875), # Db
    # Bar 4, beat 4: Fm7
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.375), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.375), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.375), # Db
]

# Add to piano instrument
for note in piano_notes:
    piano.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
