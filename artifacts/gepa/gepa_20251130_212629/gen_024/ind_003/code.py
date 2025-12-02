
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=1.6875, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),    # Gb
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.1875, end=2.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=2.5625, end=2.75),   # Gb
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=2.9375),   # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=39, start=2.9375, end=3.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=3.125, end=3.3125),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.3125, end=3.5),    # Gb
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),    # Ab
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4, dynamic variation
piano_notes = [
    # Bar 2 - comp on 2 and 4
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.0),  # F7 (F, A, C, Eb, Bb)
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=85, pitch=60, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=75, pitch=67, start=1.875, end=2.0),  # Bb
    # Bar 3 - comp on 2 and 4
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=2.8125),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=85, pitch=60, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=75, pitch=67, start=2.625, end=2.8125),
    # Bar 4 - comp on 2 and 4
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.5625),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=85, pitch=60, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=75, pitch=67, start=3.375, end=3.5625),
]
piano.notes.extend(piano_notes)

# Sax: Dante - short motif, sing, leave it hanging, make it search
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.65),  # Ab
    pretty_midi.Note(velocity=105, pitch=64, start=1.65, end=1.8),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.8, end=1.95),   # Bb
    pretty_midi.Note(velocity=105, pitch=65, start=1.95, end=2.1),   # G
    pretty_midi.Note(velocity=110, pitch=66, start=2.1, end=2.25),   # Ab
    pretty_midi.Note(velocity=105, pitch=64, start=2.25, end=2.4),   # F
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
