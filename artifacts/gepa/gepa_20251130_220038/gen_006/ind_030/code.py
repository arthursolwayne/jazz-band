
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches, no repeats
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (65, 2.625, 0.375), # Dm7
    (67, 2.875, 0.375), (69, 3.25, 0.375), (68, 3.625, 0.375), (70, 4.0, 0.375), # G7
    (67, 4.375, 0.375), (69, 4.75, 0.375), (68, 5.125, 0.375), (70, 5.5, 0.375)  # Cmaj7
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 2.25, 0.1875), (71, 2.25, 0.1875), (69, 2.25, 0.1875), (64, 2.25, 0.1875), # Dm7
    (67, 3.25, 0.1875), (71, 3.25, 0.1875), (69, 3.25, 0.1875), (62, 3.25, 0.1875), # G7
    (67, 4.25, 0.1875), (71, 4.25, 0.1875), (69, 4.25, 0.1875), (64, 4.25, 0.1875)  # Cmaj7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: motif in D, sing, leave it hanging, come back
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (65, 2.25, 0.375), (62, 2.625, 0.375), # First phrase
    (64, 3.0, 0.375), (67, 3.375, 0.375), (69, 3.75, 0.375), (67, 4.125, 0.375), # Answer
    (69, 4.5, 0.375), (67, 4.875, 0.375), (65, 5.25, 0.375), (62, 5.625, 0.375)  # Resolution
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (36, 2.625, 0.375), (38, 2.875, 0.375), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 2.875, 0.1875), (42, 3.0625, 0.1875),
    (36, 3.5, 0.375), (38, 3.875, 0.375), (42, 3.5, 0.1875),
    (42, 3.6875, 0.1875), (42, 3.875, 0.1875), (42, 4.0625, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
