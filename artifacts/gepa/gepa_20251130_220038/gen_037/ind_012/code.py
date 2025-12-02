
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

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (64, 1.5), (65, 1.75), (63, 2.0), (62, 2.25),
    (64, 2.5), (65, 2.75), (63, 3.0), (62, 3.25),
    (64, 3.5), (65, 3.75), (63, 4.0), (62, 4.25),
    (64, 4.5), (65, 4.75), (63, 5.0), (62, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (72, 1.75), (70, 1.75), (68, 1.75), (67, 1.75),  # F7
    (72, 2.25), (70, 2.25), (68, 2.25), (67, 2.25),  # F7
    # Bar 3
    (72, 3.25), (70, 3.25), (68, 3.25), (67, 3.25),  # F7
    (72, 3.75), (70, 3.75), (68, 3.75), (67, 3.75),  # F7
    # Bar 4
    (72, 4.75), (70, 4.75), (68, 4.75), (67, 4.75),  # F7
    (72, 5.25), (70, 5.25), (68, 5.25), (67, 5.25)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Sax: Motif starting at 1.5s
# Fm short motif (F, Ab, Bb, D)
sax_notes = [
    (65, 1.5), (62, 1.75), (62, 2.0), (64, 2.25),
    (65, 2.5), (62, 2.75), (62, 3.0), (64, 3.25),
    (65, 3.5), (62, 3.75), (62, 4.0), (64, 4.25),
    (65, 4.5), (62, 4.75), (62, 5.0), (64, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_russo_intro.mid')
