
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875), # B
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875), # F
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=79, start=2.25, end=2.625), # F
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375), # F
    # Bar 4 (3.75 - 4.5)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.125), # F
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.5, end=4.875), # F
    # Bar 4 (5.25 - 6.0)
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625), # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First motif (Bar 2, start at 1.5)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    # Leave it hanging (Bar 3, start at 2.25)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # B
    # Come back and finish it (Bar 4, start at 3.0)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar (Bars 2-4)
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
