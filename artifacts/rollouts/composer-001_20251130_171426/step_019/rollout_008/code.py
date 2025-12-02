
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.875),  # D
]

# Sax: short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # E
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # B
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.375),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.375),  # E
]

# Sax: motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # E
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),   # E
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.875),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=5.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=5.875),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=5.875),  # G
]

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
]

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2])

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
