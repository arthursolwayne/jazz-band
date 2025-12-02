
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

# Bass: Marcus, walking line in F, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0), # E
    pretty_midi.Note(velocity=85, pitch=60, start=1.875, end=2.0), # C
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.5), # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5), # E
    pretty_midi.Note(velocity=85, pitch=60, start=3.375, end=3.5), # C
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.5), # F
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    ])

# Sax: Dante, motif in F with a question and a pause
sax_notes = [
    # Bar 2: motif
    pretty_midi.Note(velocity=105, pitch=65, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=105, pitch=67, start=1.75, end=2.0), # G
    pretty_midi.Note(velocity=105, pitch=64, start=2.0, end=2.25), # E
    pretty_midi.Note(velocity=105, pitch=65, start=2.25, end=2.5), # F
    # Bar 3: pause
    pretty_midi.Note(velocity=105, pitch=65, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=105, pitch=65, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=105, pitch=65, start=3.5, end=3.75), # F
    pretty_midi.Note(velocity=105, pitch=65, start=3.75, end=4.0), # F
    # Bar 4: resolution
    pretty_midi.Note(velocity=105, pitch=69, start=4.5, end=4.75), # A
    pretty_midi.Note(velocity=105, pitch=67, start=4.75, end=5.0), # G
    pretty_midi.Note(velocity=105, pitch=65, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=105, pitch=64, start=5.25, end=5.5), # E
    pretty_midi.Note(velocity=105, pitch=65, start=5.5, end=5.75), # F
    pretty_midi.Note(velocity=105, pitch=67, start=5.75, end=6.0), # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_shot.mid")
