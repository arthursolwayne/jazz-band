
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
    (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125), (36, 1.5),
    (38, 1.875), (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625),
    (42, 2.25), (42, 2.4375), (42, 2.625), (42, 2.8125), (42, 3.0),
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# D minor scale: D, Eb, F, G, Ab, Bb, C
# Walking bass line in D minor
bass_notes = [
    (62, 1.5), (63, 1.875), (64, 2.25), (65, 2.625),  # D, Eb, F, G
    (66, 3.0), (67, 3.375), (68, 3.75), (69, 4.125),  # Ab, Bb, C, D
    (62, 4.5), (63, 4.875), (64, 5.25), (65, 5.625),  # D, Eb, F, G
    (66, 6.0)                                          # Ab
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# A7: A, C#, E, G
# D7: D, F#, A, C
# A7: A, C#, E, G
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5), (67, 1.5), (69, 1.5), (64, 1.5),  # D7
    (62, 2.25), (67, 2.25), (69, 2.25), (64, 2.25),  # D7
    # Bar 3 (3.0 - 4.5s)
    (65, 3.0), (70, 3.0), (72, 3.0), (67, 3.0),  # A7
    (65, 3.75), (70, 3.75), (72, 3.75), (67, 3.75),  # A7
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5), (67, 4.5), (69, 4.5), (64, 4.5),  # D7
    (62, 5.25), (67, 5.25), (69, 5.25), (64, 5.25),  # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# You: Tenor sax, one short motif, make it sing
# D, Eb, F#, G
sax_notes = [
    (62, 1.5), (63, 1.625), (66, 1.75), (67, 1.875),  # Motif
    (62, 3.0), (63, 3.125), (66, 3.25), (67, 3.375),  # Repeat
    (62, 4.5), (63, 4.625), (66, 4.75), (67, 4.875),  # Repeat
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
