
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick_1, snare_1, hihat_1])

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick_2, snare_2, hihat_2])

# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Bb7
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # C7
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Eb7
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick_3, snare_3, hihat_3])

# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb7
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb7
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # C7
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # F7
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick_4, snare_4, hihat_4])

# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb7
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # C7
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # F7
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Eb7
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
