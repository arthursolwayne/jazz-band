
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Sax melody: one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: C (60) on beat 1
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    # Bar 2: D (62) on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    # Bar 2: Eb (63) on beat 3
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),
    # Bar 2: F (65) on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    # Bar 3: Leave it hanging, nothing
    # Bar 4: Return with resolution
    # C (60) on beat 1
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),
    # Bar 4: D (62) on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    # Bar 4: Eb (63) on beat 3
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),
    # Bar 4: G (67) on beat 4 for resolution
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2: C (60)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    # Bar 2: D (62)
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),
    # Bar 2: Eb (63)
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),
    # Bar 2: F (65)
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),
    # Bar 3: F# (66)
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),
    # Bar 3: G (67)
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    # Bar 3: A (69)
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),
    # Bar 3: Bb (70)
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),
    # Bar 4: B (71)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),
    # Bar 4: C (60)
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    # Bar 2: C7 on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
    # Bar 4: C7 on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
