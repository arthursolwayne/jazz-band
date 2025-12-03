
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2 - Bb2, MIDI 53 - 57)
bass_notes = [
    # F2 (MIDI 53) on 1
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # G2 (MIDI 55) on 2 with chromatic approach
    pretty_midi.Note(velocity=90, pitch=54, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.375),
    # A2 (MIDI 57) on 3
    pretty_midi.Note(velocity=90, pitch=57, start=2.375, end=2.75),
    # Bb2 (MIDI 57) on 4 with chromatic approach
    pretty_midi.Note(velocity=90, pitch=56, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=3.0)   # E
]
piano.notes.extend(piano_notes)

# Sax: Motif starting on F (MIDI 69), short phrase with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0)   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2 - Bb2, MIDI 53 - 57)
bass_notes = [
    # Bb2 (MIDI 57) on 1
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),
    # C3 (MIDI 58) on 2 with chromatic approach
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=58, start=3.5625, end=3.875),
    # D3 (MIDI 60) on 3
    pretty_midi.Note(velocity=90, pitch=60, start=3.875, end=4.25),
    # Eb3 (MIDI 61) on 4 with chromatic approach
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=90, pitch=61, start=4.4375, end=4.75)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5)   # A
]
piano.notes.extend(piano_notes)

# Sax: Continue motif with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.5625, end=3.9375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.4375, end=4.75)   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2 - Bb2, MIDI 53 - 57)
bass_notes = [
    # Eb3 (MIDI 61) on 1
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),
    # F3 (MIDI 63) on 2 with chromatic approach
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=63, start=5.0625, end=5.375),
    # G3 (MIDI 65) on 3
    pretty_midi.Note(velocity=90, pitch=65, start=5.375, end=5.75),
    # A3 (MIDI 67) on 4 with chromatic approach
    pretty_midi.Note(velocity=90, pitch=66, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=90, pitch=67, start=5.9375, end=6.25)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb G Bb D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0)   # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.0625, end=5.4375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.9375, end=6.25)   # F
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.9375),
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
