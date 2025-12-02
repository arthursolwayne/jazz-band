
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    # Bar 2: C -> B -> Bb -> A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),   # A
    # Bar 3: G -> F# -> F -> E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # E
    # Bar 4: D -> C# -> C -> B
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
# Chords: C7 on 2, F7 on 4
piano_notes = [
    # Bar 2: C7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # Bb
    # Bar 3: No piano
    # Bar 4: F7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Dante (melody - one short motif, start it, leave it hanging, come back and finish)
# Motif: C -> E -> B -> C
# Play on beat 1 of bar 2, leave it hanging on beat 3, come back on beat 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C (coming back)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
