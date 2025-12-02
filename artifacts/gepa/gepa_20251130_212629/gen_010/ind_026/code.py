
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    
    (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875), (36, 3.0, 0.375)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm7 -> Bb -> Ab -> G
sax_notes = [
    (60, 1.5, 0.375), (62, 1.875, 0.375), (57, 2.25, 0.375), (59, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (64, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375), (68, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: F7 on 2 and 4
piano_notes = [
    (60, 1.875, 0.375), (64, 1.875, 0.375), (65, 1.875, 0.375), (67, 1.875, 0.375),
    (60, 2.625, 0.375), (64, 2.625, 0.375), (65, 2.625, 0.375), (67, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Bb -> F -> Eb -> D
sax_notes = [
    (62, 3.0, 0.375), (60, 3.375, 0.375), (58, 3.75, 0.375), (57, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Fm (Bb, B, Db, D)
bass_notes = [
    (62, 3.0, 0.375), (63, 3.375, 0.375), (65, 3.75, 0.375), (66, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: F7 on 2 and 4
piano_notes = [
    (60, 3.375, 0.375), (64, 3.375, 0.375), (65, 3.375, 0.375), (67, 3.375, 0.375),
    (60, 4.125, 0.375), (64, 4.125, 0.375), (65, 4.125, 0.375), (67, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Ab -> F -> Eb -> D (ending on D)
sax_notes = [
    (57, 4.5, 0.375), (60, 4.875, 0.375), (58, 5.25, 0.375), (57, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (64, 4.5, 0.375), (65, 4.875, 0.375), (67, 5.25, 0.375), (68, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: F7 on 2 and 4
piano_notes = [
    (60, 4.875, 0.375), (64, 4.875, 0.375), (65, 4.875, 0.375), (67, 4.875, 0.375),
    (60, 5.625, 0.375), (64, 5.625, 0.375), (65, 5.625, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (36, 4.5, 0.375),
    
    (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875), (36, 6.0, 0.375)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
