
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on upright bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - roots and fifths with chromatic approaches
# F7 chord: F, A, C, E (root, third, fifth, seventh)
# Walk with chromatic approach to each chord:
# Bar 2: F7 -> chromatic approach to F (E -> F)
# Bar 3: Bb7 -> chromatic approach to Bb (A -> Bb)
# Bar 4: E7 -> chromatic approach to E (D -> E)

bass_notes = [
    # Bar 2: F (E -> F), A, C, E
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.6875),  # E
    pretty_midi.Note(velocity=70, pitch=39, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=70, pitch=41, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=70, pitch=44, start=2.0, end=2.1875),  # C
    pretty_midi.Note(velocity=70, pitch=47, start=2.1875, end=2.375), # E

    # Bar 3: Bb7 (A -> Bb), D, F, A
    pretty_midi.Note(velocity=70, pitch=40, start=2.375, end=2.5625),  # A
    pretty_midi.Note(velocity=70, pitch=41, start=2.5625, end=2.75),  # Bb
    pretty_midi.Note(velocity=70, pitch=45, start=2.75, end=2.9375),  # D
    pretty_midi.Note(velocity=70, pitch=47, start=2.9375, end=3.125), # F
    pretty_midi.Note(velocity=70, pitch=49, start=3.125, end=3.3125), # A

    # Bar 4: E7 (D -> E), G, B, D
    pretty_midi.Note(velocity=70, pitch=43, start=3.3125, end=3.4375),  # D
    pretty_midi.Note(velocity=70, pitch=44, start=3.4375, end=3.625),  # E
    pretty_midi.Note(velocity=70, pitch=47, start=3.625, end=3.8125),  # G
    pretty_midi.Note(velocity=70, pitch=50, start=3.8125, end=4.0),   # B
    pretty_midi.Note(velocity=70, pitch=52, start=4.0, end=4.1875),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E) -> root position
# Bar 3: Bb7 (Bb, D, F, A) -> root position
# Bar 4: E7 (E, G, B, D) -> root position

piano_notes = [
    # Bar 2: F7 (root position)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F (middle C is 60, F4 = 53)
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # E

    # Bar 3: Bb7 (root position)
    pretty_midi.Note(velocity=100, pitch=50, start=2.375, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.375, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=2.375, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=2.375, end=2.75),  # A

    # Bar 4: E7 (root position)
    pretty_midi.Note(velocity=100, pitch=48, start=3.3125, end=3.6875),  # E
    pretty_midi.Note(velocity=100, pitch=51, start=3.3125, end=3.6875),  # G
    pretty_midi.Note(velocity=100, pitch=54, start=3.3125, end=3.6875),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=3.3125, end=3.6875),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Motif: Short, singable, not a scale
# F -> G -> F (implied A in the harmony) -> G -> F

# Bar 2: Start motif
# Bar 4: Finish motif

sax_notes = [
    # Bar 2: F (start of the motif)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=55, start=1.6875, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),    # F

    # Bar 3: Leave it hanging
    # No notes here, just space

    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=55, start=3.3125, end=3.4375),
    pretty_midi.Note(velocity=100, pitch=53, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=52, start=3.625, end=3.8125),  # C (chromatic descent)
    pretty_midi.Note(velocity=100, pitch=50, start=3.8125, end=4.0)    # Bb (resolution)
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
