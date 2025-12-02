
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
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 62, 100), (1.875, 63, 100), (2.25, 60, 100), (2.625, 59, 100),
    # Bar 3
    (3.0, 58, 100), (3.375, 57, 100), (3.75, 60, 100), (4.125, 62, 100),
    # Bar 4
    (4.5, 63, 100), (4.875, 60, 100), (5.25, 62, 100), (5.625, 64, 100)
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    (2.25, 64, 100), (2.25, 67, 100), (2.25, 69, 100), (2.25, 71, 100),
    # Bar 2, beat 4
    (2.625, 64, 100), (2.625, 67, 100), (2.625, 70, 100), (2.625, 72, 100),
    # Bar 3, beat 2
    (3.75, 64, 100), (3.75, 67, 100), (3.75, 69, 100), (3.75, 71, 100),
    # Bar 3, beat 4
    (4.125, 64, 100), (4.125, 67, 100), (4.125, 70, 100), (4.125, 72, 100),
    # Bar 4, beat 2
    (5.25, 64, 100), (5.25, 67, 100), (5.25, 69, 100), (5.25, 71, 100),
    # Bar 4, beat 4
    (5.625, 64, 100), (5.625, 67, 100), (5.625, 70, 100), (5.625, 72, 100)
]
for time, pitch, vel in piano_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Drums: same pattern for bars 2-4
for bar in range(2, 5):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Sax: short motif, leave it hanging
# Fm = F, Ab, Bb, D, Eb
sax_notes = [
    # Bar 2, beat 1 (F)
    (1.5, 65, 110), (1.5, 65, 110),
    # Bar 2, beat 2 (Ab)
    (1.875, 68, 110), (1.875, 68, 110),
    # Bar 2, beat 3 (Bb)
    (2.25, 69, 110), (2.25, 69, 110),
    # Bar 2, beat 4 (leave it hanging)
    (2.625, 65, 110), (2.625, 65, 110),
    # Bar 3, beat 1 (F)
    (3.0, 65, 110), (3.0, 65, 110),
    # Bar 3, beat 2 (D)
    (3.375, 67, 110), (3.375, 67, 110),
    # Bar 3, beat 3 (Eb)
    (3.75, 69, 110), (3.75, 69, 110),
    # Bar 3, beat 4 (leave it hanging)
    (4.125, 65, 110), (4.125, 65, 110),
    # Bar 4, beat 1 (F)
    (4.5, 65, 110), (4.5, 65, 110),
    # Bar 4, beat 2 (Ab)
    (4.875, 68, 110), (4.875, 68, 110),
    # Bar 4, beat 3 (Bb)
    (5.25, 69, 110), (5.25, 69, 110),
    # Bar 4, beat 4 (resolve on Eb)
    (5.625, 69, 110), (5.625, 69, 110)
]
for time, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
