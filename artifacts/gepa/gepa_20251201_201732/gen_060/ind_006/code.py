
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm (F, C, Ab)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # Ab (chromatic approach up)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F (root)
    
    # Bar 3: Bb7 (Bb, F, D)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # F (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # D (chromatic approach down)
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Bb (root)
    
    # Bar 4: Eb7 (Eb, Bb, G)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Eb (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Bb (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G (chromatic approach down)
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Eb (root)
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm9 (F, Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.0),  # F

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.5),  # Bb

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=5.0),  # Eb
]
piano.notes.extend(piano_notes)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),   # Snare on 2
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

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.9375, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.3125, end=5.5),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=6.1875, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=6.5625, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=6.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.9375, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.3125)
]
drums.notes.extend(drum_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm (F, Ab, C, Eb) in a short, lyrical, non-scalar phrase

sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=105, pitch=64, start=1.5, end=1.6875),  # F (64 is F4, not F2)
    pretty_midi.Note(velocity=105, pitch=61, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=105, pitch=65, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=105, pitch=62, start=2.0, end=2.1875),  # Eb

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=105, pitch=65, start=3.0, end=3.125),   # C (hold)
    pretty_midi.Note(velocity=105, pitch=62, start=3.125, end=3.25),  # Eb (hold)
    pretty_midi.Note(velocity=105, pitch=61, start=3.25, end=3.375),  # Ab (hold)

    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=105, pitch=64, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=105, pitch=61, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=105, pitch=65, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=105, pitch=62, start=4.875, end=5.0),   # Eb
    pretty_midi.Note(velocity=105, pitch=64, start=5.0, end=5.125),   # F (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
