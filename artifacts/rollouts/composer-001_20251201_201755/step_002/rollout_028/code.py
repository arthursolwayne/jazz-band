
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Root and fifth with chromatic approach
# D2 (D2) -> D2 (root), A2 (fifth), C#2 (chromatic approach), D2 (root)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.6875),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875), # A2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0625), # C#2
    pretty_midi.Note(velocity=90, pitch=38, start=2.0625, end=2.25)  # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chords each bar, resolve on last
# Bar 2: Dmaj7 (F#-A-D-F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875),  # F#
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (B-D-G-B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.4375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),  # B
]
piano.notes.extend(piano_notes)

# Bar 4: Cmaj7 (E-G-C-E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.1875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # E
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, start it, leave it hanging, come back and finish it
# Motif: D4 (start on beat 1), Bb4 (beat 2), D4 (beat 3), leave it hanging on beat 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.4375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
