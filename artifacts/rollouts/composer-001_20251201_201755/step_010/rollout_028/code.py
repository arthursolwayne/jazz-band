
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm7 - Bb7 - Eb7 - Ab7 (roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # F (root)
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # C (fifth of Fm7)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # Bb (chromatic approach to Bb7)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0), # D (fifth of Bb7)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375), # Eb (root of Eb7)
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # G (fifth of Eb7)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # Ab (chromatic approach to Ab7)
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5), # C (fifth of Ab7)
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875), # Eb (root of Ab7)
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # G (fifth of Ab7)
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625), # Ab (root)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0), # D (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve each bar
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb) open voicing
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.0), # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0), # C
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=2.0), # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab) open voicing
    pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.5), # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.5), # D
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.5), # F
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.5), # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D) open voicing
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=3.0), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=2.5, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.5, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=3.0), # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# F - Ab - G - Eb - F (motif)
# Start on bar 2, leave it hanging, come back on bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=48, start=1.75, end=2.0), # Ab
    pretty_midi.Note(velocity=110, pitch=51, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=45, start=2.25, end=2.5), # Eb
    pretty_midi.Note(velocity=110, pitch=53, start=3.5, end=3.75), # F (return)
    pretty_midi.Note(velocity=110, pitch=48, start=3.75, end=4.0), # Ab
    pretty_midi.Note(velocity=110, pitch=51, start=4.0, end=4.25), # G
    pretty_midi.Note(velocity=110, pitch=45, start=4.25, end=4.5), # Eb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125), # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125), # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625), # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625), # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125), # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125), # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
