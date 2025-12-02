
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
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7 chord: D, F, A, C
        # Walking line starting on D
        notes = [pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D
                 pretty_midi.Note(velocity=90, pitch=63, start=start + 0.375, end=start + 0.75),  # Eb
                 pretty_midi.Note(velocity=90, pitch=62, start=start + 0.75, end=start + 1.125),  # D
                 pretty_midi.Note(velocity=90, pitch=60, start=start + 1.125, end=start + 1.5)]  # C
    elif bar == 3:
        notes = [pretty_midi.Note(velocity=90, pitch=60, start=start, end=start + 0.375),  # C
                 pretty_midi.Note(velocity=90, pitch=62, start=start + 0.375, end=start + 0.75),  # D
                 pretty_midi.Note(velocity=90, pitch=63, start=start + 0.75, end=start + 1.125),  # Eb
                 pretty_midi.Note(velocity=90, pitch=64, start=start + 1.125, end=start + 1.5)]  # E
    else:  # bar == 4
        notes = [pretty_midi.Note(velocity=90, pitch=64, start=start, end=start + 0.375),  # E
                 pretty_midi.Note(velocity=90, pitch=62, start=start + 0.375, end=start + 0.75),  # D
                 pretty_midi.Note(velocity=90, pitch=60, start=start + 0.75, end=start + 1.125),  # C
                 pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5)]  # D
    bass.notes.extend(notes)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        # Comp on beat 2 and 4
        note2 = pretty_midi.Note(velocity=95, pitch=62, start=start + 0.375, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=95, pitch=62, start=start + 1.125, end=start + 1.5)
    elif bar == 3:
        # G7: G, B, D, F
        note2 = pretty_midi.Note(velocity=95, pitch=67, start=start + 0.375, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=95, pitch=67, start=start + 1.125, end=start + 1.5)
    else:  # bar == 4
        # Cmaj7: C, E, G, B
        note2 = pretty_midi.Note(velocity=95, pitch=60, start=start + 0.375, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=95, pitch=60, start=start + 1.125, end=start + 1.5)
    piano.notes.extend([note2, note4])

# Sax: Melody, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), A (69), D (62) in bar 2
# Repeat and resolve in bar 4

# Bar 2
start = 1.5
note1 = pretty_midi.Note(velocity=105, pitch=62, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=105, pitch=65, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=105, pitch=69, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=105, pitch=62, start=start + 1.125, end=start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Rest, leave it hanging
start = 3.0
note_rest = pretty_midi.Note(velocity=0, pitch=62, start=start, end=start + 1.5)
sax.notes.append(note_rest)

# Bar 4: Repeat motif and resolve
start = 4.5
note1 = pretty_midi.Note(velocity=105, pitch=62, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=105, pitch=65, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=105, pitch=69, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=105, pitch=62, start=start + 1.125, end=start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
