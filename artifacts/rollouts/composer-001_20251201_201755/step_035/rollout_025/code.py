
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
    # Fm root (D2, MIDI 38) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.125),
    # Fm fifth (A2, MIDI 43)
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=44, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: F (MIDI 53)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    # Second note: Ab (MIDI 50)
    pretty_midi.Note(velocity=110, pitch=50, start=2.125, end=2.5),
    # Third note: F (MIDI 53)
    pretty_midi.Note(velocity=110, pitch=53, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (D2, MIDI 38) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.625),
    # Fm fifth (A2, MIDI 43)
    pretty_midi.Note(velocity=100, pitch=43, start=3.625, end=4.0),
    pretty_midi.Note(velocity=100, pitch=44, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    # Fourth note: Bb (MIDI 51)
    pretty_midi.Note(velocity=110, pitch=51, start=3.0, end=3.375),
    # Fifth note: D (MIDI 55)
    pretty_midi.Note(velocity=110, pitch=55, start=3.375, end=3.75),
    # Sixth note: Bb (MIDI 51)
    pretty_midi.Note(velocity=110, pitch=51, start=3.75, end=4.125),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (D2, MIDI 38) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=37, start=4.875, end=5.125),
    # Fm fifth (A2, MIDI 43)
    pretty_midi.Note(velocity=100, pitch=43, start=5.125, end=5.5),
    pretty_midi.Note(velocity=100, pitch=44, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Seventh note: C (MIDI 57)
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.875),
    # Eighth note: Eb (MIDI 54)
    pretty_midi.Note(velocity=110, pitch=54, start=5.125, end=5.5),
    # Ninth note: C (MIDI 57)
    pretty_midi.Note(velocity=110, pitch=57, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
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

# Save the MIDI file
# midi.write disabled
