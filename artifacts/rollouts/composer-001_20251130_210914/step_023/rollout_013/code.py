
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
# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    kick_start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 1.125, end=kick_start + 1.5)
# Snare on 2 and 4
for bar in range(2, 4):
    snare_start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 0.75, end=snare_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 1.875, end=snare_start + 2.0)
# Hihat on every eighth
for bar in range(2, 4):
    snare_start = bar * 1.5
    for i in range(0, 8):
        start = snare_start + i * 0.375
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
