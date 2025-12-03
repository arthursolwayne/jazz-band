
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # C2
]

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 -> Ab7 -> Bbmaj7 -> Cm7
piano_notes = [
    # Fm7: F, Ab, C, Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Eb5
    # Ab7: Ab, C, Eb, Gb
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # Gb5
    # Bbmaj7: Bb, D, F, Ab
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Ab5
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # C5
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # G5
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),   # Bb5
]

# Sax: one short motif, start it, leave it hanging, come back and finish it
# Motif: F, Gb, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # Gb4
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # Ab4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75),  # F4 (return)
]

# Append all notes to corresponding instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),   # C2
]

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Cm7 -> F7 -> Bbmaj7 -> Ebmaj7
piano_notes = [
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # C5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),   # G5
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),   # Bb5
    # F7: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),   # F5
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),   # A5
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),   # C5
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),   # Eb5
    # Bbmaj7: Bb, D, F, Ab
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),   # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),   # F5
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),   # Ab5
    # Ebmaj7: Eb, G, Bb, D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),    # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),    # G5
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.5),    # Bb5
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),    # D5
]

# Sax: continuation of the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),  # Gb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.125, end=3.25),  # Ab4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.375),  # F4
]

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),   # C2
]

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Ebmaj7 -> Ab7 -> Bbmaj7 -> Fm7
piano_notes = [
    # Ebmaj7: Eb, G, Bb, D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),    # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),    # G5
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),    # Bb5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),    # D5
    # Ab7: Ab, C, Eb, Gb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),   # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),   # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),   # Eb5
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),   # Gb5
    # Bbmaj7: Bb, D, F, Ab
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),   # D5
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),   # F5
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),   # Ab5
    # Fm7: F, Ab, C, Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),    # F5
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),    # Ab5
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),    # C5
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),    # Eb5
]

# Sax: continuation of the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.625),  # Eb5
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=4.875),  # Gb4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),   # Ab4
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.125),   # F4
]

# Append all notes to corresponding instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
