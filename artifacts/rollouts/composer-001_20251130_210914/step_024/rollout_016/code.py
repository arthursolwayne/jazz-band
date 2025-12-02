
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
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7 = D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D -> Eb -> F -> G -> A -> Bb -> B -> C
bass_notes = [62, 63, 64, 65, 67, 68, 69, 71, 62, 63, 64, 65, 67, 68, 69, 71]
bass_durations = [0.375] * 16
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + bass_durations[i])
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4 (Dm7, Gm7, Cm7, F7)
# Bars 2: Dm7 (D F A C)
# Bar 3: Gm7 (G Bb D F)
# Bar 4: Cm7 (C Eb G Bb)
# Bar 5: F7 (F A C E)
for bar in range(2, 6):
    start = (bar - 2) * 1.5
    if bar == 2:
        # Dm7 on 2 and 4
        notes = [62, 66, 69, 72]
    elif bar == 3:
        # Gm7 on 2 and 4
        notes = [67, 71, 69, 72]
    elif bar == 4:
        # Cm7 on 2 and 4
        notes = [60, 64, 67, 70]
    elif bar == 5:
        # F7 on 2 and 4
        notes = [65, 68, 72, 76]
    for i, note in enumerate(notes):
        # Play on 2 and 4
        if i == 0:
            time = start + 0.375
        else:
            time = start + 1.125
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
        piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D Eb F G A Bb B C
# Motif: D -> Eb -> F -> D (staccato)
# Then A -> Bb -> C -> A (legato)
# Total 8 notes over 4 bars (each note = 0.375s)
sax_notes = [62, 63, 64, 62, 67, 68, 71, 67]
sax_velocities = [100, 100, 100, 100, 100, 100, 100, 100]
sax_durations = [0.1875, 0.1875, 0.1875, 0.1875, 0.375, 0.375, 0.375, 0.375]
for i, note in enumerate(sax_notes):
    start = 1.5 + i * 0.375
    sax_note = pretty_midi.Note(velocity=sax_velocities[i], pitch=note, start=start, end=start + sax_durations[i])
    sax.notes.append(sax_note)

# Drums for bars 2-4
for bar in range(2, 6):
    start = (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
