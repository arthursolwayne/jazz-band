
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to D2 (MIDI 38) on beat 4
    pretty_midi.Note(velocity=80, pitch=39, start=2.375, end=2.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Motif starts on beat 2
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # F
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    # Chromatic approach to D2 (MIDI 38) on beat 2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.625),
    # D2 (MIDI 38) on beat 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=3.9375),
    # Chromatic approach to G2 (MIDI 43) on beat 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # A
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    # Continue the motif on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # E
    # Continue the motif on beat 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Chromatic approach to G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.125),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=100, pitch=43, start=5.125, end=5.5),
    # Chromatic approach to D2 (MIDI 38) on beat 4
    pretty_midi.Note(velocity=80, pitch=39, start=5.5, end=5.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Finish the motif on beat 1
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # F
    # Resolve on beat 3
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),  # F
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
