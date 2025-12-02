
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (38) -> F#2 (43), root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # chromatic approach up
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0)   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25)   # C#4
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging
# D4, F#4, G#4, A4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # G#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5)   # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (43) -> A2 (45), root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # chromatic approach up
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5)   # G2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G, B, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75)   # F#4
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging (F#4, G#4, A4, Bb4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # G#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.0)   # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (45) -> B2 (47), root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),  # chromatic approach up
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # B2
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0)   # A2
]
bass.notes.extend(bass_notes)

# Piano: A7 (A, C#, E, G#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),  # C#5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25)   # G#4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif (Bb4, A4, G#4, D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # G#4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5)   # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
