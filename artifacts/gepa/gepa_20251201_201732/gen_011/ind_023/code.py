
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
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Marcus - walking line, roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7 - D, A, root
        notes = [(D2, 0.375), (F1, 0.375), (D2, 0.375), (G2, 0.375)]
    elif bar == 3:
        # G7 - G, D, chromatic approach
        notes = [(G2, 0.375), (F2, 0.375), (G2, 0.375), (D3, 0.375)]
    elif bar == 4:
        # Cmaj7 - C, G, root
        notes = [(C2, 0.375), (E2, 0.375), (C2, 0.375), (G2, 0.375)]
    for pitch, duration in notes:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
        bass.notes.append(note)

# PIANO: Diane - open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7 - D, F, A, C
        notes = [62, 65, 67, 69]
    elif bar == 3:
        # G7 - G, B, D, F
        notes = [67, 71, 69, 65]
    elif bar == 4:
        # Cmaj7 - C, E, G, B
        notes = [60, 64, 67, 71]
    for pitch in notes:
        # Comp on 2 and 4
        if bar % 2 == 1:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.75, end=start + 1.125)
        else:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.375, end=start + 0.75)
        piano.notes.append(note)

# SAX: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 - D, F, Bb, C
# Motif: D - F - Bb - C (quarter notes)
# Start the motif on bar 2, leave it hanging on the third note, come back on bar 4
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875)
sax.notes.extend([note1, note2, note3, note4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
