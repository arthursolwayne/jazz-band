
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

# Marcus: Walking bass line in Dm (F, Ab, D, C) with chromatic approaches
bass_notes = [
    (65, 1.5), (64, 1.875), (62, 2.25), (60, 2.625),
    (65, 3.0), (64, 3.375), (62, 3.75), (60, 4.125),
    (65, 4.5), (64, 4.875), (62, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords on 2 and 4, comp in Dm7 (F, Ab, D, C)
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (62, 2.25), (60, 2.25), (65, 2.25), (67, 2.25),
    (62, 2.625), (60, 2.625), (65, 2.625), (67, 2.625),
    # Bar 3: Dm7 on 2 and 4
    (62, 3.75), (60, 3.75), (65, 3.75), (67, 3.75),
    (62, 4.125), (60, 4.125), (65, 4.125), (67, 4.125),
    # Bar 4: Dm7 on 2 and 4
    (62, 5.25), (60, 5.25), (65, 5.25), (67, 5.25),
    (62, 5.625), (60, 5.625), (65, 5.625), (67, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Dante: Melody - one short motif, make it sing
# Dm - D (62), F (65), Ab (67), C (69), Bb (67), D (62)
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25), (69, 2.625),
    (67, 3.0), (62, 3.375),
    (62, 4.5), (65, 4.875), (67, 5.25), (69, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
