
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
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0)   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # D7 - D
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.875),  # D7 - F#
    pretty_midi.Note(velocity=95, pitch=79, start=1.5, end=1.875),  # D7 - A
    pretty_midi.Note(velocity=95, pitch=81, start=1.5, end=1.875),  # D7 - C
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375),  # D7 - D
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375),  # D7 - F#
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.375),  # D7 - A
    pretty_midi.Note(velocity=95, pitch=81, start=3.0, end=3.375),  # D7 - C
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),  # D7 - D
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),  # D7 - F#
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=4.875),  # D7 - A
    pretty_midi.Note(velocity=95, pitch=81, start=4.5, end=4.875),  # D7 - C
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - Melody: One short motif, make it sing. Start it, leave it hanging, finish it.
sax_notes = [
    # Bar 2 - Start the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G
    # Bar 3 - Let it hang, then come back
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G
    # Bar 4 - Finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    # Final resolution
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
