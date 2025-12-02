
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),  # F (Dm7)
    pretty_midi.Note(velocity=90, pitch=56, start=1.5, end=3.0),  # A (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D (Dm7)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F (Dm7, 7th)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (start on 2nd beat, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),  # E4
    pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.25),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D4 (hold)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (Bb, D, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=4.5),  # Bb (Gm7)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=4.5),  # D (Gm7)
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=4.5),  # G (Gm7)
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5),  # Bb (Gm7, 7th)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (continue from where it left off)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5),  # D4 (hold)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (Eb, G, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=6.0),  # Eb (Cm7)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # G (Cm7)
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=6.0),  # C (Cm7)
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=6.0),  # Eb (Cm7, 7th)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (resolve the hanging note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E4
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # E4
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # C4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
