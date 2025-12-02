
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
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Marcus - walking line, chromatic approaches, never the same note twice
for bar in range(2, 5):
    start = bar * 1.5
    # Fm bass line: F, Gb, Ab, A, Bb, B, C, Db
    notes = [77, 78, 80, 81, 82, 83, 84, 85]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        bass.notes.append(note)

# PIANO: Diane - 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # Fm7 = F, Ab, Bb, C
    # Bb7 = Bb, Db, E, F
    # Fm7 on beat 2, Bb7 on beat 4
    # comp on beat 2 and 4
    if bar % 2 == 0:
        # Beat 2
        chord = [77, 80, 82, 84]
        for i, pitch in enumerate(chord):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.75, end=start + 0.75 + 0.125)
            piano.notes.append(note)
        # Beat 4
        chord = [82, 85, 87, 77]
        for i, pitch in enumerate(chord):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5, end=start + 1.5 + 0.125)
            piano.notes.append(note)
    else:
        # Beat 2
        chord = [77, 80, 82, 84]
        for i, pitch in enumerate(chord):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.75, end=start + 0.75 + 0.125)
            piano.notes.append(note)
        # Beat 4
        chord = [82, 85, 87, 77]
        for i, pitch in enumerate(chord):
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5, end=start + 1.5 + 0.125)
            piano.notes.append(note)

# SAX: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
bar_start = 1.5
note1 = pretty_midi.Note(velocity=110, pitch=72, start=bar_start + 0.0, end=bar_start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=76, start=bar_start + 0.375, end=bar_start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=73, start=bar_start + 0.75, end=bar_start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=74, start=bar_start + 1.125, end=bar_start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Rest
bar_start = 3.0
# Rest
pass

# Bar 4: Return and finish the motif
bar_start = 4.5
note5 = pretty_midi.Note(velocity=110, pitch=72, start=bar_start + 0.0, end=bar_start + 0.375)
note6 = pretty_midi.Note(velocity=110, pitch=76, start=bar_start + 0.375, end=bar_start + 0.75)
note7 = pretty_midi.Note(velocity=110, pitch=73, start=bar_start + 0.75, end=bar_start + 1.125)
note8 = pretty_midi.Note(velocity=110, pitch=74, start=bar_start + 1.125, end=bar_start + 1.5)
sax.notes.extend([note5, note6, note7, note8])

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
