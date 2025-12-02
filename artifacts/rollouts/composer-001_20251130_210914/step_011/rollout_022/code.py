
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D minor
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625),
    (63, 3.0), (64, 3.375), (62, 3.75), (63, 4.125),
    (64, 4.5), (65, 4.875), (62, 5.25), (63, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (67, 1.75), (71, 1.75), (74, 1.75), (76, 1.75),  # D7 on beat 2
    (67, 2.75), (71, 2.75), (74, 2.75), (76, 2.75),  # D7 on beat 4
    # Bar 3 (3.0 - 4.5s)
    (67, 3.75), (71, 3.75), (74, 3.75), (76, 3.75),  # D7 on beat 2
    (67, 4.75), (71, 4.75), (74, 4.75), (76, 4.75),  # D7 on beat 4
    # Bar 4 (4.5 - 6.0s)
    (67, 5.75), (71, 5.75), (74, 5.75), (76, 5.75)   # D7 on beat 2
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.875), (38, 5.25), (42, 5.25)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Motif in D minor, one short phrase with a suspended ending
sax_notes = [
    (62, 1.5), (65, 1.625), (62, 1.75), (65, 1.875),
    (62, 2.0), (65, 2.125), (62, 2.25), (65, 2.375),
    (62, 2.5), (65, 2.625), (62, 2.75), (65, 2.875),
    (62, 3.0), (65, 3.125), (62, 3.25), (65, 3.375),
    (62, 3.5), (65, 3.625), (62, 3.75), (65, 3.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
