
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
    # D2 (MIDI 38) on 1
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Eb2 (MIDI 39) on & of 1
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.0),
    # G2 (MIDI 43) on 2
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    # A2 (MIDI 45) on & of 2
    pretty_midi.Note(velocity=80, pitch=45, start=2.375, end=2.5),
    # D2 (MIDI 38) on 3
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.875),
    # Eb2 (MIDI 39) on & of 3
    pretty_midi.Note(velocity=80, pitch=39, start=2.875, end=3.0),
    # G2 (MIDI 43) on 4
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    # A2 (MIDI 45) on & of 4
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=3.0),  # F (MIDI 70)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # A (MIDI 74)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # E (MIDI 79)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (MIDI 70), G (MIDI 71), Eb (MIDI 69), F (MIDI 70)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=70, start=2.5, end=2.75),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on 1
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    # A2 (MIDI 45) on & of 1
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.5),
    # C3 (MIDI 48) on 2
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.875),
    # Db3 (MIDI 49) on & of 2
    pretty_midi.Note(velocity=80, pitch=49, start=3.875, end=4.0),
    # G2 (MIDI 43) on 3
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.375),
    # A2 (MIDI 45) on & of 3
    pretty_midi.Note(velocity=80, pitch=45, start=4.375, end=4.5),
    # C3 (MIDI 48) on 4
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),
    # Db3 (MIDI 49) on & of 4
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # D (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # Ab (MIDI 74)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=70, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=70, start=4.0, end=4.25),
    pretty_midi.Note(velocity=110, pitch=68, start=4.25, end=4.5),
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=70, start=4.75, end=5.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C3 (MIDI 48) on 1
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),
    # Db3 (MIDI 49) on & of 1
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.0),
    # F3 (MIDI 53) on 2
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.375),
    # G3 (MIDI 55) on & of 2
    pretty_midi.Note(velocity=80, pitch=55, start=5.375, end=5.5),
    # C3 (MIDI 48) on 3
    pretty_midi.Note(velocity=80, pitch=48, start=5.5, end=5.875),
    # Db3 (MIDI 49) on & of 3
    pretty_midi.Note(velocity=80, pitch=49, start=5.875, end=6.0),
    # F3 (MIDI 53) on 4
    pretty_midi.Note(velocity=80, pitch=53, start=6.0, end=6.375),
    # G3 (MIDI 55) on & of 4
    pretty_midi.Note(velocity=80, pitch=55, start=6.375, end=6.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # F# (MIDI 73)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # A (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # C (MIDI 71)
]
piano.notes.extend(piano_notes)

# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=70, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=68, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=70, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
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

# Save the MIDI file
# midi.write disabled
