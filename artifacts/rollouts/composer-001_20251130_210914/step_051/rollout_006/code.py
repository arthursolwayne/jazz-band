
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

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=59, start=2.25, end=2.625), # E (F7)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=59, start=3.75, end=4.125), # E (F7)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.125), # D
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=60, start=3.375, end=3.75), # F# (G7)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=85, pitch=68, start=3.375, end=3.75), # D#
    pretty_midi.Note(velocity=95, pitch=60, start=5.25, end=5.625), # F# (G7)
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=85, pitch=68, start=5.25, end=5.625), # D#
]
piano.notes.extend(piano_notes)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=105, pitch=66, start=1.5, end=1.875), # A (F7)
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.625), # C (G7)
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=105, pitch=66, start=3.0, end=3.375), # A (F7)
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=105, pitch=69, start=4.5, end=4.875), # C (G7)
    pretty_midi.Note(velocity=105, pitch=66, start=4.875, end=5.25), # A (F7)
    pretty_midi.Note(velocity=105, pitch=64, start=5.25, end=5.625), # B (F7)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
