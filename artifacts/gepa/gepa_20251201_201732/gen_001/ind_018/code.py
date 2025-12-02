
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in
# Bass: C2 (MIDI 36) root, chromatic approach to D2 (MIDI 37), then D2 (MIDI 37)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625),
]
bass.notes.extend(bass_notes)

# Piano: Fmaj7 (F, A, C, E) on bar 2, then G7 (G, B, D, F) on bar 3, then Am7 (A, C, E, G) on bar 4
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # E
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # F
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),  # G
]
piano.notes.extend(piano_notes)

# Sax: One short motif, starting on F, then Bb, then G, then D — no scales, just melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D (return)
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Kick on 1 and 3 (2.25 - 3.75)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4 (2.625 - 3.0 and 3.75 - 4.125)
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
# Kick on 1 and 3 (3.75 - 4.5)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on 2 and 4 (4.125 - 4.25 and 4.875 - 5.0)
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bass: D2 (MIDI 37) on bar 3, then F2 (MIDI 38) on bar 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
]
bass.notes.extend(bass_notes)

# Piano: resolve on last chord (Am7 on bar 4)
piano_notes = [
    # Bar 4 (3.0 - 3.75) already added above
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
