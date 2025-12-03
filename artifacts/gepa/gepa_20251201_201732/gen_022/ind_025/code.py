
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 1.5)
    hihat.duration = 1.5
    hihat.note_on = 0
    hihat.note_off = 1.5
    # Add to drums instrument
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
# Bar 2: Fm7 -> Bb7 (F, C, Ab, D)
# Bar 3: Cm7 -> F7 (C, G, Eb, A)
# Bar 4: Bb7 -> Eb7 (Bb, F, Db, G)
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    if bar == 2:
        # Fm7 (F, Ab, D, C) -> root F (38), 5th C (43)
        root = pretty_midi.Note(velocity=80, pitch=38, start=start, end=start + 0.375)
        fifth = pretty_midi.Note(velocity=80, pitch=43, start=start + 0.375, end=start + 0.75)
        # Chromatic approach to F
        chromatic = pretty_midi.Note(velocity=70, pitch=37, start=start + 0.75, end=start + 1.125)
        bass.notes.extend([root, fifth, chromatic])
    elif bar == 3:
        # Cm7 (C, Eb, G, Bb) -> root C (40), 5th G (47)
        root = pretty_midi.Note(velocity=80, pitch=40, start=start, end=start + 0.375)
        fifth = pretty_midi.Note(velocity=80, pitch=47, start=start + 0.375, end=start + 0.75)
        # Chromatic approach to C
        chromatic = pretty_midi.Note(velocity=70, pitch=39, start=start + 0.75, end=start + 1.125)
        bass.notes.extend([root, fifth, chromatic])
    elif bar == 4:
        # Bb7 (Bb, D, F, Ab) -> root Bb (42), 5th F (43)
        root = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
        fifth = pretty_midi.Note(velocity=80, pitch=43, start=start + 0.375, end=start + 0.75)
        # Chromatic approach to Bb
        chromatic = pretty_midi.Note(velocity=70, pitch=41, start=start + 0.75, end=start + 1.125)
        bass.notes.extend([root, fifth, chromatic])

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Fm7 (F, Ab, D, C)
# Bar 3: Cm7 (C, Eb, G, Bb)
# Bar 4: Bb7 (Bb, D, F, Ab)
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    if bar == 2:
        # Fm7 (F, Ab, D, C)
        note1 = pretty_midi.Note(velocity=90, pitch=53, start=start, end=start + 0.75)
        note2 = pretty_midi.Note(velocity=90, pitch=51, start=start, end=start + 0.75)
        note3 = pretty_midi.Note(velocity=90, pitch=49, start=start, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=90, pitch=48, start=start, end=start + 0.75)
        piano.notes.extend([note1, note2, note3, note4])
    elif bar == 3:
        # Cm7 (C, Eb, G, Bb)
        note1 = pretty_midi.Note(velocity=90, pitch=60, start=start, end=start + 0.75)
        note2 = pretty_midi.Note(velocity=90, pitch=58, start=start, end=start + 0.75)
        note3 = pretty_midi.Note(velocity=90, pitch=57, start=start, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=90, pitch=55, start=start, end=start + 0.75)
        piano.notes.extend([note1, note2, note3, note4])
    elif bar == 4:
        # Bb7 (Bb, D, F, Ab)
        note1 = pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.75)
        note2 = pretty_midi.Note(velocity=90, pitch=59, start=start, end=start + 0.75)
        note3 = pretty_midi.Note(velocity=90, pitch=57, start=start, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=90, pitch=55, start=start, end=start + 0.75)
        piano.notes.extend([note1, note2, note3, note4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 1.5)
    hihat.duration = 1.5
    hihat.note_on = 0
    hihat.note_off = 1.5
    # Add to drums instrument
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat])

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Start on F (65), move to Ab (64), then to D (62) — F, Ab, D — the first 3 notes of the Fm scale
# Leave it hanging on the third beat, and finish it on the fourth beat.
# Play this motif on bar 2, beat 1 and bar 4, beat 1

# Bar 2, beat 1: F (65)
note_f = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875)
sax.notes.append(note_f)

# Bar 2, beat 2: Ab (64)
note_ab = pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625)
sax.notes.append(note_ab)

# Bar 2, beat 3: D (62)
note_d = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375)
sax.notes.append(note_d)

# Bar 4, beat 1: F (65) again, completing the motif
note_f2 = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875)
sax.notes.append(note_f2)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
