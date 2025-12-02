
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
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
        drums.notes.append(note)

# Bars 2-4: Full quartet
# Bar 2: Bass walks in, piano comps, sax starts motif
# Bass: F - G - Ab - A, then A - Bb - B - C
# Piano: 7th chords on 2 and 4
# Sax: F - Bb - D - G (motif)

# Bar 2 (1.5 - 3.0s)
# Bass
for i, pitch in enumerate([71, 72, 70, 71]):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=1.5 + i * bar_length / 4, end=1.5 + (i + 1) * bar_length / 4)
    bass.notes.append(note)

# Piano
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + bar_length / 2)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=73, start=1.5 + bar_length / 2, end=1.5 + bar_length)
piano.notes.append(note)

# Sax motif
note = pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.5 + bar_length / 4)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=88, start=1.5 + bar_length / 4, end=1.5 + bar_length / 2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=91, start=1.5 + bar_length / 2, end=1.5 + 3 * bar_length / 4)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=96, start=1.5 + 3 * bar_length / 4, end=1.5 + bar_length)
sax.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# Bass: A - Bb - B - C, then C - D - Eb - F
# Piano: 7th chords on 2 and 4
# Sax: repeat the motif

# Bass
for i, pitch in enumerate([71, 70, 71, 72]):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=3.0 + i * bar_length / 4, end=3.0 + (i + 1) * bar_length / 4)
    bass.notes.append(note)

# Piano
note = pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.0 + bar_length / 2)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=75, start=3.0 + bar_length / 2, end=3.0 + bar_length)
piano.notes.append(note)

# Sax motif
note = pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.0 + bar_length / 4)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=88, start=3.0 + bar_length / 4, end=3.0 + bar_length / 2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=91, start=3.0 + bar_length / 2, end=3.0 + 3 * bar_length / 4)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=96, start=3.0 + 3 * bar_length / 4, end=3.0 + bar_length)
sax.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Bass: C - D - Eb - F, then F - G - Ab - A
# Piano: 7th chords on 2 and 4
# Sax: repeat the motif, then leave it hanging

# Bass
for i, pitch in enumerate([72, 74, 73, 71]):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=4.5 + i * bar_length / 4, end=4.5 + (i + 1) * bar_length / 4)
    bass.notes.append(note)

# Piano
note = pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=4.5 + bar_length / 2)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5 + bar_length / 2, end=4.5 + bar_length)
piano.notes.append(note)

# Sax motif
note = pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.5 + bar_length / 4)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=88, start=4.5 + bar_length / 4, end=4.5 + bar_length / 2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=91, start=4.5 + bar_length / 2, end=4.5 + 3 * bar_length / 4)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=96, start=4.5 + 3 * bar_length / 4, end=4.5 + bar_length)
sax.notes.append(note)

# Drums for Bars 2-4
for bar in range(2, 5):
    start_time = bar * bar_length
    for beat in range(4):
        time = start_time + beat * bar_length / 4
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
