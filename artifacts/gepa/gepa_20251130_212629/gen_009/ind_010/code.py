
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Dm (D F A C)
# 1: D, 2: F, 3: A, 4: C, repeating
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords in Dm
# Dm7 = D F A C
# 2: Dm7, 4: Dm7
piano_notes = [
    # Bar 2, beat 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25), # C
    # Bar 2, beat 4: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0), # C
]
piano.notes.extend(piano_notes)

# Dante: Motif in Dm, starting with a descending minor 3rd
# D -> F -> C (to imply Dm)
# Then leave it hanging, return and finish it on the last beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Little Ray: Drums again
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Little Ray: Drums again
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes)

# Dante: Finish the motif with a descending minor 3rd on the last bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=5.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.875, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
