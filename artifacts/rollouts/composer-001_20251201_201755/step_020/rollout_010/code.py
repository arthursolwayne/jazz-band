
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

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=2.0),  # C (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.5),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # C (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=2.75, end=3.0),  # B (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.25),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.5),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75),  # C (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.25),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=4.25, end=4.5),  # C (fifth)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.75),  # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=5.0),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # C (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.5, end=5.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=5.75, end=6.0),  # C (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # A (C5)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # C (D5)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # Eb (F5)
]

# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Bb (E4)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # D (G4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.5),  # Ab (F#4)
])

# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # C (G4)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # Eb (F5)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # G (D5)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # Bb (E4)
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (69), Bb (68), C (72), F (69)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
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
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
