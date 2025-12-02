
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Dante's motif
# Start with a phrase that lingers, ends unresolved
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Fm7: F, Ab, Bb, D
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # E (tension)
    # Bar 3: Repeat the first two notes
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),
    # Bar 4: Leave it hanging on the E, not resolving yet
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),
    # Repeat the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),
    # End on E, unresolved
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

# Bass: Marcus's walking line
# Fm7 (F, Ab, Bb, D) with chromatic approaches
# Bar 2: F -> Eb -> F -> Gb -> Ab (chromatic line down to Ab)
# Bar 3: Ab -> G -> Ab -> Bb -> B
# Bar 4: B -> A -> B -> C -> D (chromatic line up to D)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=61, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane's comping
# 7th chords on 2 and 4, Fm7 (F, Ab, Bb, D)
# Bar 2: Fm7 on beat 2
# Bar 3: Fm7 on beat 2
# Bar 4: Fm7 on beat 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2 (start=1.75)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    # Bar 3: Fm7 on beat 2 (start=3.0)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    # Bar 4: Fm7 on beat 2 (start=4.25)
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),
    # Fm7 on beat 4 (start=5.75)
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for eighth in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + eighth * 0.375, end=start + eighth * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
