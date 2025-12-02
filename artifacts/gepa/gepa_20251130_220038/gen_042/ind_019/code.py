
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

# Bass line (Marcus)
for bar in range(2, 5):
    start = bar * 1.5
    # Walking line with chromatic approaches
    # Dm7 (D F A C)
    # Root on 1, 5, 3, 7
    bass_notes = [50, 53, 52, 55]
    for i in range(4):
        note_start = start + i * 0.375
        note = pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=note_start, end=note_start + 0.375)
        bass.notes.append(note)

# Piano (Diane)
for bar in range(2, 5):
    start = bar * 1.5
    # 7th chords, comp on 2 and 4
    if bar == 2:
        # Dm7: D F A C
        # Comp on 2 and 4
        chord_notes = [50, 53, 55, 57]
    elif bar == 3:
        # G7: G B D F
        chord_notes = [62, 65, 67, 69]
    else:
        # Cmaj7: C E G B
        chord_notes = [60, 64, 67, 71]
    for i in range(2, 5, 2):
        note_start = start + i * 0.375
        for pitch in chord_notes:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=note_start, end=note_start + 0.125)
            piano.notes.append(note)

# Sax (Dante)
# Motif: D - F - A - ?
# Start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

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
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_introduction.mid')
