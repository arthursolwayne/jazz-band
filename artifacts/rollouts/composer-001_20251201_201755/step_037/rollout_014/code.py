
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
    # Hihat on every eighth
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
    # Chromatic approach to G2 (MIDI 43) on & of 1
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to C3 (MIDI 48) on & of 2
    pretty_midi.Note(velocity=70, pitch=47, start=2.375, end=2.5625),
    # C3 (MIDI 48) on beat 3
    pretty_midi.Note(velocity=90, pitch=48, start=2.5625, end=2.9375),
    # Chromatic approach to F3 (MIDI 53) on & of 3
    pretty_midi.Note(velocity=70, pitch=52, start=2.9375, end=3.125),
    # F3 (MIDI 53) on beat 4
    pretty_midi.Note(velocity=90, pitch=53, start=3.125, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),  # E (MIDI 68)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Bb - F (MIDI 65 - 67 - 69 - 65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # Chromatic approach to C3 (MIDI 48) on & of 1
    pretty_midi.Note(velocity=70, pitch=47, start=3.375, end=3.5625),
    # C3 (MIDI 48) on beat 2
    pretty_midi.Note(velocity=90, pitch=48, start=3.5625, end=3.9375),
    # Chromatic approach to F3 (MIDI 53) on & of 2
    pretty_midi.Note(velocity=70, pitch=52, start=3.9375, end=4.125),
    # F3 (MIDI 53) on beat 3
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),
    # Chromatic approach to Bb3 (MIDI 58) on & of 3
    pretty_midi.Note(velocity=70, pitch=57, start=4.5, end=4.6875),
    # Bb3 (MIDI 58) on beat 4
    pretty_midi.Note(velocity=90, pitch=58, start=4.6875, end=5.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab (MIDI 60)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
# Motif continuation: G - Bb - F (MIDI 67 - 69 - 65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bb3 (MIDI 58) on beat 1
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),
    # Chromatic approach to Eb4 (MIDI 63) on & of 1
    pretty_midi.Note(velocity=70, pitch=62, start=4.875, end=5.0625),
    # Eb4 (MIDI 63) on beat 2
    pretty_midi.Note(velocity=90, pitch=63, start=5.0625, end=5.4375),
    # Chromatic approach to Ab4 (MIDI 68) on & of 2
    pretty_midi.Note(velocity=70, pitch=67, start=5.4375, end=5.625),
    # Ab4 (MIDI 68) on beat 3
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),
    # Chromatic approach to Db5 (MIDI 73) on & of 3
    pretty_midi.Note(velocity=70, pitch=72, start=6.0, end=6.1875),
    # Db5 (MIDI 73) on beat 4
    pretty_midi.Note(velocity=90, pitch=73, start=6.1875, end=6.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # Eb (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # Db (MIDI 65)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
# Motif conclusion: F (MIDI 65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 3: 3.0 - 4.5s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
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

# Bar 4: 4.5 - 6.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
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
