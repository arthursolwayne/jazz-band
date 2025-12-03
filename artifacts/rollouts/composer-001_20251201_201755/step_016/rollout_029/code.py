
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches, roots and fifths
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # G (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # F# (chromatic)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # G (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # A (root + 3)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # B (fifth + 3)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # A# (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # B (fifth + 3)
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # C (root + 4)
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25), # D (fifth + 4)
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625), # C# (chromatic)
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),  # D (fifth + 4)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.5),
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # Amin7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend([n for n in dir() if isinstance(n, pretty_midi.Note)])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
