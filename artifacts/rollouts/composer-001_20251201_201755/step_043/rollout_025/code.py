
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
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (MIDI 43) on beat 2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.125),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # D2 (MIDI 38) on beat 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    # Second note: A (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    # Leave it hanging
    # Come back and finish it: C (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # Bb (MIDI 45) on beat 2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.625),
    # C (MIDI 48) on beat 3
    pretty_midi.Note(velocity=90, pitch=48, start=3.625, end=4.0),
    # G2 (MIDI 43) on beat 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    # Third note: D (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    # Fourth note: F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C (MIDI 48) on beat 1
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    # D (MIDI 50) on beat 2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.125),
    # F (MIDI 53) on beat 3
    pretty_midi.Note(velocity=90, pitch=53, start=5.125, end=5.5),
    # C (MIDI 48) on beat 4
    pretty_midi.Note(velocity=90, pitch=48, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Fifth note: G (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    # Sixth note: F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),
    # Seventh note: C (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    # Eighth note: F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),
    # Ninth note: G (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),
    # Tenth note: C (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
