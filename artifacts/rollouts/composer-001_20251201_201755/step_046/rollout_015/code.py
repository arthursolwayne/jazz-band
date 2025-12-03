
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
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root) on 1
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # G#2 (chromatic approach to A2) on 2
    pretty_midi.Note(velocity=85, pitch=55, start=1.875, end=2.0),
    # A2 (fifth) on 3
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.375),
    # G#2 (chromatic approach to F2) on 4
    pretty_midi.Note(velocity=85, pitch=55, start=2.375, end=2.625),
    # F2 (root) on 4
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0)   # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: F# (MIDI 66) on beat 1
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),
    # Second note: A (MIDI 69) on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.125),
    # Third note: F# (MIDI 66) on beat 3
    pretty_midi.Note(velocity=110, pitch=66, start=2.125, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # A2 (fifth) on 1
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),
    # Bb2 (chromatic approach to B2) on 2
    pretty_midi.Note(velocity=85, pitch=58, start=3.375, end=3.625),
    # B2 (chromatic approach to C2) on 3
    pretty_midi.Note(velocity=85, pitch=59, start=3.625, end=3.875),
    # C2 (root) on 4
    pretty_midi.Note(velocity=90, pitch=60, start=3.875, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5)   # A
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    # Fourth note: A (MIDI 69) on beat 1
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),
    # Fifth note: C (MIDI 60) on beat 2
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),
    # Sixth note: A (MIDI 69) on beat 3
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),
    # Seventh note: F# (MIDI 66) on beat 4
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # C2 (root) on 1
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    # D2 (chromatic approach to D#2) on 2
    pretty_midi.Note(velocity=85, pitch=62, start=4.875, end=5.125),
    # D#2 (chromatic approach to E2) on 3
    pretty_midi.Note(velocity=85, pitch=63, start=5.125, end=5.375),
    # E2 (fifth) on 4
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0)   # E
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Eighth note: F# (MIDI 66) on beat 1
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),
    # Ninth note: A (MIDI 69) on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),
    # Tenth note: C (MIDI 60) on beat 3
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),
    # Eleventh note: F# (MIDI 66) on beat 4
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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
