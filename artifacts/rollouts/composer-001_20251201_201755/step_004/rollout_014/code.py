
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # F (41) on 2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # D2 (38) chromatic approach on 3 (C#2 = 37)
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625),
    # A (45) on 4
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # G5
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Dante: Motif (Bb, D, F, Bb)
# Start on 1.5s, end on 2.0s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.6875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=74, start=1.6875, end=1.875), # D5
    pretty_midi.Note(velocity=110, pitch=77, start=1.875, end=2.0),    # F5
    pretty_midi.Note(velocity=110, pitch=70, start=2.0, end=2.1875),  # Bb4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Dm
bass_notes = [
    # F (41) on 1
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),
    # A (45) on 2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),
    # D2 (38) chromatic approach on 3 (C#2 = 37)
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.125),
    # G (48) on 4
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # G5
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Dante: Motif continuation (Bb, D, F, Bb)
# Start on 3.0s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.1875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=74, start=3.1875, end=3.375), # D5
    pretty_midi.Note(velocity=110, pitch=77, start=3.375, end=3.5625), # F5
    pretty_midi.Note(velocity=110, pitch=70, start=3.5625, end=3.75),  # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Dm
bass_notes = [
    # G (48) on 1
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
    # D2 (38) on 2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    # F (41) chromatic approach on 3 (E = 40)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),
    # A (45) on 4
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # G5
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Dante: Motif continuation (Bb, D, F, Bb) with resolution
# Start on 4.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.6875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=74, start=4.6875, end=4.875), # D5
    pretty_midi.Note(velocity=110, pitch=77, start=4.875, end=5.0625), # F5
    pretty_midi.Note(velocity=110, pitch=70, start=5.0625, end=5.25),  # Bb4
    # Resolution to Dm
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
