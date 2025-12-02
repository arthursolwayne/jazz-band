
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
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, Fm key
bass_notes = [
    (64, 1.5), (63, 1.875), (65, 2.25), (62, 2.625),  # F, Eb, G, D
    (64, 3.0), (63, 3.375), (65, 3.75), (62, 4.125),  # F, Eb, G, D
    (64, 4.5), (63, 4.875), (65, 5.25), (62, 5.625)   # F, Eb, G, D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (57, 1.5), (60, 1.5), (62, 1.5), (64, 1.5),  # F7
    (64, 2.25), (67, 2.25), (69, 2.25), (71, 2.25),  # Bb7
    # Bar 3
    (57, 3.0), (60, 3.0), (62, 3.0), (64, 3.0),  # F7
    (64, 3.75), (67, 3.75), (69, 3.75), (71, 3.75),  # Bb7
    # Bar 4
    (57, 4.5), (60, 4.5), (62, 4.5), (64, 4.5),  # F7
    (64, 5.25), (67, 5.25), (69, 5.25), (71, 5.25)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, D (Fm7), then rest, then repeat
sax_notes = [
    (64, 1.5), (62, 1.875), (62, 2.25), (67, 2.625),  # F, Ab, Bb, D
    (64, 3.0), (62, 3.375), (62, 3.75), (67, 4.125),  # F, Ab, Bb, D
    (64, 5.25), (62, 5.625)  # F, Ab
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
