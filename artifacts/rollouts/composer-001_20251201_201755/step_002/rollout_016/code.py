
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches (Bar 2: Fm7)
bass_notes = [
    # Bar 2: Fm7 (F, C, Ab, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=2.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.25),  # Bb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # C2
    # Bar 3: Bb7 (Bb, F, D, Ab)
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.75),  # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=3.0),  # F2
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),  # Ab2
    # Bar 4: Eb7 (Eb, Bb, G, Db)
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.75),  # Eb2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # Bb2
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25),  # C2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=54, start=4.25, end=4.5),  # Db2
    # Bar 4 (end): E7 (E, B, G#, D)
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.75),  # E2
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # B2
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.25),  # C2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.75),  # Ab3
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Eb4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # Bb3
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.75),  # Ab4

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Eb3
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # D4
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Bar 2
for i in range(0, 6):
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 0.125, end=1.5 + i * 0.125 + 0.125)
for i in [0, 2]:
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 0.5, end=1.5 + i * 0.5 + 0.375)
for i in [1, 3]:
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 0.5, end=1.5 + i * 0.5 + 0.125)

# Bar 3
for i in range(0, 6):
    pretty_midi.Note(velocity=100, pitch=42, start=2.5 + i * 0.125, end=2.5 + i * 0.125 + 0.125)
for i in [0, 2]:
    pretty_midi.Note(velocity=100, pitch=36, start=2.5 + i * 0.5, end=2.5 + i * 0.5 + 0.375)
for i in [1, 3]:
    pretty_midi.Note(velocity=100, pitch=38, start=2.5 + i * 0.5, end=2.5 + i * 0.5 + 0.125)

# Bar 4
for i in range(0, 6):
    pretty_midi.Note(velocity=100, pitch=42, start=3.5 + i * 0.125, end=3.5 + i * 0.125 + 0.125)
for i in [0, 2]:
    pretty_midi.Note(velocity=100, pitch=36, start=3.5 + i * 0.5, end=3.5 + i * 0.5 + 0.375)
for i in [1, 3]:
    pretty_midi.Note(velocity=100, pitch=38, start=3.5 + i * 0.5, end=3.5 + i * 0.5 + 0.125)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
# Fm7 (F, Ab, C, Eb) - play F, Ab
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=105, pitch=80, start=1.75, end=2.0),  # Ab4

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.5),  # F4

    # Bar 4: Come back and finish the motif
    pretty_midi.Note(velocity=110, pitch=77, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=105, pitch=80, start=3.75, end=4.0),  # Ab4
    pretty_midi.Note(velocity=110, pitch=81, start=4.0, end=4.25),  # Bb4
    pretty_midi.Note(velocity=105, pitch=79, start=4.25, end=4.5),  # G4
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=105, pitch=80, start=4.75, end=5.0),  # Ab4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
