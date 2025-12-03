
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
    # D2 (root) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (chromatic approach) on 2
    pretty_midi.Note(velocity=85, pitch=41, start=1.875, end=2.125),
    # G2 (fifth) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # D2 (root) on 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, finish it
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    # D (start of motif)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Eb (chromatic passing tone)
    pretty_midi.Note(velocity=105, pitch=63, start=1.875, end=2.125),
    # F (resolution)
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.5),
    # Leave it hanging on G (suspense)
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.875),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    # Bb (chromatic approach) on 1
    pretty_midi.Note(velocity=85, pitch=46, start=3.0, end=3.375),
    # C (root) on 2
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),
    # D (fifth) on 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),
    # Bb (chromatic approach) on 4
    pretty_midi.Note(velocity=85, pitch=46, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=4.5),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    # G (continue motif)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    # A (chromatic passing tone)
    pretty_midi.Note(velocity=105, pitch=69, start=3.375, end=3.75),
    # Bb (resolution)
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),
    # Leave it hanging on C (suspense)
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    # D (root) on 1
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    # F (chromatic approach) on 2
    pretty_midi.Note(velocity=85, pitch=53, start=4.875, end=5.125),
    # G (fifth) on 3
    pretty_midi.Note(velocity=90, pitch=55, start=5.125, end=5.5),
    # D (root) on 4
    pretty_midi.Note(velocity=90, pitch=50, start=5.5, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D F A C) - resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # D (resolve motif)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    # Eb (chromatic passing tone)
    pretty_midi.Note(velocity=105, pitch=63, start=4.875, end=5.125),
    # F (resolution)
    pretty_midi.Note(velocity=110, pitch=65, start=5.125, end=5.5),
    # End on G (strong finish)
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
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
