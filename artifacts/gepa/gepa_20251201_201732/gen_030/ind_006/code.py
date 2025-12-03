
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875)  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass (Marcus) - walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # D (root)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar
piano_notes = [
    # Bar 2: F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # E
    # Bar 3: Bb7 (Bb D F A)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # A
    # Bar 4: Eb7 (Eb G Bb D)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, start on 2nd beat of bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875), # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (1.5 - 3.0s)
# Add hihat on every eighth
for i in range(0, 3):
    for j in range(0, 8):
        start = 1.5 + (i * 1.5) + (j * 0.375)
        if j % 2 == 0:
            pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
        else:
            pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.1875)
        # Kick on 1 and 3
        if j == 0 or j == 4:
            pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.1875)

# Bar 4: Drums (3.0 - 4.5s)
# Same pattern
for i in range(3, 4):
    for j in range(0, 8):
        start = 3.0 + (i * 1.5) + (j * 0.375)
        if j % 2 == 0:
            pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
        else:
            pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.1875)
        # Kick on 1 and 3
        if j == 0 or j == 4:
            pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.1875)

# Add full bar of drums for bar 4
for i in range(4, 5):
    for j in range(0, 8):
        start = 3.0 + (i * 1.5) + (j * 0.375)
        if j % 2 == 0:
            pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
        else:
            pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.1875)
        # Kick on 1 and 3
        if j == 0 or j == 4:
            pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
