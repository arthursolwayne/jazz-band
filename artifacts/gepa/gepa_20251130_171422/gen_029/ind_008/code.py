
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # Fm7 - 3rd
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # E♭ - 7th
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A♭ - 9th
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Fm7 - 3rd
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # E♭ - 7th
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A♭ - 9th
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # G♭
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # E♭
    pretty_midi.Note(velocity=80, pitch=48, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),  # G♭
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # F7 - 3rd
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),  # A♭ - 7th
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # F7 - 3rd
    pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=3.0),  # A♭ - 7th
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Fm7 - 3rd
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # E♭ - 7th
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A♭ - 9th
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # Fm7 - 3rd
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # E♭ - 7th
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # A♭ - 9th
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),  # E♭
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # G♭
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),  # E♭
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # F7 - 3rd
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),  # A♭ - 7th
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # F7 - 3rd
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),  # A♭ - 7th
]
piano.notes.extend(piano_notes)

# Drums: continue the pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Fm7 - 3rd
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # E♭ - 7th
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A♭ - 9th
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # Fm7 - 3rd
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # E♭ - 7th
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # A♭ - 9th
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # G♭
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),  # E♭
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),  # G♭
    pretty_midi.Note(velocity=80, pitch=49, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # F7 - 3rd
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),  # A♭ - 7th
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # F7 - 3rd
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0),  # A♭ - 7th
]
piano.notes.extend(piano_notes)

# Drums: continue the pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
