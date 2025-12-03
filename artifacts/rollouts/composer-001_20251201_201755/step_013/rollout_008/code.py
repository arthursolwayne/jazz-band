
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line in Fm (F2, Bb2, Eb2, Ab2, D2, G2, C2, F2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Bb2
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # Ab2
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, resolve on last bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=2.875, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),   # Bb
])
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Dante - Tenor sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (66), G (67), C (69)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=65, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=105, pitch=66, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=105, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.5),   # C
    pretty_midi.Note(velocity=105, pitch=65, start=2.875, end=3.0),  # F (reprise)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
