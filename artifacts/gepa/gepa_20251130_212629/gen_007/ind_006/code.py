
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Dm7 - D, F, C, Bb
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.5),  # Bb

    # Bar 3: G7 - G, Bb, D, F
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # F

    # Bar 4: Cm7 - C, Eb, Bb, A
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=59, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Tenor solo - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: A (65) on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),
    # Bar 2: E (69) on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),
    # Bar 3: D (62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
    # Bar 3: Bb (59) on beat 2
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.25),
    # Bar 4: A (65) on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),
    # Bar 4: E (69) on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),
    # Bar 4: D (62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    # Bar 4: Bb (59) on beat 4
    pretty_midi.Note(velocity=110, pitch=59, start=5.0, end=5.25),
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_shorter_intro.mid")
