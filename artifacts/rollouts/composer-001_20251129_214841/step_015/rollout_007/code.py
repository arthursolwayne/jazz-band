
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Marcus on bass - walking line with chromatic approaches
bass_notes = [
    # Bar 2: C - B - Bb - A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),
    # Bar 3: D - C# - C - B
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5),
    # Bar 4: E - D# - D - C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 on 2
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),
    # Bar 3: D7 on 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=4.125),
    # Bar 4: E7 on 2
    pretty_midi.Note(velocity=95, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Dante on sax - short motif, start it, leave it hanging, come back
# Motif: C - E - B - D (ascending)
sax_notes = [
    # Start the motif (Bar 2)
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),
    # Leave it hanging (Bar 3)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),
    # Come back and finish it (Bar 4)
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
