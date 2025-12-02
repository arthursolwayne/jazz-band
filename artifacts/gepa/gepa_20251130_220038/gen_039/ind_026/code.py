
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25), # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625), # E (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # A (3rd)
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.75), # Bb (4th)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # A (chromatic)
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # B (5th)
    pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.875),  # Bb (chromatic)
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25), # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # E (chromatic)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # F (root)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # F7: F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F7: Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # F7: C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F7: E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # F7: F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # F7: Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # F7: C
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F7: E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # F7: F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # F7: Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # F7: C
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F7: E
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 4
]
drums.notes.extend(drum_notes)

# Saxophone (Dante)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # F (whisper)
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A (build)
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # D (turn)
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G (rise)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # D (fall)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # F (return)
    # Bar 4: Resolution
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # A (cry)
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # D (resolve)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # F (end)
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # F (hold)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("whisper_cry.mid")
