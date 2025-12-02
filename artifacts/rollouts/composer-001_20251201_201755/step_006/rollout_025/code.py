
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bass line (F7 - D - A - C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=2.0),  # F7
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=3.5, end=4.0),  # F7
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=5.5, end=6.0),  # F7
]
bass.notes.extend(bass_notes)

# Piano chords (open voicings, resolve on the last beat of each bar)
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.0),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=80, start=2.5, end=3.0),  # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=3.5, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=80, start=3.5, end=4.0),  # Bb
    # Resolutions on last beat of each bar
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Sax melody (short motif, start it, leave it hanging, finish it)
# F - G# - A - Bb (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),   # Bb
    # Rest for a beat
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=2.75),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.875, end=3.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
