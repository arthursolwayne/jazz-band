
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet starts here (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (41, 2.625),
    (43, 3.0), (41, 3.375), (40, 3.75), (38, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Diane: Open voicings, one chord per bar, resolving on the last
# Bar 2: Dm7 (F, A, D, F#)
piano_notes = [
    (62, 1.5), (65, 1.5), (67, 1.5), (69, 1.5),
    (69, 1.875), (67, 1.875), (65, 1.875), (62, 1.875),
    (69, 2.25), (67, 2.25), (65, 2.25), (62, 2.25),
    (62, 2.625), (65, 2.625), (67, 2.625), (69, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Dante: Tenor sax motif (start on D4), short, singable, leave it hanging
sax_notes = [
    (62, 1.5), (64, 1.875), (62, 2.25), (65, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 3.0), (40, 3.375), (38, 3.75), (41, 4.125),
    (43, 4.5), (41, 4.875), (40, 5.25), (38, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Diane: Open voicings, one chord per bar, resolving on the last
# Bar 3: Gm7 (Bb, D, G, B)
piano_notes = [
    (60, 3.0), (62, 3.0), (65, 3.0), (67, 3.0),
    (67, 3.375), (65, 3.375), (62, 3.375), (60, 3.375),
    (67, 3.75), (65, 3.75), (62, 3.75), (60, 3.75),
    (60, 4.125), (62, 4.125), (65, 4.125), (67, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Dante: Tenor sax motif (start on G4), short, singable, leave it hanging
sax_notes = [
    (67, 3.0), (69, 3.375), (67, 3.75), (70, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 4.5), (40, 4.875), (38, 5.25), (41, 5.625),
    (43, 6.0), (41, 6.375), (40, 6.75), (38, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Diane: Open voicings, one chord per bar, resolving on the last
# Bar 4: C7 (E, G, C, E)
piano_notes = [
    (64, 4.5), (67, 4.5), (60, 4.5), (64, 4.5),
    (64, 4.875), (67, 4.875), (60, 4.875), (64, 4.875),
    (64, 5.25), (67, 5.25), (60, 5.25), (64, 5.25),
    (64, 5.625), (67, 5.625), (60, 5.625), (64, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Dante: Tenor sax motif (start on C5), short, singable, finish it
sax_notes = [
    (72, 4.5), (74, 4.875), (72, 5.25), (74, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums continue in bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 5):
    for offset in [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]:
        time = i * 1.5 + offset
        if offset in [0.0, 1.5, 3.0, 4.5]:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if offset in [0.375, 1.875, 3.375, 4.875]:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        if offset in [0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25]:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
