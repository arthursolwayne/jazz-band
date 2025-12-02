
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

# Marcus (Bass): Walking line in Dm, chromatic approaches
# Dm = D F A C
# Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.875, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.375, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.125, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.375, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.875, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane (Piano): 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-2.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # C
    # Bar 3 (2.0-2.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # C
    # Bar 4 (2.5-3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # C
    # Bar 5 (3.0-3.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # C
    # Bar 6 (3.5-4.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # C
    # Bar 7 (4.0-4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # C
    # Bar 8 (4.5-5.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # C
    # Bar 9 (5.0-5.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # C
    # Bar 10 (5.5-6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Dante (Sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Dm motif: D, F, A, C, then back to D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=5.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.875, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Drums: continue pattern
for i in range(1, 5):
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5 + 1.125, end=1.5 + i*1.5 + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*1.5 + 0.75, end=1.5 + i*1.5 + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*1.5 + 1.875, end=1.5 + i*1.5 + 2.0),
    # Hihat on every eighth
    for j in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + j*0.1875, end=1.5 + i*1.5 + j*0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
