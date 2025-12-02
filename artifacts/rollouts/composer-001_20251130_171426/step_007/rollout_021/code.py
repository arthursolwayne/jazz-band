
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
# Start with sax melody, 4 bars in Fm, 160 BPM

# Bass: Walking line in Fm, chromatic approaches
notes = [35, 37, 38, 39, 37, 35, 33, 32, 35, 37, 38, 39, 37, 35, 33, 32]
time = 1.5
for note in notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)
    time += 0.375

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 (F, Ab, Bb, C)
# Bb7 (Bb, D, F, Ab)
# Eb7 (Eb, G, Bb, Db)
# Ab7 (Ab, C, Eb, G)
chords = [
    [53, 55, 57, 60],  # Fm7
    [57, 59, 62, 65],  # Bb7
    [50, 52, 57, 60],  # Eb7
    [55, 57, 60, 64],  # Ab7
]
time = 1.5
for i in range(4):
    chord = chords[i]
    for note in chord:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
        piano.notes.append(piano_note)
    time += 1.5

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C (no B), C
# Motif: F - Bb - Ab - F (4 notes)
# Bar 2: F, Bb, Ab, F
# Bar 3: Rest
# Bar 4: F, Bb, Ab, F
# Bar 5: F, Bb, Ab, F

sax_notes = [
    [53, 57, 55, 53],  # F, Bb, Ab, F
    [53, 57, 55, 53],  # F, Bb, Ab, F
    [53, 57, 55, 53],  # F, Bb, Ab, F
]

time = 1.5
for i in range(3):
    for note in sax_notes[i]:
        sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
        sax.notes.append(sax_note)
        time += 0.375
    time += 0.375  # Rest between phrases

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
