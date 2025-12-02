
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

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (65, 2.25),
    (67, 2.5), (68, 2.75), (69, 3.0), (70, 3.25),
    (72, 3.5), (73, 3.75), (74, 4.0), (75, 4.25),
    (77, 4.5), (78, 4.75), (79, 5.0), (80, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.0), (67, 2.0), (71, 2.0), (72, 2.0),  # D7
    (67, 3.0), (71, 3.0), (76, 3.0), (77, 3.0),  # G7
    (69, 4.0), (72, 4.0), (76, 4.0), (77, 4.0),  # Bm7
    (67, 5.0), (71, 5.0), (76, 5.0), (77, 5.0)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (66), G (67), D (62)
sax_notes = [
    (62, 1.5), (66, 1.75), (67, 2.0), (62, 2.25),
    (66, 3.0), (67, 3.25), (62, 3.5), (66, 3.75),
    (67, 4.0), (62, 4.25), (66, 4.5), (67, 4.75),
    (62, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
