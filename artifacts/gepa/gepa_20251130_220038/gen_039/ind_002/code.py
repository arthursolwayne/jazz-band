
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Dm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # A
    # Bar 3: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # A
    # Bar 4: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # A
]
piano.notes.extend(piano_notes)

# Dante - Tenor sax melody
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # Bb
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),# G
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # B
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.1875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.1875, end=5.375),# B
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5625),# Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.5625, end=5.75), # B
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),    # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend([n for n in drums.notes if n.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
