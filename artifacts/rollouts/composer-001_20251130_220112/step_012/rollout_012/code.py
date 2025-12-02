
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
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick_1, snare_1, hihat_1])

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Marcus - Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # C
]
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat_2 = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick_2, snare_2, hihat_2])

# Dante - Tenor Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: 3.0 - 4.5s
# Marcus continues walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat_3 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick_3, snare_3, hihat_3])

# Dante - Tenor Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: 4.5 - 6.0s
# Marcus continues walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5),  # C
]
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat_4 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick_4, snare_4, hihat_4])

# Dante - Tenor Sax: Wrap it up
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
