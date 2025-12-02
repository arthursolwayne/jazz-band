
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4])

# BAR 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B
]
piano.notes.extend(piano_notes)

# Sax: Motif starting on C, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # B
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
drums.notes.extend([kick2, snare2, hihat5, hihat6, hihat7, hihat8])

# BAR 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # B
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation, leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # E
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
drums.notes.extend([kick3, snare3, hihat9, hihat10, hihat11, hihat12])

# BAR 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # B
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
hihat16 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick4, snare4, hihat13, hihat14, hihat15, hihat16])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
