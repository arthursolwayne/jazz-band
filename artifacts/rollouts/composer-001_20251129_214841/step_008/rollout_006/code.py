
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (65, 2.25, 0.375),
    (64, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass walking line
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375),
    (51, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: C7 on 2
    (60, 1.875, 0.375), (64, 1.875, 0.375),
    # Bar 2: C7 on 4
    (60, 2.625, 0.375), (64, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (repeat and resolve)
sax_notes = [
    (62, 3.0, 0.375), (64, 3.375, 0.375), (65, 3.75, 0.375),
    (67, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass walking line
bass_notes = [
    (52, 3.0, 0.375), (53, 3.375, 0.375), (54, 3.75, 0.375),
    (55, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3: C7 on 2
    (60, 3.375, 0.375), (64, 3.375, 0.375),
    # Bar 3: C7 on 4
    (60, 4.125, 0.375), (64, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (finish)
sax_notes = [
    (67, 4.5, 0.375), (64, 4.875, 0.375), (62, 5.25, 0.375),
    (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass walking line
bass_notes = [
    (56, 4.5, 0.375), (57, 4.875, 0.375), (58, 5.25, 0.375),
    (59, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4: C7 on 2
    (60, 4.875, 0.375), (64, 4.875, 0.375),
    # Bar 4: C7 on 4
    (60, 5.625, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums for Bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.1875, end=start + 0.375)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.5625, end=start + 0.75)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.9375, end=start + 1.125)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.5)

    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
