
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
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875)
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (36, 1.5, 0.375), (34, 1.875, 0.375), (33, 2.25, 0.375), (35, 2.625, 0.375)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (58, 1.875, 0.1875), (60, 1.875, 0.1875), (62, 1.875, 0.1875), (65, 1.875, 0.1875),
    (58, 2.625, 0.1875), (60, 2.625, 0.1875), (62, 2.625, 0.1875), (65, 2.625, 0.1875)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Sax: Melody (1.5 - 3.0s)
sax_notes = [
    # Bar 2
    (53, 1.5, 0.375), (55, 2.25, 0.375), (53, 2.625, 0.375)
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 3
    (32, 3.0, 0.375), (34, 3.375, 0.375), (36, 3.75, 0.375), (33, 4.125, 0.375)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3
    (58, 3.375, 0.1875), (60, 3.375, 0.1875), (62, 3.375, 0.1875), (65, 3.375, 0.1875),
    (58, 4.125, 0.1875), (60, 4.125, 0.1875), (62, 4.125, 0.1875), (65, 4.125, 0.1875)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Sax: Melody (3.0 - 4.5s)
sax_notes = [
    # Bar 3
    (55, 3.0, 0.375), (53, 3.75, 0.375), (50, 4.125, 0.375)
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 4
    (34, 4.5, 0.375), (32, 4.875, 0.375), (31, 5.25, 0.375), (33, 5.625, 0.375)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4
    (58, 4.875, 0.1875), (60, 4.875, 0.1875), (62, 4.875, 0.1875), (65, 4.875, 0.1875),
    (58, 5.625, 0.1875), (60, 5.625, 0.1875), (62, 5.625, 0.1875), (65, 5.625, 0.1875)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Sax: Melody (4.5 - 6.0s)
sax_notes = [
    # Bar 4
    (53, 4.5, 0.375), (50, 5.25, 0.375), (53, 5.625, 0.375)
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
