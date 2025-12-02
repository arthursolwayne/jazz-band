
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
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
for bar in range(2, 5):
    start = bar * 1.5
    # Bass line in D minor, walking
    if bar == 2:
        # Dm7
        notes = [50, 49, 51, 52]  # D, C, Eb, F
    elif bar == 3:
        # G7
        notes = [62, 61, 60, 63]  # G, F, F#, A
    elif bar == 4:
        # Cm7
        notes = [60, 59, 62, 64]  # C, Bb, Db, Eb
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + (i + 1) * 0.375)
        bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        for i, pitch in enumerate([50, 52, 57, 60]):
            note = pretty_midi.Note(velocity=95, pitch=pitch, start=start + (i % 2) * 0.75, end=start + (i % 2) * 0.75 + 0.375)
            piano.notes.append(note)
    elif bar == 3:
        # G7: G, B, D, F
        for i, pitch in enumerate([62, 67, 67, 69]):
            note = pretty_midi.Note(velocity=95, pitch=pitch, start=start + (i % 2) * 0.75, end=start + (i % 2) * 0.75 + 0.375)
            piano.notes.append(note)
    elif bar == 4:
        # Cm7: C, Eb, G, Bb
        for i, pitch in enumerate([60, 64, 67, 69]):
            note = pretty_midi.Note(velocity=95, pitch=pitch, start=start + (i % 2) * 0.75, end=start + (i % 2) * 0.75 + 0.375)
            piano.notes.append(note)

# Dante on sax: 4-bar motif, short and singable
# Dm7 -> G7 -> Cm7 -> Dm7
# Motif: D - F - A - C (Dm7)
# Then, G - B - D - F (G7)
# Then, C - Eb - G - Bb (Cm7)
# Then, D - F - A - C (Dm7 again)

for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        for i, pitch in enumerate([50, 52, 57, 60]):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + (i + 1) * 0.375)
            sax.notes.append(note)
    elif bar == 3:
        # G7: G, B, D, F
        for i, pitch in enumerate([62, 67, 67, 69]):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + (i + 1) * 0.375)
            sax.notes.append(note)
    elif bar == 4:
        # Cm7: C, Eb, G, Bb
        for i, pitch in enumerate([60, 64, 67, 69]):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + (i + 1) * 0.375)
            sax.notes.append(note)

# Add the drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
