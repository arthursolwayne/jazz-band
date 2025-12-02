
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
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Fm, chromatic approaches
bass_notes = [
    (14, 1.5, 0.375), (13, 1.875, 0.375), (15, 2.25, 0.375), (12, 2.625, 0.375),  # Bar 2
    (11, 3.0, 0.375), (12, 3.375, 0.375), (13, 3.75, 0.375), (14, 4.125, 0.375),  # Bar 3
    (15, 4.5, 0.375), (16, 4.875, 0.375), (14, 5.25, 0.375), (13, 5.625, 0.375)   # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (33, 1.875, 0.375), (37, 1.875, 0.375), (39, 1.875, 0.375), (42, 1.875, 0.375),  # F7 on 2
    (33, 3.375, 0.375), (37, 3.375, 0.375), (39, 3.375, 0.375), (42, 3.375, 0.375),  # F7 on 4
    (33, 4.875, 0.375), (37, 4.875, 0.375), (39, 4.875, 0.375), (42, 4.875, 0.375)   # F7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm (F, Ab, Bb, Eb), start on bar 2, leave it hanging, come back on bar 4
sax_notes = [
    (34, 1.5, 0.375), (31, 1.875, 0.375), (32, 2.25, 0.375), (30, 2.625, 0.375),  # Bar 2
    (34, 4.5, 0.375), (31, 4.875, 0.375), (32, 5.25, 0.375), (30, 5.625, 0.375)   # Bar 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue for bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    for i in range(4):
        time = bar_start + i * 0.375
        if i == 0 or i == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
        elif i == 1 or i == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))
        if i % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1875))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
