
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), chromatic approach to C#2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=37, start=1.875, end=2.25),
    # Bar 3: A2 (fifth), chromatic approach to Bb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0),
    # Bar 4: D2 (root), chromatic approach to C#2
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=37, start=3.375, end=3.75),
    # Bar 5: A2 (fifth), chromatic approach to Bb2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=42, start=4.125, end=4.5),
    # Bar 6: D2 (root), chromatic approach to C#2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=37, start=4.875, end=5.25),
    # Bar 7: A2 (fifth), chromatic approach to Bb2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # F5
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb4
])
# Bar 5: F7 (F-A-C-E)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # E5
])
# Bar 6: Bb7 (Bb-D-F-A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # A5
])
# Bar 7: Dm7 (D-F-A-C) - resolve back
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # C5
])
piano.notes.extend(piano_notes)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D E F G A Bb C D
# Motif: D -> F -> A -> Bb (sings, then leaves it)
# Bar 2: D (start), F (end of bar)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F4
    # Bar 3: A (mid), Bb (end of bar)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A4 (hold)
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A4 (hold)
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # A4 (hold)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # Bb4
    # Bar 4: D (end)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
