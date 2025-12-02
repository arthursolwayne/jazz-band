
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=80, pitch=39, start=2.0, end=2.1875),  # G#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=40, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=80, pitch=41, start=2.375, end=2.5625), # A#
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=2.9375),  # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=44, start=2.9375, end=3.125), # B
    pretty_midi.Note(velocity=80, pitch=43, start=3.125, end=3.3125), # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),   # A
    pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=3.6875),   # A#
    pretty_midi.Note(velocity=80, pitch=40, start=3.6875, end=3.875), # A
    pretty_midi.Note(velocity=80, pitch=39, start=3.875, end=4.0625), # G#
    pretty_midi.Note(velocity=80, pitch=38, start=4.0625, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=37, start=4.25, end=4.4375),  # F#
    pretty_midi.Note(velocity=80, pitch=36, start=4.4375, end=4.625), # F
    pretty_midi.Note(velocity=80, pitch=35, start=4.625, end=4.8125), # E
    pretty_midi.Note(velocity=80, pitch=34, start=4.8125, end=5.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.6875),  # E
    # Bar 3 - C7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.4375), # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.4375), # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.4375), # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.4375), # B
    # Bar 4 - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=59, start=2.9375, end=3.125), # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=2.9375, end=3.125), # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.9375, end=3.125), # F
    pretty_midi.Note(velocity=80, pitch=61, start=2.9375, end=3.125), # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (E), F (G), F (Bb), F (C), F (Bb), F (G), F (E), F (D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.1875, end=2.375), # C
    pretty_midi.Note(velocity=100, pitch=58, start=2.375, end=2.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.5625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.75, end=2.9375),  # E
    pretty_midi.Note(velocity=100, pitch=50, start=2.9375, end=3.125), # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.125, end=3.3125), # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.3125, end=3.5),   # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.5, end=3.6875),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.6875, end=3.875), # C
    pretty_midi.Note(velocity=100, pitch=58, start=3.875, end=4.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.0625, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=4.25, end=4.4375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.4375, end=4.625), # E
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.6875, end=1.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.4375, end=2.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.9375, end=3.125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.3125), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.8125, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
