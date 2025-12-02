
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches, no repeating notes
bass_notes = [
    (64, 1.5), (65, 1.875), (63, 2.25), (62, 2.625),
    (64, 3.0), (65, 3.375), (63, 3.75), (62, 4.125),
    (64, 4.5), (65, 4.875), (63, 5.25), (62, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875), (64, 1.875), # F7
    (65, 2.625), (69, 2.625), # G7
    # Bar 3
    (60, 3.375), (64, 3.375), # F7
    (65, 4.125), (69, 4.125), # G7
    # Bar 4
    (60, 4.875), (64, 4.875), # F7
    (65, 5.625), (69, 5.625)  # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25))

# Dante: saxophone, short motif, start it, leave it hanging, come back
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.25),
    (60, 2.625), (62, 2.75), (60, 3.0),
    (62, 3.5), (64, 3.75), (62, 4.25),
    (60, 4.625), (62, 4.75), (60, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
