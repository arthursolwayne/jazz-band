
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
bar_length = 1.5
for i in range(4):
    time = i * bar_length / 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4, end=time + bar_length / 4 + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 8))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [36, 34, 32, 31, 36, 34, 32, 31, 36, 34, 32, 31, 36, 34, 32, 31]
for i, note in enumerate(bass_notes):
    start_time = 1.5 + (i * bar_length / 4)
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start_time, end=start_time + 0.25))

# Diane: 7th chords on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, Db, F, Ab
# Eb7 = Eb, Gb, Bb, Db
# Ab7 = Ab, B, Eb, Gb
chords = [
    [76, 70, 69, 64],  # Fm7
    [72, 67, 76, 70],  # Bb7
    [69, 64, 72, 67],  # Eb7
    [70, 72, 69, 64]   # Ab7
]
for i, chord in enumerate(chords):
    start_time = 1.5 + (i * bar_length)
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start_time, end=start_time + 0.25))

# Dante: Tenor sax motif
# Start with a short motif that sings, leave it hanging
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Ab, Bb, C
motif = [76, 78, 77, 80]
for i, note in enumerate(motif):
    start_time = 1.5
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.1))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(6):
    time = 1.5 + (i * bar_length / 2)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4, end=time + bar_length / 4 + 0.1))
    for j in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time + j * bar_length / 8, end=time + j * bar_length / 8 + 0.05))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
