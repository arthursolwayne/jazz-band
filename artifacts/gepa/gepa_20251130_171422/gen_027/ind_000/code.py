
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
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    # But with variation in dynamics and placement
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=85, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=85, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=85, pitch=41, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=82, pitch=39, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=84, pitch=40, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=83, pitch=42, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=81, pitch=41, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=86, pitch=38, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=87, pitch=40, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=88, pitch=43, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=89, pitch=41, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=85, pitch=40, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=84, pitch=39, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4, emotionally charged
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F7: F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=68, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # Ab
    
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=95, pitch=68, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # Ab

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),  # C7: C
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Eb

    pretty_midi.Note(velocity=105, pitch=62, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # Eb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F7: F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=105, pitch=68, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.875),  # Ab

    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=105, pitch=68, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=95, pitch=66, start=5.25, end=5.625),  # Ab

    pretty_midi.Note(velocity=115, pitch=62, start=5.625, end=6.0),  # C7: C
    pretty_midi.Note(velocity=105, pitch=67, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Eb
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): Motif — concise, memorable, emotional
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=105, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=105, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # C

    pretty_midi.Note(velocity=115, pitch=62, start=5.25, end=5.625),  # C (return)
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
