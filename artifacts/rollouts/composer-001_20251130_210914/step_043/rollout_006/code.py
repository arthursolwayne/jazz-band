
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

# Marcus: Walking line, chromatic approaches, never the same note twice. Dm7 = D F A C
# Walking bass line in Dm: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach to F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4. Dm7 = D F A C
# Bars 2-4: play Dm7 on beat 2 and 4 of each bar
piano_notes = [
    # Bar 2, beat 2: Dm7
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625), # C
    # Bar 2, beat 4: Dm7
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125), # C
    # Bar 3, beat 2: Dm7
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25), # C
    # Bar 3, beat 4: Dm7
    pretty_midi.Note(velocity=95, pitch=62, start=6.0, end=6.375), # D
    pretty_midi.Note(velocity=90, pitch=65, start=6.0, end=6.375), # F
    pretty_midi.Note(velocity=95, pitch=67, start=6.0, end=6.375), # A
    pretty_midi.Note(velocity=90, pitch=70, start=6.0, end=6.375), # C
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: D -> Eb -> F -> D (Dm7 arpeggio with chromatic approach)
# Bar 2: Start motif on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=105, pitch=63, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25), # D
    # Leave it hanging, don't resolve
    # Bar 3: Repeat motif, start on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875), # D
    pretty_midi.Note(velocity=105, pitch=63, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75), # D
    # Bar 4: Resolve the motif, start on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875), # D
    pretty_midi.Note(velocity=105, pitch=63, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=5.25), # A (resolve to A)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # A (hold)
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0), # A (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
