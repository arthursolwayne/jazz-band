
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
# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # F#4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D4
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice. He's the anchor.
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D3
    pretty_midi.Note(velocity=80, pitch=63, start=1.625, end=1.75),  # D#3
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=1.875),  # E3
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0),  # F3
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.625),  # G3
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=2.75),  # G#3
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=2.875),  # A3
    pretty_midi.Note(velocity=80, pitch=70, start=2.875, end=3.0),  # A#3
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.625),  # C4
    pretty_midi.Note(velocity=80, pitch=73, start=3.625, end=3.75),  # C#4
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=3.875),  # D4
    pretty_midi.Note(velocity=80, pitch=76, start=3.875, end=4.0),  # E4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2: Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # E3 (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G3
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # B3
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),  # E4
    # Bar 3: Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # E3 (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G3
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # B3
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),  # E4
    # Bar 4: Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # E3 (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G3
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # B3
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # E4
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
