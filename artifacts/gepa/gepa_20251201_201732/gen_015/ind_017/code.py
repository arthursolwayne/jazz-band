
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Ab (E2)
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # G (D#2)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # Bb (F2)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C (G2)
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # B (F#2)
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),  # Db (A2)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # C (G2)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # Ab (E2)
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625),  # G (D#2)
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # Bb (F2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=2.25),  # Ab (A3)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.25),  # C (E4)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),  # D (F4)
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=3.0),  # Bb (B3)
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=3.0),  # D (C4)
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=3.0),  # Ab (A3)
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75),  # C (E4)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.75),  # Eb (C4)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),  # G (F4)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75),  # Bb (B3)
])
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
drums.notes.extend(drum_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: F, Ab, Bb, G (C4, E3, F3, D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # F (C4)
    pretty_midi.Note(velocity=110, pitch=57, start=1.875, end=2.25),  # Ab (F3)
    pretty_midi.Note(velocity=110, pitch=59, start=2.25, end=2.625),  # Bb (G3)
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # G (D4)
]
# Leave it hanging, then come back and finish it
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875))  # F (C4)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=57, start=4.875, end=5.25))  # Ab (F3)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=5.625))  # Bb (G3)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0))  # G (D4)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
