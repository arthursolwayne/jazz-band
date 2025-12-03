
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

# Bass: Walking line in F (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root) on beat 1
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    # G2 (chromatic approach) on & of 1
    pretty_midi.Note(velocity=70, pitch=54, start=1.875, end=2.0),
    # C3 (fifth) on beat 2
    pretty_midi.Note(velocity=80, pitch=58, start=2.0, end=2.375),
    # B2 (chromatic approach) on & of 2
    pretty_midi.Note(velocity=70, pitch=57, start=2.375, end=2.5),
    # F2 (root) on beat 3
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.875),
    # G2 (chromatic approach) on & of 3
    pretty_midi.Note(velocity=70, pitch=54, start=2.875, end=3.0),
    # C3 (fifth) on beat 4
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),
    # B2 (chromatic approach) on & of 4
    pretty_midi.Note(velocity=70, pitch=57, start=3.375, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + 0.375),  # F (MIDI 65)
    pretty_midi.Note(velocity=80, pitch=68, start=1.5, end=1.5 + 0.375),  # A
    pretty_midi.Note(velocity=70, pitch=72, start=1.5, end=1.5 + 0.375),  # C
    pretty_midi.Note(velocity=60, pitch=76, start=1.5, end=1.5 + 0.375),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.0 + 0.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.0 + 0.375),  # Bb
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.0 + 0.375),  # D
    pretty_midi.Note(velocity=60, pitch=72, start=3.0, end=3.0 + 0.375),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: C7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.5 + 0.375),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.5 + 0.375),  # E
    pretty_midi.Note(velocity=70, pitch=67, start=4.5, end=4.5 + 0.375),  # G
    pretty_midi.Note(velocity=60, pitch=71, start=4.5, end=4.5 + 0.375),  # B
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (MIDI 65), A (68), C (72), then leave it hanging on the F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # F (leave it hanging)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F (come back)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
