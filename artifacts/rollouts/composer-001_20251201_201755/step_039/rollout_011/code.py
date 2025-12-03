
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
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to C3 (MIDI 48) on beat 4
    pretty_midi.Note(velocity=60, pitch=47, start=2.375, end=2.625),
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
    # First note: F (MIDI 65) on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    # Second note: A (MIDI 76) on beat 2
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.125),
    # Leave it hanging on beat 3
    pretty_midi.Note(velocity=110, pitch=76, start=2.125, end=2.375),
    # Come back and finish it on beat 4 with C (MIDI 69)
    pretty_midi.Note(velocity=110, pitch=69, start=2.375, end=2.625),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (C3-Eb3, MIDI 48-50), roots and fifths with chromatic approaches
bass_notes = [
    # C3 (MIDI 48) on beat 1
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),
    # Chromatic approach to Eb3 (MIDI 50) on beat 2
    pretty_midi.Note(velocity=60, pitch=49, start=3.375, end=3.625),
    # Eb3 (MIDI 50) on beat 3
    pretty_midi.Note(velocity=80, pitch=50, start=3.625, end=3.9375),
    # Chromatic approach to G3 (MIDI 53) on beat 4
    pretty_midi.Note(velocity=60, pitch=52, start=3.9375, end=4.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif with a variation
sax_notes = [
    # First note: C (MIDI 60) on beat 1
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),
    # Second note: Eb (MIDI 62) on beat 2
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.625),
    # Leave it hanging on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.9375),
    # Come back and finish it on beat 4 with G (MIDI 67)
    pretty_midi.Note(velocity=110, pitch=67, start=3.9375, end=4.125),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (G3-Bb3, MIDI 53-55), roots and fifths with chromatic approaches
bass_notes = [
    # G3 (MIDI 53) on beat 1
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),
    # Chromatic approach to Bb3 (MIDI 55) on beat 2
    pretty_midi.Note(velocity=60, pitch=54, start=4.875, end=5.125),
    # Bb3 (MIDI 55) on beat 3
    pretty_midi.Note(velocity=80, pitch=55, start=5.125, end=5.4375),
    # Chromatic approach to D4 (MIDI 58) on beat 4
    pretty_midi.Note(velocity=60, pitch=57, start=5.4375, end=5.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif and resolve
sax_notes = [
    # First note: G (MIDI 67) on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),
    # Second note: B (MIDI 71) on beat 2
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.125),
    # Leave it hanging on beat 3
    pretty_midi.Note(velocity=110, pitch=71, start=5.125, end=5.4375),
    # Come back and finish it on beat 4 with F (MIDI 65)
    pretty_midi.Note(velocity=110, pitch=65, start=5.4375, end=5.625),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
