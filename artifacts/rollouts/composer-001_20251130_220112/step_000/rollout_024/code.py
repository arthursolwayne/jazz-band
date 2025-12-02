
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, Fm7 -> Bb7 -> Eb7 -> Am7
# Fm7: F, Ab, Db, E
# Bb7: Bb, D, F, Ab
# Eb7: Eb, G, Bb, Db
# Am7: A, C, E, G

bass_notes = [
    # Fm7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # Db
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0),  # E
    
    # Bb7
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),  # Ab
    
    # Eb7
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # Db
    
    # Am7
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5),  # G
]
bass.notes.extend(bass_notes)

# Diane: Fm7 -> Bb7 -> Eb7 -> Am7, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # E (7th)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Db

    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # G (7th)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F

    # Bar 4: Eb7
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),  # B (7th)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Bb

    # Bar 4: Am7
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=3.75),  # C (7th)
    pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),  # G
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, short motif
sax_notes = [
    # Bar 2: motif start
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # Db
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
    
    # Bar 3: motif repeat
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),  # Db
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D
    
    # Bar 4: motif finish
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),  # Db
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend([n for n in drums.notes if n.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
