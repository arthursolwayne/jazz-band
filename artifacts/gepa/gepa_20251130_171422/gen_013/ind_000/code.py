
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice.
# F minor scale: F, Gb, G, Ab, A, Bb, B, C
# Walking line in F minor: F, Gb, G, Ab, Bb, B, C, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),   # Ab
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
# F7 chord on beat 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=73, start=3.375, end=3.5),   # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5),   # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),   # F
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C (F minor) - short, singable, leaves it hanging on Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.625, end=1.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),    # C
    # Re-enter on beat 3 of bar 2
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=2.875),   # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),    # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.125),    # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for eighth in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + eighth * 0.1875, end=start + (eighth + 1) * 0.1875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
