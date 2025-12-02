
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create tension with space and dynamic variation
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=60, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: melodic walking line in F minor with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping with 7th chords on 2 and 4, emotionally charged
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # D

    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # D

    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: concise, emotional motif (start on bar 2)
# F, G#, Bb, Ab — a simple, modal phrase that lingers
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G#
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G#
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
