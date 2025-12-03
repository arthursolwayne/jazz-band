
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (F2 - A2, MIDI 53 - 57), roots and fifths
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.25),  # C3
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),  # Ab2
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),   # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, chord each bar, resolve on last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # E4
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Ab4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # C5
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # Eb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # G5
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # Bb4
]
piano.notes.extend(piano_notes)

# Sax: motif (C5, Eb5, F5, G5), start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # Eb5
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),   # F5
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.5),   # G5
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=3.0),    # C5 (repeat)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line (F2 - A2, MIDI 53 - 57)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75),  # C3
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),  # Ab2
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),   # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, chord each bar, resolve on last
piano_notes = [
    # Bar 3: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # E4
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Ab4
    # Bar 5: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # C5
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # Eb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # G5
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # Bb4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hi-hats
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line (F2 - A2, MIDI 53 - 57)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # C3
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),   # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, chord each bar, resolve on last
piano_notes = [
    # Bar 4: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # E4
    # Bar 5: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Ab4
    # Bar 6: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # C5
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # Eb4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # G5
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # Bb4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hats
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
