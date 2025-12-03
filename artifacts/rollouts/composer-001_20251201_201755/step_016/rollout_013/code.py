
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125), # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875), # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # D (b7)
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # G (5th)
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375), # C (b3)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # D (b7)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # G (5th)
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875), # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # D (b7)
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # G (5th)
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0), # E (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0), # F (Fm7)
    pretty_mIDI.Note(velocity=90, pitch=50, start=1.5, end=2.0), # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=2.0), # C
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.0), # Eb

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=2.0, end=2.5), # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=2.0, end=2.5), # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.5), # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.5), # Ab

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=57, start=2.5, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=59, start=2.5, end=3.0), # C
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: F, Ab, G, F (1st bar), then Bb, C, D, Bb (2nd bar), then D, C, Bb, D (3rd bar), then F, Ab, G, F (4th bar)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=50, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0),

    pretty_midi.Note(velocity=110, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=57, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=52, start=4.125, end=4.5),

    pretty_midi.Note(velocity=110, pitch=55, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=57, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=52, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=55, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0), # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
