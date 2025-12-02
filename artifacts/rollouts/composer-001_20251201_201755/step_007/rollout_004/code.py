
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3 (beats 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4 (beats 1 and 3)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F - G - A - Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # Bb
]
# Bar 3: Bb - C - D - Eb
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # Eb
])
# Bar 4: Eb - F - G - A
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # A
])
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875),  # E
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # Db
])
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3 (beats 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4 (beats 1 and 3)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (60) -> G (62) -> Bb (62), then resolve with a descending line
# Bar 2: F, G, Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # Bb
]
# Bar 3: Rest
# Bar 4: F, G, Bb again, but with a slight variation
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # Bb
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
