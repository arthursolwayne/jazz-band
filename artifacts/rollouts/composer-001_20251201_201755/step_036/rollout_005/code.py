
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
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    # G2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.125),
    # A2 (chromatic approach to Bb2)
    pretty_midi.Note(velocity=100, pitch=78, start=2.125, end=2.375),
    # Bb2 (fourth)
    pretty_midi.Note(velocity=100, pitch=79, start=2.375, end=2.625),
    # C3 (root)
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=2.875),
    # D3 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=82, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: F (F4)
    pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.875),
    # Second note: A (A4)
    pretty_midi.Note(velocity=110, pitch=79, start=1.875, end=2.125),
    # Leave it hanging
    # Come back and finish it
    # Third note: C (C5)
    pretty_midi.Note(velocity=110, pitch=81, start=2.625, end=2.875),
    # Fourth note: F (F5)
    pretty_midi.Note(velocity=110, pitch=84, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    # G2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.625),
    # A2 (chromatic approach to Bb2)
    pretty_midi.Note(velocity=100, pitch=78, start=3.625, end=3.875),
    # Bb2 (fourth)
    pretty_midi.Note(velocity=100, pitch=79, start=3.875, end=4.125),
    # C3 (root)
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.375),
    # D3 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=82, start=4.375, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # A
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    # Fifth note: G (G5)
    pretty_midi.Note(velocity=110, pitch=85, start=3.0, end=3.375),
    # Sixth note: Bb (Bb5)
    pretty_midi.Note(velocity=110, pitch=87, start=3.375, end=3.625),
    # Seventh note: D (D5)
    pretty_midi.Note(velocity=110, pitch=89, start=3.625, end=3.875),
    # Eighth note: F (F5)
    pretty_midi.Note(velocity=110, pitch=84, start=3.875, end=4.125),
    # Ninth note: G (G5)
    pretty_midi.Note(velocity=110, pitch=85, start=4.125, end=4.375),
    # Tenth note: A (A5)
    pretty_midi.Note(velocity=110, pitch=87, start=4.375, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    # G2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.125),
    # A2 (chromatic approach to Bb2)
    pretty_midi.Note(velocity=100, pitch=78, start=5.125, end=5.375),
    # Bb2 (fourth)
    pretty_midi.Note(velocity=100, pitch=79, start=5.375, end=5.625),
    # C3 (root)
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=5.875),
    # D3 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=82, start=5.875, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    # Eleventh note: C (C5)
    pretty_midi.Note(velocity=110, pitch=81, start=4.5, end=4.875),
    # Twelfth note: F (F5)
    pretty_midi.Note(velocity=110, pitch=84, start=4.875, end=5.125),
    # Thirteenth note: G (G5)
    pretty_midi.Note(velocity=110, pitch=85, start=5.125, end=5.375),
    # Fourteenth note: A (A5)
    pretty_midi.Note(velocity=110, pitch=87, start=5.375, end=5.625),
    # Fifteenth note: Bb (Bb5)
    pretty_midi.Note(velocity=110, pitch=87, start=5.625, end=5.875),
    # Sixteenth note: C (C5)
    pretty_midi.Note(velocity=110, pitch=81, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
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
