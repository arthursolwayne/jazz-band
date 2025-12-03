
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
# Bass: Walking line (F2 - Bb2, MIDI 53 - 57)
bass_notes = [
    # F2 (MIDI 53) - root
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    # G2 (MIDI 55) - chromatic approach to Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.125),
    # Bb2 (MIDI 57) - fifth of F7
    pretty_midi.Note(velocity=100, pitch=57, start=2.125, end=2.5),
    # F2 (MIDI 53) - root
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # Bb (MIDI 77)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # D (MIDI 79)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # E (MIDI 82)
]
piano.notes.extend(piano_notes)

# Sax: Motif - F, G#, Bb, Ab (MIDI 71, 73, 77, 76)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=73, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=77, start=2.125, end=2.5),
    pretty_midi.Note(velocity=110, pitch=76, start=2.5, end=2.875),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2 - Bb2, MIDI 53 - 57)
bass_notes = [
    # F2 (MIDI 53) - root
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),
    # G2 (MIDI 55) - chromatic approach to Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.625),
    # Bb2 (MIDI 57) - fifth of F7
    pretty_midi.Note(velocity=100, pitch=57, start=3.625, end=4.0),
    # F2 (MIDI 53) - root
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # Bb (MIDI 77)
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=4.5),  # D (MIDI 80)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # F (MIDI 79)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # Ab (MIDI 76)
]
piano.notes.extend(piano_notes)

# Sax: Motif - Bb, C, D, C (MIDI 77, 79, 81, 79)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=79, start=3.375, end=3.625),
    pretty_midi.Note(velocity=110, pitch=81, start=3.625, end=4.0),
    pretty_midi.Note(velocity=110, pitch=79, start=4.0, end=4.375),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2 - Bb2, MIDI 53 - 57)
bass_notes = [
    # F2 (MIDI 53) - root
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    # G2 (MIDI 55) - chromatic approach to Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.125),
    # Bb2 (MIDI 57) - fifth of F7
    pretty_midi.Note(velocity=100, pitch=57, start=5.125, end=5.5),
    # F2 (MIDI 53) - root
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # A (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # Bb (MIDI 77)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # D (MIDI 79)
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),  # E (MIDI 82)
]
piano.notes.extend(piano_notes)

# Sax: Motif - F, G#, Bb, Ab (MIDI 71, 73, 77, 76)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=73, start=4.875, end=5.125),
    pretty_midi.Note(velocity=110, pitch=77, start=5.125, end=5.5),
    pretty_midi.Note(velocity=110, pitch=76, start=5.5, end=5.875),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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
