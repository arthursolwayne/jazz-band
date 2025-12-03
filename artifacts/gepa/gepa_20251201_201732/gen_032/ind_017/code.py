
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F2, Ab2, Bb2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0)   # Db2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875), # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0), # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0)  # Db
])
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Motif: F, Ab, Bb, F - but leave the last F hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.625, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.125), # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.125, end=2.375), # F (hanging)
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=2.75), # F (finish)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet continues (3.0 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125), # Db2
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # Ab2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # Db2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0)   # F2
]
bass.notes.extend(bass_notes)

# Piano: Continue with open voicings
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375), # D
]
piano.notes.extend(piano_notes)

# Sax: Motif continues (end of bar 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=2.75, end=3.0)  # F (finish)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
