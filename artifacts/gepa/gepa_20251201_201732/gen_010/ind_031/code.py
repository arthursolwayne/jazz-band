
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75), # D#2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # G2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - C7, D7, E7, F7
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),  # C7
    pretty_midi.Note(velocity=100, pitch=85, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=1.875),  # E7

    # Bar 3 (3.0 - 4.5s) - G7, A7, B7, C7
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),  # G7
    pretty_midi.Note(velocity=100, pitch=88, start=3.0, end=3.375),  # A7
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.375),  # B7
    pretty_midi.Note(velocity=100, pitch=91, start=3.0, end=3.375),  # D7

    # Bar 4 (4.5 - 6.0s) - C7, D7, E7, F7
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),  # C7
    pretty_midi.Note(velocity=100, pitch=85, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.875),  # E7
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif in F, short and haunting
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - motif: F, A, Bb, (G)
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # G

    # Bar 3 (3.0 - 4.5s) - repeat the motif
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # G

    # Bar 4 (4.5 - 6.0s) - resolve the motif with a shift to G
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # Bb (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('waynes_moment.mid')
