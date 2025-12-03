
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=59, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=36, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=35, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: Bbmaj7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif with a variation or extension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),   # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0),   # E
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
