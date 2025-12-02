
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # F# (F7 chord)
    pretty_midi.Note(velocity=100, pitch=47, start=1.75, end=2.0),  # A (F7 chord)
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # A# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.5),  # A#
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=2.75),  # B (F7 chord)
    pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=3.0),  # B#
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # G (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Sax (Dante) - melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # F (F7)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A (F7)
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # C (F7)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # D (chromatic)
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # B (F7)
]
sax.notes.extend(sax_notes)

# Drums (Bar 2)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5),  # A#
    pretty_midi.Note(velocity=100, pitch=47, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=45, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=100, pitch=46, start=4.25, end=4.5),  # G (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Sax (Dante) - melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # B
]
sax.notes.extend(sax_notes)

# Drums (Bar 3)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0),  # A#
    pretty_midi.Note(velocity=100, pitch=47, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=100, pitch=45, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=100, pitch=46, start=5.75, end=6.0),  # G (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax (Dante) - melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums (Bar 4)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
