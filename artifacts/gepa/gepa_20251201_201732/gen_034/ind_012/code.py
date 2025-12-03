
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # F (fifth)
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2 (root)

    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F (fifth)
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D2 (root)

    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # F (fifth)
    pretty_midi.Note(velocity=100, pitch=54, start=5.25, end=5.625), # F# (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D

    # Bar 3: Gm7 (Bb, D, F, G)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G

    # Bar 4: Cm7 (Eb, G, Bb, C)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),

    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),

    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),

    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875),
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
