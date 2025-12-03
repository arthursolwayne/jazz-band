
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # Fm fifth
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # Fm root
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Fm fifth
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # D (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # Fm root
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # Fm fifth
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # C (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Fm root
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F Ab C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875), # Eb
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375), # Ab
])
# Bar 4: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875), # F
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # G
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375), # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0), # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
