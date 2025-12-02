
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
# C7 -> Bb7 -> Am7 -> D7
for bar in range(2, 5):
    start = bar * 1.5
    root = 60  # C
    if bar == 2:
        # C7 chord: C, E, B, Bb
        chromatic_notes = [60, 61, 62, 63, 64, 65, 66, 67]
        bass_notes = [60, 61, 62, 63]
    elif bar == 3:
        # Bb7 chord: Bb, D, F, Ab
        chromatic_notes = [59, 60, 61, 62, 63, 64, 65, 66]
        bass_notes = [59, 60, 61, 62]
    elif bar == 4:
        # Am7 chord: A, C, E, G
        chromatic_notes = [57, 58, 59, 60, 61, 62, 63, 64]
        bass_notes = [57, 58, 59, 60]
    # Walking line
    for i in range(4):
        note = bass_notes[i]
        duration = 0.375
        bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start + i * duration, end=start + (i + 1) * duration)
        bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # C7: C, E, B, Bb
        chords = [60, 64, 67, 62]
    elif bar == 3:
        # Bb7: Bb, D, F, Ab
        chords = [59, 62, 65, 57]
    elif bar == 4:
        # Am7: A, C, E, G
        chords = [57, 60, 64, 67]
    # Play on 2 and 4
    for i in [1, 3]:
        for note in chords:
            duration = 0.375
            piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start + i * duration, end=start + (i + 1) * duration)
            piano.notes.append(piano_note)

# Sax: Motif - start it, leave it hanging, come back and finish
motif = [62, 60, 62, 64]  # G, E, G, A
for i in range(4):
    note = motif[i]
    duration = 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=1.5 + i * duration, end=1.5 + (i + 1) * duration)
    sax.notes.append(sax_note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
