
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
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),  # A2
    pretty_midi.Note(velocity=100, pitch=54, start=2.25, end=2.625),  # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D2
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # A2
    pretty_midi.Note(velocity=100, pitch=54, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.25),  # C5
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # F4
    # Bar 4: Cmaj7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # B4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # F4
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # D4
    # Bar 4: Finish motif
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
