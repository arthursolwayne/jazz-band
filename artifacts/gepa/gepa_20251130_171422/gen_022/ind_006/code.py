
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
    pretty_midi.Note(velocity=110, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=110, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=110, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=110, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in F
# F7 -> E7 -> D7 -> C7 -> B7 -> A7 -> G7 -> F7 (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G again
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=66, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # G again
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# F7, Bb7, E7, A7
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # D
    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # C
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.5),  # F
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # F
]
piano.notes.extend(piano_notes)

# Dante: Melody - one short motif, make it sing.
# F -> G -> A -> Bb, then hold Bb and resolve to F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=3.0),  # Bb (hold)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=110, pitch=73, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.5),  # Bb (hold)
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums continue for the full 6 seconds
# Bars 2-4: 1.5 - 6.0s
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2])
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare1, snare2])
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=110, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
