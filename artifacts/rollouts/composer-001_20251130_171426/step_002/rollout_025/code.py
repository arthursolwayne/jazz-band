
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.875), (50, 2.25), (51, 2.625),
    (50, 3.0), (49, 3.375), (48, 3.75), (47, 4.125),
    (46, 4.5), (47, 4.875), (48, 5.25), (49, 5.625)
]
for note, time in bass_notes:
    b = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(b)

# Piano: Diane, 7th chords, comp on 2 and 4 (1.5 to 6.0)
# Fm7 = F, Ab, C, D
# Bbm7 = Bb, Db, F, G
# Ebm7 = Eb, Gb, Bb, C
# Abm7 = Ab, B, Db, E
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (53, 2.25), (50, 2.25), (58, 2.25), (60, 2.25),
    # Bar 3: Bbm7 on beat 2
    (58, 3.375), (55, 3.375), (53, 3.375), (57, 3.375),
    # Bar 4: Ebm7 on beat 2
    (50, 4.5), (47, 4.5), (55, 4.5), (58, 4.5),
    # Bar 4: Abm7 on beat 4
    (53, 5.625), (55, 5.625), (58, 5.625), (60, 5.625)
]
for note, time in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(p)

# Sax: Dante, 4-bar motif, starts at 1.5s
# Start with F, Ab, C, D (Fm7), leave it hanging on Ab
# Then come back on the third bar with a variation
sax_notes = [
    # Bar 2: F, Ab, C, D (Fm7)
    (53, 1.5), (50, 1.5), (58, 1.5), (60, 1.5),
    # Bar 3: F, C, Eb (chromatic approach)
    (53, 3.0), (58, 3.0), (61, 3.0),
    # Bar 4: F, Ab, Bb, C (Fm7 with added Bb)
    (53, 4.5), (50, 4.5), (57, 4.5), (58, 4.5)
]
for note, time in sax_notes:
    s = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(s)

# Drums: Bars 2-4 (1.5 to 6.0)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for bar in range(3):
    for beat in [0, 1, 2, 3]:
        time = bar_start + beat * 1.5
        if beat == 0 or beat == 2:
            dr = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(dr)
        if beat == 1 or beat == 3:
            dr = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(dr)
        for eighth in [0, 1]:
            dr = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.75, end=time + eighth * 0.75 + 0.125)
            drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
