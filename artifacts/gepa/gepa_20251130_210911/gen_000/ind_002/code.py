
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625), (42, 0.75), (42, 0.9375),
    (36, 1.125), (38, 1.5), (42, 1.125), (42, 1.3125), (42, 1.5)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet
# Diane: 7th chords on 2 and 4
# Bar 2: F7 on beat 2, A7 on beat 4
piano_notes = [
    # F7 (F, A, C, E) on beat 2
    (65, 1.5), (68, 1.5), (60, 1.5), (64, 1.5),
    # A7 (A, C#, E, G) on beat 4
    (69, 1.875), (71, 1.875), (67, 1.875), (70, 1.875)
]
for note, time in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(p)

# Marcus: Walking bass line in F
# F - G - A - Bb (chromatic approach to Bb)
bass_notes = [
    (53, 1.5), (55, 1.875), (57, 2.25), (58, 2.625)
]
for note, time in bass_notes:
    b = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(b)

# Dante: Motif in F - D - Bb - A
sax_notes = [
    (65, 1.5), (58, 1.875), (58, 2.25), (57, 2.625)
]
for note, time in sax_notes:
    s = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(s)

# Bar 3: Diane: F7 on beat 2, A7 on beat 4
piano_notes = [
    (65, 3.0), (68, 3.0), (60, 3.0), (64, 3.0),
    (69, 3.375), (71, 3.375), (67, 3.375), (70, 3.375)
]
for note, time in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(p)

# Marcus: Walking bass line in F
# F - G - A - Bb (chromatic approach to Bb)
bass_notes = [
    (53, 3.0), (55, 3.375), (57, 3.75), (58, 4.125)
]
for note, time in bass_notes:
    b = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(b)

# Dante: Motif variation, D - Bb - A - G
sax_notes = [
    (58, 3.0), (58, 3.375), (57, 3.75), (55, 4.125)
]
for note, time in sax_notes:
    s = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(s)

# Bar 4: Diane: F7 on beat 2, A7 on beat 4
piano_notes = [
    (65, 4.5), (68, 4.5), (60, 4.5), (64, 4.5),
    (69, 4.875), (71, 4.875), (67, 4.875), (70, 4.875)
]
for note, time in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(p)

# Marcus: Walking bass line in F
# F - G - A - Bb (chromatic approach to Bb)
bass_notes = [
    (53, 4.5), (55, 4.875), (57, 5.25), (58, 5.625)
]
for note, time in bass_notes:
    b = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(b)

# Dante: Motif resolution, F - D - Bb - A
sax_notes = [
    (65, 4.5), (58, 4.875), (58, 5.25), (57, 5.625)
]
for note, time in sax_notes:
    s = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(s)

# Drums for Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625), (42, 2.25), (42, 2.4375),
    (36, 2.625), (38, 3.0), (42, 2.625), (42, 2.8125), (42, 3.0),

    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.1875), (42, 3.375), (42, 3.5625), (42, 3.75), (42, 3.9375),
    (36, 4.125), (38, 4.5), (42, 4.125), (42, 4.3125), (42, 4.5),

    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.6875), (42, 4.875), (42, 5.0625), (42, 5.25), (42, 5.4375),
    (36, 5.625), (38, 6.0), (42, 5.625), (42, 5.8125), (42, 6.0)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
