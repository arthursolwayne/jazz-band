
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875),
    (36, 1.125), (38, 1.5), (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus bass: walking line, chromatic approaches, never the same note twice
# Fm7 chord: F, Ab, C, Eb
bass_line = [
    (64, 1.5), (65, 1.875), (62, 2.25), (63, 2.625),
    (62, 2.875), (63, 3.25), (65, 3.625), (64, 4.0),
    (64, 4.25), (63, 4.625), (62, 5.0), (61, 5.375),
    (62, 5.625), (63, 6.0)
]
for note, time in bass_line:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, C, Eb
# Bb7: Bb, D, F, Ab
# Cm7: C, Eb, G, Bb
# Eb7: Eb, G, Bb, D
piano_notes = [
    # Bar 2
    (53, 1.5), (58, 1.5), (60, 1.5), (62, 1.5),
    (55, 1.875), (60, 1.875), (62, 1.875), (64, 1.875),
    # Bar 3
    (60, 2.25), (62, 2.25), (64, 2.25), (65, 2.25),
    (58, 2.625), (60, 2.625), (62, 2.625), (64, 2.625),
    # Bar 4
    (62, 3.0), (64, 3.0), (65, 3.0), (67, 3.0),
    (60, 3.375), (62, 3.375), (64, 3.375), (67, 3.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375),
    (36, 2.625), (38, 3.0), (42, 2.625), (42, 2.75), (42, 2.875), (42, 3.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3
drum_notes = [
    (36, 3.25), (38, 3.625), (42, 3.25), (42, 3.375), (42, 3.5), (42, 3.625),
    (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    (36, 4.375), (38, 4.75), (42, 4.375), (42, 4.5), (42, 4.625), (42, 4.75)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4
drum_notes = [
    (36, 5.0), (38, 5.375), (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375),
    (42, 5.5), (42, 5.625), (42, 5.75), (42, 5.875),
    (36, 6.125), (38, 6.5), (42, 6.125), (42, 6.25), (42, 6.375), (42, 6.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante sax: Start with a whisper, build to a cry
# Fm7: F (65), Ab (67), C (69), Eb (66)
# Create a motif that feels like a whisper at first, then a cry
sax_notes = [
    (65, 1.5), (67, 1.625), (69, 1.75), (66, 1.875),
    (65, 2.0), (67, 2.125), (69, 2.25), (66, 2.375),
    (65, 2.5), (67, 2.625), (69, 2.75), (66, 2.875),
    (65, 3.0), (67, 3.125), (69, 3.25), (66, 3.375),
    (65, 3.5), (67, 3.625), (69, 3.75), (66, 3.875),
    (65, 4.0), (67, 4.125), (69, 4.25), (66, 4.375),
    (65, 4.5), (67, 4.625), (69, 4.75), (66, 4.875),
    (65, 5.0), (67, 5.125), (69, 5.25), (66, 5.375),
    (65, 5.5), (67, 5.625), (69, 5.75), (66, 5.875),
    (65, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
