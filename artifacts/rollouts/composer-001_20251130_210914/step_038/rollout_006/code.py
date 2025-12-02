
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

# Marcus: Walking line, chromatic approaches, never the same note twice. He's the anchor.
# F minor walking bass line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
# F7, Bb7, Eb7, Ab7
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # F
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=60, start=2.625, end=2.8125),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.8125),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.8125),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=57, start=3.75, end=3.9375),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # Ab
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=3.9375),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),  # D
]
piano.notes.extend(piano_notes)

# You: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs — that's student shit.
# Motif: F, Bb, Eb, F
# Start on bar 2, leave it hanging, come back in bar 4
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=105, pitch=79, start=1.6875, end=1.875),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.8125),  # Eb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=84, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=105, pitch=79, start=3.9375, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.3125),  # Eb
    pretty_midi.Note(velocity=110, pitch=84, start=4.3125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0625),
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
