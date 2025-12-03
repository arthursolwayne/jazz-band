
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
    # Chromatic approach to G2 (MIDI 43) on & of 1
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to D2 (MIDI 38) on & of 2
    pretty_midi.Note(velocity=70, pitch=39, start=2.375, end=2.5625),
    # D2 (MIDI 38) on beat 3
    pretty_midi.Note(velocity=90, pitch=38, start=2.5625, end=2.9375),
    # Chromatic approach to G2 (MIDI 43) on & of 3
    pretty_midi.Note(velocity=70, pitch=42, start=2.9375, end=3.125),
    # G2 (MIDI 43) on beat 4
    pretty_midi.Note(velocity=90, pitch=43, start=3.125, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.5),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start motif on beat 2
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # A
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # Bb
    # Come back and finish it on beat 4
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.875),
    # Chromatic approach to D2 (MIDI 38) on & of 1
    pretty_midi.Note(velocity=70, pitch=41, start=3.875, end=4.0625),
    # D2 (MIDI 38) on beat 2
    pretty_midi.Note(velocity=90, pitch=38, start=4.0625, end=4.4375),
    # Chromatic approach to G2 (MIDI 43) on & of 2
    pretty_midi.Note(velocity=70, pitch=42, start=4.4375, end=4.625),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=90, pitch=43, start=4.625, end=5.0),
    # Chromatic approach to D2 (MIDI 38) on & of 3
    pretty_midi.Note(velocity=70, pitch=41, start=5.0, end=5.1875),
    # D2 (MIDI 38) on beat 4
    pretty_midi.Note(velocity=90, pitch=38, start=5.1875, end=5.5625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=5.5),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging again
sax_notes = [
    # Start motif on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=4.0625, end=4.3125),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.3125, end=4.5625),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=4.5625, end=4.8125),  # F
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=4.8125, end=5.0625),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=5.5625, end=5.9375),
    # Chromatic approach to G2 (MIDI 43) on & of 1
    pretty_midi.Note(velocity=70, pitch=42, start=5.9375, end=6.125),
    # G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=6.125, end=6.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=5.5625, end=6.5),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.5625, end=6.5),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.5625, end=6.5),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=5.5625, end=6.5),  # E
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Finish motif on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=6.125, end=6.375),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=6.375, end=6.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.5625, end=5.9375),
    pretty_midi.Note(velocity=100, pitch=36, start=6.6875, end=7.0625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=6.125, end=6.25),
    pretty_midi.Note(velocity=110, pitch=38, start=7.25, end=7.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.125),
    pretty_midi.Note(velocity=80, pitch=42, start=6.125, end=6.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=6.3125, end=6.5),
    pretty_midi.Note(velocity=80, pitch=42, start=6.5, end=6.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=6.6875, end=6.875),
    pretty_midi.Note(velocity=80, pitch=42, start=6.875, end=7.0625),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
