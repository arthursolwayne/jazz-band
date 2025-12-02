
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

# Bass: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (61, 2.25), (64, 2.625),
    (65, 3.0), (64, 3.375), (62, 3.75), (60, 4.125),
    (62, 4.5), (63, 4.875), (61, 5.25), (64, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # D7 on beat 2
    (64, 3.5), (67, 3.5), (69, 3.5), (71, 3.5),  # D7 on beat 4
    (64, 5.0), (67, 5.0), (69, 5.0), (71, 5.0)   # D7 on beat 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0),  # start the motif
    (64, 2.25), (62, 2.5), (64, 2.75), (62, 3.0),  # leave it hanging
    (64, 3.5), (62, 3.75), (64, 4.0),  # come back
    (62, 4.5), (64, 4.75), (62, 5.0)   # finish it
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums continue in bars 2-4
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
midi.save('jazz_intro.mid')
