
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
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
for bar in range(2, 5):
    start_time = bar * 1.5
    # F bass line: F, Gb, G, Ab, A, Bb, B, C, etc.
    # Walking line with chromatic approaches
    if bar == 2:
        notes = [78, 77, 79, 78, 80, 79, 81, 80]
    elif bar == 3:
        notes = [80, 81, 79, 80, 78, 79, 77, 78]
    elif bar == 4:
        notes = [77, 78, 79, 80, 81, 82, 80, 81]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.1875)
        bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start_time = bar * 1.5
    if bar == 2:
        # F7 on beat 2
        notes = [79, 82, 81, 84]
        for i, pitch in enumerate(notes):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time + 0.75, end=start_time + 0.75 + 0.1875)
            piano.notes.append(note)
    elif bar == 3:
        # G7 on beat 2
        notes = [80, 83, 82, 85]
        for i, pitch in enumerate(notes):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time + 0.75, end=start_time + 0.75 + 0.1875)
            piano.notes.append(note)
    elif bar == 4:
        # C7 on beat 2
        notes = [84, 87, 86, 89]
        for i, pitch in enumerate(notes):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time + 0.75, end=start_time + 0.75 + 0.1875)
            piano.notes.append(note)

# Dante: Tenor sax motif
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (82, 0.0, 0.375),    # F
    (84, 0.375, 0.75),   # A
    (82, 0.75, 1.125),   # F
    # Bar 3
    (84, 1.5, 1.875),    # A
    (82, 1.875, 2.25),   # F
    (84, 2.25, 2.625),   # A
    (86, 2.625, 3.0),    # C
    # Bar 4
    (82, 3.0, 3.375),    # F
    (84, 3.375, 3.75),   # A
    (82, 3.75, 4.125),   # F
    (84, 4.125, 4.5),    # A
    (86, 4.5, 4.875),    # C
    (84, 4.875, 5.25),   # A
    (82, 5.25, 5.625),   # F
    (80, 5.625, 6.0)     # D
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + 1.5, end=end + 1.5)
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
