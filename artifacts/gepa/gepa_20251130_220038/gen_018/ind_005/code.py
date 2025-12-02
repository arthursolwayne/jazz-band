
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
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (65, 2.25),  # Dm7: D F A C
    (65, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),  # G7: G B D F
    (60, 3.5), (62, 3.75), (64, 4.0), (65, 4.25),  # Cm7: C Eb G Bb
    (65, 4.5), (64, 4.75), (62, 5.0), (60, 5.25)   # F7: F A C E
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (62, 2.0), (65, 2.0), (69, 2.0), (72, 2.0),
    # Bar 3: G7 (G B D F)
    (67, 3.0), (71, 3.0), (69, 3.0), (65, 3.0),
    # Bar 4: Cm7 (C Eb G Bb)
    (60, 4.0), (64, 4.0), (69, 4.0), (67, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax, one short motif, start it, leave it hanging
# Motif: D (62) -> C# (61) -> D (62) -> B (61), but only play first three notes
# Then rest on bar 2, then come back and finish in bar 3
sax_notes = [
    # Bar 2 (start motif)
    (62, 1.5), (61, 1.75), (62, 2.0),
    # Bar 3 (finish motif)
    (61, 3.0),
    # Bar 3 (melody continuation)
    (64, 3.25), (62, 3.5), (60, 3.75), (62, 4.0),
    # Bar 4 (resolution)
    (64, 4.25), (62, 4.5), (60, 4.75), (62, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
