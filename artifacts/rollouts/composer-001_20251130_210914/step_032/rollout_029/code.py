
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),  # G#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=73, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=80, pitch=75, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=77, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=78, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=80, pitch=80, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=80, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=78, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=80, start=2.625, end=3.0),  # F
    # Bar 3: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=80, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=78, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=80, start=4.125, end=4.5),  # F
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=80, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=78, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.6875, end=1.875), # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=3.1875, end=3.375), # Bb
    # Bar 4: Return to finish it
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=78, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=110, pitch=71, start=5.0625, end=5.25),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
