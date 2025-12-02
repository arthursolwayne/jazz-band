
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - Melody: C (60), E (64), G (67), Bb (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bass - Walking line: C (60), D (62), Eb (63), F (65)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano - Comp on 2 and 4: C7 (60), E7 (64), G7 (67), Bb7 (62)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.875),
]
piano.notes.extend(piano_notes)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - Repeat the motif, slightly altered: C (60), E (64), Bb (62), G (67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bass - Walking line: C (60), D (62), Eb (63), F (65)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano - Comp on 2 and 4: C7 (60), E7 (64), G7 (67), Bb7 (62)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.375),
]
piano.notes.extend(piano_notes)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - Finish the motif: C (60), G (67), E (64), C (60)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bass - Walking line: C (60), D (62), Eb (63), F (65)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano - Comp on 2 and 4: C7 (60), E7 (64), G7 (67), Bb7 (62)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=5.875),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.875),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.875),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.875),
]
piano.notes.extend(piano_notes)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro_wayne.mid")
