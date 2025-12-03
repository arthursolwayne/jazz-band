
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
    # Hi-hat on every eighth
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

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), G (fifth), E (chromatic approach to F), F (root)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=73, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # E2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # F2
    # Bar 3: A (root), B (fifth), G# (chromatic approach to A), A
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=90, pitch=75, start=3.75, end=4.125),  # G#2
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # A2
    # Bar 4: C (root), D (fifth), B (chromatic approach to C), C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625),  # B2
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F2
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # A2
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # C2
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=2.0),  # E2
]
# Bar 3: Amaj7 (A, C#, E, G#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),  # A2
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.5),  # C#2
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.5),  # E2
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.5),  # G#2
])
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # C2
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=5.0),  # E2
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=5.0),  # G2
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=5.0),  # B2
])
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=2.25),  # F2 (half note)
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.5),  # Bb2 (quarter note)
    pretty_midi.Note(velocity=110, pitch=76, start=2.5, end=2.625),  # C2 (eighth note)
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.75),  # F2 (eighth note)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
