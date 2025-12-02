
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: One short motif, start it, leave it hanging

# C7 (C E G B) -> D7 (D F# A C) -> E7 (E G# B D)
# 16th note motif: C, D, E, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, no repeated notes
# C -> D -> Eb -> E -> F -> F# -> G -> Ab -> A -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=50, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=53, start=2.125, end=2.25),
    pretty_midi.Note(velocity=90, pitch=54, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=52, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=56, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=57, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: C7 on beat 1, comp on beat 2 (F7), on beat 3 (C7), on beat 4 (F7)
piano_notes = [
    # C7 on beat 1
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=69, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=76, start=1.625, end=1.75),
    # C7 on beat 3
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif, but leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, no repeated notes
# C -> D -> Eb -> E -> F -> F# -> G -> Ab -> A -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=53, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=52, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=55, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=56, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=57, start=4.375, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 3: C7 on beat 1, comp on beat 2 (F7), on beat 3 (C7), on beat 4 (F7)
piano_notes = [
    # C7 on beat 1
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=69, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=76, start=3.125, end=3.25),
    # C7 on beat 3
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.625),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, no repeated notes
# C -> D -> Eb -> E -> F -> F# -> G -> Ab -> A -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=50, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=49, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=52, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=53, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=52, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=55, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=54, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=56, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=57, start=5.875, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 4: C7 on beat 1, comp on beat 2 (F7), on beat 3 (C7), on beat 4 (F7)
piano_notes = [
    # C7 on beat 1
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=69, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=76, start=4.625, end=4.75),
    # C7 on beat 3
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0),
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.125),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.8125, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("4_bar_intro.mid")
