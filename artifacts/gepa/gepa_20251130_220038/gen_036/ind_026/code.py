
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in D, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (62, 2.25), (65, 2.625),  # D -> F -> D -> F#
    (67, 3.0), (65, 3.375), (67, 3.75), (69, 4.125)   # G -> F# -> G -> A
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: Comping with 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#) on beat 2
    (67, 2.0), (72, 2.0), (62, 2.0), (65, 2.0),
    # Bar 3: G7 (G, B, D, F) on beat 4 (3.5)
    (72, 3.5), (76, 3.5), (67, 3.5), (69, 3.5),
    # Bar 4: C#7 (C#, E#, G#, B) on beat 2 (4.5)
    (65, 4.5), (68, 4.5), (62, 4.5), (67, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    (42, 2.75), (42, 2.875), (42, 3.0),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    (42, 4.25), (42, 4.375), (42, 4.5),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625),
    (42, 5.75), (42, 5.875), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax (start at bar 2, 1.5s)
# Motif: D (62) - F# (65) - D (62) - G (67) - rest - then back on the 4th beat
sax_notes = [
    (62, 1.5), (65, 1.875), (62, 2.25), (67, 2.625),  # first phrase
    (62, 3.5), (65, 3.875), (62, 4.25), (67, 4.625)   # second phrase
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("whisper_cry.mid")
