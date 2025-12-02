
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),   # G#
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
# Chord progression: F7, Bb7, E7, A7
# Bar 2 (1.5 - 3.0): F7 (F A C Eb)
# Bar 3 (3.0 - 4.5): Bb7 (Bb D F Ab)
# Bar 4 (4.5 - 6.0): E7 (E G# B D)
for bar in range(2, 4):
    start = bar * 1.5
    if bar % 2 == 1:
        if bar == 2:
            # F7
            notes = [53, 58, 60, 57]
        elif bar == 3:
            # Bb7
            notes = [56, 61, 63, 60]
        elif bar == 4:
            # E7
            notes = [64, 69, 71, 68]
        for note in notes:
            piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.75))

# Drums: continue with same pattern
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax (Dante): one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# First motif in bar 2: F, Ab, A, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=58, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=2.5, end=2.75),  # F (rest)
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),  # F (come back)
    pretty_midi.Note(velocity=110, pitch=57, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=58, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=53, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),  # F (rest)
    pretty_midi.Note(velocity=110, pitch=53, start=5.0, end=5.25),  # F (come back)
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=58, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=53, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
