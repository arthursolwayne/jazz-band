
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
    (36, 0.0), (38, 0.375), (42, 0.0),
    (36, 1.125), (38, 1.5), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line in Dm (F, Ab, D, C)
bass_notes = [
    (65, 1.5), (63, 1.875), (62, 2.25), (60, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    # Dm7 (D, F, A, C) on beat 2 (1.875)
    (62, 1.875), (64, 1.875), (67, 1.875), (60, 1.875),
    # G7 (G, B, D, F) on beat 4 (2.625)
    (67, 2.625), (71, 2.625), (69, 2.625), (64, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5),
    (36, 2.625), (38, 3.0), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante - Sax solo (simple motif: D, F, Bb, D)
sax_notes = [
    (62, 1.5), (64, 1.875), (66, 2.25), (62, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Walking bass line in Dm (F, Ab, D, C)
bass_notes = [
    (65, 3.0), (63, 3.375), (62, 3.75), (60, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    # Dm7 (D, F, A, C) on beat 2 (3.375)
    (62, 3.375), (64, 3.375), (67, 3.375), (60, 3.375),
    # G7 (G, B, D, F) on beat 4 (4.125)
    (67, 4.125), (71, 4.125), (69, 4.125), (64, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.0),
    (36, 4.125), (38, 4.5), (42, 4.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante - Sax solo (repeat motif with variation: D, F, Bb, Eb)
sax_notes = [
    (62, 3.0), (64, 3.375), (66, 3.75), (63, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Walking bass line in Dm (F, Ab, D, C)
bass_notes = [
    (65, 4.5), (63, 4.875), (62, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    # Dm7 (D, F, A, C) on beat 2 (4.875)
    (62, 4.875), (64, 4.875), (67, 4.875), (60, 4.875),
    # G7 (G, B, D, F) on beat 4 (5.625)
    (67, 5.625), (71, 5.625), (69, 5.625), (64, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.5),
    (36, 5.625), (38, 6.0), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante - Sax solo (finish motif: D, F, Bb, D)
sax_notes = [
    (62, 4.5), (64, 4.875), (66, 5.25), (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
