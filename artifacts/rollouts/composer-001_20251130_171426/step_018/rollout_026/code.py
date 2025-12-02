
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Comping on 2 and 4 with 7th chords
# Fm7 = F, Ab, C, Eb
piano_notes = [
    # Bar 2, beat 2 (1.875s) - Fm7
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Eb
    # Bar 2, beat 4 (2.625s) - Fm7
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax - motif
sax_notes = [
    # Bar 2, beat 1: Start motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.875),  # G
    # Bar 2, beat 3: Continue motif
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),    # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),    # A
    # Bar 3, beat 1: Return and finish motif
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.625), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.625, end=3.875), # Eb
    # Bar 3, beat 3: One more phrase
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),    # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3 and 4: Continue the quartet
# Marcus: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=6.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3, beat 2 (3.875s) - Fm7
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=3.875, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.25),  # Eb
    # Bar 3, beat 4 (4.875s) - Fm7
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Eb
    # Bar 4, beat 2 (5.875s) - Fm7
    pretty_midi.Note(velocity=90, pitch=71, start=5.875, end=6.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.875, end=6.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=5.875, end=6.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.875, end=6.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Continue the drum pattern for bars 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
]
for note in drum_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("fm_intro.mid")
