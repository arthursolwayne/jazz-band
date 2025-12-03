
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

# Bass: Walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif starts on F, ascends to A, then hangs on G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=4.5),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif repeats, but with a variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Drums: Same pattern, repeat
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif resolves
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Same pattern, repeat
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
