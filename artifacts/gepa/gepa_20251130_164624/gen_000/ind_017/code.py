
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, Fm7 -> Bb7 -> Eb7 -> Am7
# Fm7: F, Ab, Db, Eb
# Bb7: Bb, D, F, Ab
# Eb7: Eb, G, Bb, Db
# Am7: A, C, E, G
for bar in range(2, 5):
    start = bar * 1.5
    # Walking bass line
    # Fm -> Bb -> Eb -> Am
    if bar == 2:
        notes = [pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=100, pitch=61, start=start + 0.375, end=start + 0.75),  # Ab
                 pretty_midi.Note(velocity=100, pitch=58, start=start + 0.75, end=start + 1.125),  # Db
                 pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)]  # Eb
    elif bar == 3:
        notes = [pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # Bb
                 pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75),  # D
                 pretty_midi.Note(velocity=100, pitch=64, start=start + 0.75, end=start + 1.125),  # F
                 pretty_midi.Note(velocity=100, pitch=61, start=start + 1.125, end=start + 1.5)]  # Ab
    elif bar == 4:
        notes = [pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # Eb
                 pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75),  # G
                 pretty_midi.Note(velocity=100, pitch=62, start=start + 0.75, end=start + 1.125),  # Bb
                 pretty_midi.Note(velocity=100, pitch=58, start=start + 1.125, end=start + 1.5)]  # Db
    bass.notes.extend(notes)

# Diane: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Db, Eb
# Bb7: Bb, D, F, Ab
# Eb7: Eb, G, Bb, Db
# Am7: A, C, E, G
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7 on beat 2
        notes = [pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75),  # F
                 pretty_midi.Note(velocity=100, pitch=61, start=start + 0.375, end=start + 0.75),  # Ab
                 pretty_midi.Note(velocity=100, pitch=58, start=start + 0.375, end=start + 0.75),  # Db
                 pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)]  # Eb
    elif bar == 3:
        # Bb7 on beat 2
        notes = [pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # Bb
                 pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75),  # D
                 pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75),  # F
                 pretty_midi.Note(velocity=100, pitch=61, start=start + 0.375, end=start + 0.75)]  # Ab
    elif bar == 4:
        # Eb7 on beat 2
        notes = [pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # Eb
                 pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75),  # G
                 pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # Bb
                 pretty_midi.Note(velocity=100, pitch=58, start=start + 0.375, end=start + 0.75)]  # Db
    piano.notes.extend(notes)

# You: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm: F, Ab, Db, Eb
# Motif: F - Ab - Db - Eb (half note on F, quarter on Ab, eighth on Db, quarter on Eb)
# Then rest for a beat, then repeat the motif in Eb
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # First motif: F - Ab - Db - Eb
        notes = [pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75),  # F (half note)
                 pretty_midi.Note(velocity=100, pitch=61, start=start + 0.75, end=start + 1.125),  # Ab (quarter)
                 pretty_midi.Note(velocity=100, pitch=58, start=start + 1.125, end=start + 1.375),  # Db (eighth)
                 pretty_midi.Note(velocity=100, pitch=62, start=start + 1.375, end=start + 1.5)]  # Eb (eighth)
        sax.notes.extend(notes)
    elif bar == 4:
        # Second motif in Eb
        notes = [pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75),  # Eb (half note)
                 pretty_midi.Note(velocity=100, pitch=67, start=start + 0.75, end=start + 1.125),  # G (quarter)
                 pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.375),  # Bb (eighth)
                 pretty_midi.Note(velocity=100, pitch=58, start=start + 1.375, end=start + 1.5)]  # Db (eighth)
        sax.notes.extend(notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
