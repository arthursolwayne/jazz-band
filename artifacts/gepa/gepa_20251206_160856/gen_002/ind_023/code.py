
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: C2 (MIDI 36), chromatic approach to D2 (MIDI 38)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # E
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab
])
# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Bb
])
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend([n for n in drums.notes if n.start >= 1.5])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - G - Bb - F (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
