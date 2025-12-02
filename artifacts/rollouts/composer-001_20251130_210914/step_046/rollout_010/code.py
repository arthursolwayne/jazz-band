
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

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D
    # Bar 3 - D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),  # D
    # Bar 4 - D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

# Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Start of motif
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # F
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # E
    # Bar 4 - Come back and finish it
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
