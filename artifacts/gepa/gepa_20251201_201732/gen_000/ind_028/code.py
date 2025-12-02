
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
    # Kick on 1 and 3 (0.0, 0.75)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.15),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.9),
    # Snare on 2 and 4 (0.375, 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.525),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.275),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.15),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.3375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.525),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.7125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.0875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.275),
    pretty_midi.Note(velocity=100, pitch=42, start=1.29375, end=1.44375)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.65),  # Fm root (F)
    pretty_midi.Note(velocity=100, pitch=40, start=1.6875, end=1.8375),  # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.025),  # Bb (Fm 5th)
    pretty_midi.Note(velocity=100, pitch=38, start=2.0625, end=2.2125),  # F again
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.15),  # Ab
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.3375),  # B (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.525),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=3.5625, end=3.7125),  # Ab
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.65),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=4.6875, end=4.8375),  # C (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.025),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=5.0625, end=5.2125),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.65),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.65),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.65),  # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.15),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.15),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.15),  # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.15),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.65),  # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.65),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.65),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.65),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.65),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.8375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.025),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.2125),  # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.525),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.5625, end=3.7125),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.025),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.2125),  # G
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.65),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.025),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.775),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.65),
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.8375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.025),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.2125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4),
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.5875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.775),
    pretty_midi.Note(velocity=100, pitch=42, start=2.8125, end=2.9625)
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.15),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.525),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.275),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.15),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.3375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.525),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.7125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.0875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.275),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.4625)
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.65),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.025),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.4),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.775),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.65),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.8375),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.025),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.2125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.5875),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.775),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=5.9625)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
