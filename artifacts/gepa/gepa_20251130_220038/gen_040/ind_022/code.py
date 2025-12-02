
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
# Dm7 -> G7 -> Cmaj7 -> F7
# D - C# - C - B - A - G - F# - F - E - D - C - B - A - G - F - E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),   # C#
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.5),   # B
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),   # F#
    pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),   # E
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.0, end=4.25),   # C#
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.75),   # B
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),   # F#
    pretty_midi.Note(velocity=80, pitch=63, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 on bar 2, G7 on bar 3, Cmaj7 on bar 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cmaj7: C, E, G, B
piano_notes = [
    # Dm7 (bar 2) on 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),   # C

    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),   # C

    # G7 (bar 3) on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),   # B
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),   # F

    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),   # B
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),   # F

    # Cmaj7 (bar 4) on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0),   # B

    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0),   # B
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), E (64), F# (66), D (62), E (64), F# (66), E (64), F# (66), G (67), A (69), G (67), F# (66), E (64), D (62)
# Split into two phrases: first four notes, then rest
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625)
note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75)
note3 = pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=1.875)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0)

note5 = pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.625)
note6 = pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75)
note7 = pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875)
note8 = pretty_midi.Note(velocity=110, pitch=66, start=2.875, end=3.0)
note9 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125)
note10 = pretty_midi.Note(velocity=110, pitch=69, start=3.125, end=3.25)
note11 = pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375)
note12 = pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5)
note13 = pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.625)
note14 = pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.75)

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12, note13, note14])

# Drums: Bar 2 (1.5 - 3.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875)
hihat2 = pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.25)
hihat3 = pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625)
hihat4 = pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 3: Drums (3.0 - 4.5s)
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.375)
hihat2 = pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.75)
hihat3 = pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=4.125)
hihat4 = pretty_midi.Note(velocity=70, pitch=42, start=4.125, end=4.5)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 4: Drums (4.5 - 6.0s)
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.875)
hihat2 = pretty_midi.Note(velocity=70, pitch=42, start=4.875, end=5.25)
hihat3 = pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
