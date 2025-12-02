
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F - C
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # C
    # Bar 3: Bb - F
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # F
    # Bar 4: F - C
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # C
    # Chromatic approaches
    pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=2.25),  # E
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=3.0),  # Ab
])
# Bar 4: F7 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.75),  # Eb
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (G), Ab (Bb), Bb (A), F (G) - descending minor third
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # F (G)
    pretty_midi.Note(velocity=100, pitch=59, start=1.625, end=1.75),  # Ab (Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # Bb (A)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),   # F (G)
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # F (G)
    pretty_midi.Note(velocity=100, pitch=59, start=3.125, end=3.25),  # Ab (Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375),  # Bb (A)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),   # F (G)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
