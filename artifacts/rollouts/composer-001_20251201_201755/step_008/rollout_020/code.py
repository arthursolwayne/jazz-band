
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: D2 (D2=38) -> G2 (43) with chromatic approaches
# Bar 2: D2 -> Eb2 -> G2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # D
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Ab
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Bb
])
piano.notes.extend(piano_notes)

# Little Ray on drums (Bar 2-4)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (melodic interval: 4th, 2nd, 4th)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # Bb (return)
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
