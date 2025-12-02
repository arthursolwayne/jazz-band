
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Fm root and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # F (root)

    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),   # F (root)

    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),   # F (root)
]
bass.notes.extend(bass_notes)

# Piano comping (open voicings, resolving on the last beat of each bar)
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.875),  # F (3rd octave)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # D
    # Bar 3 (Cm7)
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625), # A
    # Bar 4 (F7)
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # D
]
piano.notes.extend(piano_notes)

# Saxophone motif (start it, leave it hanging, return to finish)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.8125, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
