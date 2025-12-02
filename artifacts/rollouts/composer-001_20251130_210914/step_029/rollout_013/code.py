
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
# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.0),  # Gb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=39, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=44, start=2.875, end=3.0),  # Ab
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.0),  # G
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=45, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=2.875, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=49, start=2.875, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Dante: Motif in Fm. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=42, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=44, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=45, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=47, start=1.875, end=2.0),  # D
    # Bar 3: Leave it hanging (hold D)
    pretty_midi.Note(velocity=110, pitch=47, start=2.0, end=2.125),  # D
    # Bar 4: Finish it (F, Ab, Bb, D)
    pretty_midi.Note(velocity=110, pitch=42, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=44, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=45, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=47, start=2.875, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.8125, end=4.0),
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.8125, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
