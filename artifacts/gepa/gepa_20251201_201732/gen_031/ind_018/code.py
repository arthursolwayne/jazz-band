
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
    # Kick on 1 & 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 & 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line in F (F2, Bb2, C3, D3, etc.), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # Bb2
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # C3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # D3

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),   # D3
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # G3
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.125),  # F#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),   # G3

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),   # G3
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # Bb3
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625),  # B3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),   # Bb3
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, each bar a different chord, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, A, F (starting on beat 1 of bar 2)
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),   # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),   # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
