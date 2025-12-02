
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # F - Gb - G - Ab (chromatic approach to G)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=70, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),
    # D - Eb - E - F (walking line)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=66, start=2.125, end=2.25),
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),
    # Bb - B - C - D
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (beat 1): F7
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=95, pitch=73, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=95, pitch=79, start=1.5, end=1.625),  # D
    # Bar 2 (beat 3): G7
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=95, pitch=77, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=95, pitch=80, start=1.875, end=2.0),  # D
    # Bar 3 (beat 1): Am7
    pretty_midi.Note(velocity=95, pitch=77, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=95, pitch=82, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=95, pitch=79, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=95, pitch=82, start=2.25, end=2.375),  # C
    # Bar 3 (beat 3): D7
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=95, pitch=74, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=95, pitch=79, start=2.625, end=2.75),  # C
    # Bar 4 (beat 1): Gm7
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=95, pitch=82, start=3.0, end=3.125),  # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - Gb - G - F (melodic motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=70, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.125),
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=70, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0)
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
