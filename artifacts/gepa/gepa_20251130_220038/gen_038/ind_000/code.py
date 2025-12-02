
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),   # G#
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25),  # D#
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=56, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # D
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # G
    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Melody (start of motif, leave it hanging, come back and finish it)
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # E
    # Bar 3: Rest and build
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),   # Ab
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=4.25, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("intro_wayne.mid")
