
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drums_notes = [
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drums_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=54, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # Eb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm (F, Ab, G, Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),   # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),    # Ab
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drums_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drums_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
