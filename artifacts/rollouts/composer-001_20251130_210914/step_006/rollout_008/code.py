
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
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
for bar in range(2, 5):
    start = bar * 1.5
    # F7 chord: F, A, C, E
    # Walking line in F minor with chromatic passing tones
    if bar == 2:
        # F -> Eb -> D -> C -> B -> A -> G -> F
        notes = [71, 70, 69, 68, 67, 66, 65, 64]
    elif bar == 3:
        # Bb -> B -> C -> D -> Eb -> E -> F -> G
        notes = [66, 67, 68, 69, 70, 71, 72, 73]
    elif bar == 4:
        # G -> F -> Eb -> D -> C -> B -> A -> Ab
        notes = [73, 71, 70, 69, 68, 67, 66, 65]
    for i, note in enumerate(notes):
        duration = 0.375
        start_time = start + i * 0.375
        bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + duration)
        bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # F7 = F, A, C, E
    # Bb7 = Bb, D, F, Ab
    # E7 = E, G#, B, D
    if bar == 2:
        chords = [(71, 74, 76, 78), (68, 71, 73, 65)]
    elif bar == 3:
        chords = [(71, 74, 76, 78), (68, 71, 73, 65)]
    elif bar == 4:
        chords = [(71, 74, 76, 78), (68, 71, 73, 65)]
    for i, chord in enumerate(chords):
        duration = 0.75
        start_time = start + i * 0.75
        for note in chord:
            piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start_time, end=start_time + duration)
            piano.notes.append(piano_note)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 motif: F, G, E, D (F - G - E - D)
motif = [71, 72, 74, 73]
for i, note in enumerate(motif):
    start = 1.5 + i * 0.375
    duration = 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# End of motif, leave it hanging
# Then repeat it, but finish it
for i, note in enumerate(motif):
    start = 1.5 + 2.25 + i * 0.375
    duration = 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
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
