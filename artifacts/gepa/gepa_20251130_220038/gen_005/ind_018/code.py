
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# 16th note pattern: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.1875), (42, 0.375),
    (36, 1.125), (38, 1.5), (42, 1.3125), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (61, 2.25),
    (62, 2.5), (63, 2.75), (60, 3.0), (61, 3.25),
    (62, 3.5), (63, 3.75), (60, 4.0), (61, 4.25),
    (62, 4.5), (63, 4.75), (60, 5.0), (61, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (62, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),
    (62, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),
    # Bar 3: Dm7 on 2 and 4
    (62, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),
    (62, 3.5), (67, 3.5), (69, 3.5), (71, 3.5),
    # Bar 4: Dm7 on 2 and 4
    (62, 4.0), (67, 4.0), (69, 4.0), (71, 4.0),
    (62, 4.5), (67, 4.5), (69, 4.5), (71, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.75), (42, 1.625), (42, 1.75),
    (36, 2.25), (38, 2.5), (42, 2.375), (42, 2.5),
    (36, 3.0), (38, 3.25), (42, 3.125), (42, 3.25),
    (36, 3.75), (38, 4.0), (42, 3.875), (42, 4.0),
    (36, 4.5), (38, 4.75), (42, 4.625), (42, 4.75),
    (36, 5.25), (38, 5.5), (42, 5.375), (42, 5.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Dante: Tenor sax - one short motif, make it sing
# Dm7 chord: D F A C (62, 65, 69, 71)
# Motif: D -> F -> A -> rest, then return on bar 4
sax_notes = [
    (62, 1.5), (65, 1.75), (69, 2.0), (62, 3.5), (65, 3.75), (69, 4.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
