
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

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
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # C7 -> Bb -> C -> D
        notes = [60, 59, 60, 62]
    elif bar == 3:
        # D -> Eb -> D -> E
        notes = [62, 63, 62, 64]
    elif bar == 4:
        # E -> F -> E -> F#
        notes = [64, 65, 64, 66]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2: C7 on beat 2
    if bar == 2:
        piano_notes = [60, 64, 67, 71]
        for i, pitch in enumerate(piano_notes):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.375, end=start + 0.75)
            piano.notes.append(note)
    # Bar 3: D7 on beat 2
    elif bar == 3:
        piano_notes = [62, 66, 69, 73]
        for i, pitch in enumerate(piano_notes):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.375, end=start + 0.75)
            piano.notes.append(note)
    # Bar 4: E7 on beat 2
    elif bar == 4:
        piano_notes = [64, 68, 71, 75]
        for i, pitch in enumerate(piano_notes):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.375, end=start + 0.75)
            piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C -> Bb -> C -> D (bar 2)
# D -> E -> D -> F (bar 3)
# E -> F -> E -> G (bar 4)

for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        sax_notes = [60, 59, 60, 62]
    elif bar == 3:
        sax_notes = [62, 64, 62, 65]
    elif bar == 4:
        sax_notes = [64, 65, 64, 67]
    for i, pitch in enumerate(sax_notes):
        note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("jazz_intro.mid")
