
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

# Bass: Marcus - walking line (roots and fifths with chromatic approaches)
# Key is F, so root of first chord is F
bass_notes = [
    # Bar 2: F (root), G (fifth), E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),  # F

    # Bar 3: Bb (root), D (fifth), C (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # Bb

    # Bar 4: C (root), G (fifth), Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # E

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Ab

    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note of motif on beat 1 of bar 2: F (60)
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.6875),
    # Second note on beat 2 of bar 2: A (65)
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0625),
    # Third note on beat 3 of bar 2: G (62)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),
    # Leave it hanging on the last beat of bar 2: silence
    # Come back on beat 1 of bar 3: F (60)
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.1875),
    # Repeat the motif on beat 2 of bar 3: A (65)
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5625),
    # Repeat on beat 3 of bar 3: G (62)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375),
    # End on beat 4 of bar 3: C (64)
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.3125),
    # Last note on beat 1 of bar 4: F (60)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.6875),
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
# Kick on 1 and 3
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
