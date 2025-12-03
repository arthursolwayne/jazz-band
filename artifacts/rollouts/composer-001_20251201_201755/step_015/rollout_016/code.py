
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)    # hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Gb2
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # E2
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),  # D2

    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # C#2
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # Bb2

    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25), # C#2
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625), # E2
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Ab4

    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D5

    # Bar 4: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # Gb4
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Eb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Use F, Ab, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # C5
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625), # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)    # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)    # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375)    # hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
