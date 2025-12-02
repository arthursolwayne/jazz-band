
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3 (beats 0 and 2)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4 (beats 1 and 3)
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start of motif (Fm7 -> Bb7 -> Eb7 -> Ab7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # D2 (Fm root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),  # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),  # G2 (Fm fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),  # F# (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Continue motif (Bb7 -> Eb7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line (Bb -> C -> F -> Eb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.5),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Ab7 (Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G
]
piano.notes.extend(piano_notes)

# Sax: End of motif (Ab7 -> resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line (Ab -> Bb -> Eb -> D)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3 (beats 0 and 2)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.75),
    # Snare on 2 and 4 (beats 1 and 3)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=4.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.375),
    pretty_midi.Note(velocity=100, pitch=42, start=4.375, end=4.75),
    pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=5.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.5),
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("jazz_intro.mid")
