
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
# F7 chord: F A C E
# Bar 2: F A Bb C
# Bar 3: E D C Bb
# Bar 4: A G F E
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [77, 80, 79, 72]  # F A Bb C
    elif bar == 3:
        notes = [71, 69, 72, 79]  # E D C Bb
    elif bar == 4:
        notes = [80, 78, 77, 71]  # A G F E
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on 2 and 4
# Bar 3: E7 on 2 and 4
# Bar 4: A7 on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        chord_notes = [77, 80, 72, 79]  # F7
    elif bar == 3:
        chord_notes = [71, 74, 67, 76]  # E7
    elif bar == 4:
        chord_notes = [80, 83, 75, 82]  # A7
    for i in [1, 3]:
        for pitch in chord_notes:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
            piano.notes.append(note)

# Sax: Motif - F Bb G E, start on 1, leave it hanging
# Bar 2: F Bb G E (start at 0.0)
# Bar 3: F Bb G E (start at 1.5)
# Bar 4: F Bb G E (start at 3.0)
for bar in range(2, 5):
    start = (bar - 2) * 1.5
    notes = [77, 79, 81, 76]  # F Bb G E
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.25)
        sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
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
