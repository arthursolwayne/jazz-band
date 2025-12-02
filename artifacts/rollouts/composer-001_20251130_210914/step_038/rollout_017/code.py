
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

# Bass line - Marcus: walking line, chromatic approaches, never the same note twice
# F7 chord: F A C E (7th chord)
# Walking bass line in F (F, G, A, Bb, B, C, D, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # G3
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # A3
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G3
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B3
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # A3
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # B3
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # C4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25), # B3
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625), # C4
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # B3
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
# F7 chord: F A C E
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A3
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E4
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A3
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E4
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F3
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E4
]
piano.notes.extend(piano_notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - Bb (67) - G (69) - A (71)
# Play it in bars 2 and 4, leave it hanging in bar 3
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # Bb3
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # G3
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # A3
    # Bar 3 (3.0 - 4.5s)
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # F3
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # Bb3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # G3
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),  # A3
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # F3
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # Bb3
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),  # G3
    pretty_midi.Note(velocity=110, pitch=71, start=5.75, end=6.0),  # A3
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
]
# Snare on 2 and 4
snare_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
]
# Hihat on every eighth
hihat_notes = [
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
