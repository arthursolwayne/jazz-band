
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (37) -> C (40) -> F (37) -> C (40)
    pretty_midi.Note(velocity=70, pitch=37, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=37, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=40, start=2.625, end=3.0),
    # Bar 3: Bb (39) -> F (37) -> Bb (39) -> F# (41)
    pretty_midi.Note(velocity=70, pitch=39, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=37, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=39, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=41, start=4.125, end=4.5),
    # Bar 4: A (41) -> D (38) -> A (41) -> G (42)
    pretty_midi.Note(velocity=70, pitch=41, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=70, pitch=41, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.5 + 0.75),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.5 + 0.75),  # A (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.75),  # C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.75),  # E (MIDI 64)
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.0 + 0.75),  # Bb (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.0 + 0.75),  # D (MIDI 55)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.0 + 0.75),  # F (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.75),  # Ab (MIDI 62)
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.5 + 0.75),  # A (MIDI 61)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.75),  # C (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.75),  # E (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.5 + 0.75),  # G (MIDI 69)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it
# Motif: F (60) -> G (62) -> A (64) -> F (60) (Bar 2)
# Then F (60) -> Ab (62)? -> A (64) -> C (65) (Bar 4)
sax_notes = [
    # Bar 2: F -> G -> A -> F
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=62, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=60, start=2.0625, end=2.25),
    # Bar 3: Silence (no note)
    # Bar 4: F -> Ab -> A -> C
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=65, start=5.0625, end=5.25)
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick
    pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=95, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=95, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875)

drums.notes.extend([n for n in drums.notes if n not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
