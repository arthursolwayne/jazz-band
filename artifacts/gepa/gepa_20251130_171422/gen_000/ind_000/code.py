
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375), (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875),
    (36, 1.125), (38, 1.5), (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    # Bar 2
    (41, 1.5), (42, 1.875), (40, 2.25), (40, 2.625),
    # Bar 3
    (39, 3.0), (40, 3.375), (41, 3.75), (42, 4.125),
    # Bar 4
    (40, 4.5), (39, 4.875), (38, 5.25), (38, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (45, 1.875), (43, 1.875), (40, 1.875), (38, 1.875),  # F7
    # Bar 3
    (43, 3.375), (41, 3.375), (38, 3.375), (36, 3.375),  # Dm7
    # Bar 4
    (45, 4.875), (43, 4.875), (40, 4.875), (38, 4.875)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875), (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375),
    (36, 2.625), (38, 3.0), (42, 2.625), (42, 2.75), (42, 2.875), (42, 3.0),
    # Bar 3
    (36, 3.375), (38, 3.75), (42, 3.375), (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125), (42, 4.25),
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    # Bar 4
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625), (42, 5.75), (42, 5.875), (42, 6.0), (42, 6.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax melody - short motif, make it sing
sax_notes = [
    # Bar 2
    (60, 1.5), (62, 1.875), (60, 2.25), (62, 2.625),
    # Bar 3
    (59, 3.0), (60, 3.375), (62, 3.75), (60, 4.125),
    # Bar 4
    (58, 4.5), (60, 4.875), (62, 5.25), (60, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
