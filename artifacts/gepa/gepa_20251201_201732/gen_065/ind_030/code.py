
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
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Root: F (48), Bb (50), Ab (51), D (52), F (48), Bb (50), Ab (51), D (52)
bass_notes = [
    (48, 1.5, 1.875), (50, 1.875, 2.25), (51, 2.25, 2.625), (52, 2.625, 3.0),
    (48, 3.0, 3.375), (50, 3.375, 3.75), (51, 3.75, 4.125), (52, 4.125, 4.5),
    (48, 4.5, 4.875), (50, 4.875, 5.25), (51, 5.25, 5.625), (52, 5.625, 6.0)
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Ab7 (Ab, C, Eb, F)
# Each chord is voiced in open position with space
# Comp on 2 and 4
def add_piano_notes(start, chord):
    # Chord: root, third, fifth, seventh
    for i, note in enumerate(chord):
        # Spread the voicing
        pitch = note + (i * 12)
        # Note on 2 and 4
        if i == 0:
            note1 = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.75, end=start + 0.75 + 0.375)
            piano.notes.append(note1)
            note2 = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5, end=start + 1.5 + 0.375)
            piano.notes.append(note2)
        else:
            note1 = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 0.75, end=start + 0.75 + 0.375)
            piano.notes.append(note1)
            note2 = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5, end=start + 1.5 + 0.375)
            piano.notes.append(note2)

# Chords
chords = [
    (48, 51, 55, 57),  # Fm7
    (50, 53, 57, 59),  # Bb7
    (51, 54, 58, 60)   # Ab7
]
for i, chord in enumerate(chords):
    add_piano_notes(1.5 + i * 1.5, chord)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (48), G (49), Eb (50), F (48)
# Play on beat 1 of bar 2, then leave it hanging until bar 4
note1 = pretty_midi.Note(velocity=110, pitch=48, start=1.5, end=1.5 + 0.125)
note2 = pretty_midi.Note(velocity=110, pitch=49, start=1.5 + 0.375, end=1.5 + 0.375 + 0.125)
note3 = pretty_midi.Note(velocity=110, pitch=50, start=1.5 + 0.75, end=1.5 + 0.75 + 0.125)
note4 = pretty_midi.Note(velocity=110, pitch=48, start=4.5, end=4.5 + 0.125)
sax.notes.extend([note1, note2, note3, note4])

# Drums: Continue with same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
